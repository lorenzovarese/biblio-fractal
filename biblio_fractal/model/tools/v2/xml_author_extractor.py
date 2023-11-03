import argparse
from lxml import etree
import os

def collect_collaborators(input_file, author_name):
    """
    Collects a set of collaborators for a given author from an XML file.

    Parameters:
    - input_file (str): Path to the XML file to be parsed.
    - author_name (str): The name of the author whose collaborators are to be found.

    Returns:
    - set: A set of unique collaborator names.
    """
    collaborators = set()
    context = etree.iterparse(input_file, events=('end',), tag='author')
    for event, elem in context:
        if elem.text == author_name:
            # Add all authors in the same entry except the target author as collaborators
            for sibling in elem.getparent():
                if sibling.tag == 'author' and sibling.text != author_name:
                    collaborators.add(sibling.text)
            elem.clear()
    return collaborators

def process_tag(context, tag, author_name, collaborators, f_out):
    """
    Processes each XML tag and writes relevant entries to the output file.

    Parameters:
    - context (iterparse context): Iterator providing (event, elem) pairs.
    - tag (str): The specific XML tag to look for (e.g., 'article').
    - author_name (str): The author name to filter the XML entries.
    - collaborators (set): A set of collaborator names.
    - f_out (file object): The output file to which the entries are written.
    """
    for event, elem in context:
        if elem.tag == tag:
            if any(author.text == author_name or author.text in collaborators for author in elem.findall('author')):
                f_out.write(etree.tostring(elem, pretty_print=True, encoding='ISO-8859-1', xml_declaration=False))
                f_out.write(b"\n")
            elem.clear()
            # Clean up preceding siblings from memory to keep a small footprint
            while elem.getprevious() is not None:
                del elem.getparent()[0]

def extract_author_data(input_file, author_name, collaborators, output_file):
    """
    Extracts and writes the data of a specified author and their collaborators to an output file.

    Parameters:
    - input_file (str): Path to the input XML file.
    - author_name (str): The name of the target author.
    - collaborators (set): A set of the author's collaborators.
    - output_file (str): Path to the output XML file.
    """
    # Write XML header if output file is new or empty
    if not os.path.exists(output_file) or os.path.getsize(output_file) == 0:
        with open(output_file, 'wb') as f_out:
            f_out.write(b"<?xml version='1.0' encoding='ISO-8859-1'?>\n<dblp>\n")

    tags_to_process = ['article', 'incollection', 'inproceedings']
    with open(output_file, 'ab') as f_out:
        for tag in tags_to_process:
            context = etree.iterparse(input_file, events=('end',), tag=tag, huge_tree=True)
            process_tag(context, tag, author_name, collaborators, f_out)

        # Finalize the output file with a closing tag
        f_out.write(b'</dblp>\n')

if __name__ == "__main__":
    # Command-line interface setup
    parser = argparse.ArgumentParser(description='Extract data for a specified author from an XML database.')
    parser.add_argument('author_name', type=str, help='The name of the author for whom to extract data.')
    parser.add_argument('--collaborators', action='store_true', help='Flag to include author\'s collaborators in the output.')

    args = parser.parse_args()
    author_name = args.author_name
    author_file_name = ''.join(char for char in author_name if char.isalnum())

    # Define paths for input and output files
    workspace = os.getcwd()
    input_file_path = os.path.join(workspace, "input", "dblp_without_entities.xml")

    # Execute data extraction with or without collaborators based on the command-line flag
    if args.collaborators:
        print("Collecting collaborators...")
        collaborators = collect_collaborators(input_file_path, author_name)
        print(f"Found {len(collaborators)} collaborators.")
        output_file_path = os.path.join(workspace, "output", f"{author_file_name}_author_db_with_collaborators.xml")
        print(f"Extracting author's data with collaborators...")
        extract_author_data(input_file_path, author_name, collaborators, output_file_path)
    else:
        collaborators = set() # Set of collaborators is empty if the flag is not set
        output_file_path = os.path.join(workspace, "output", f"{author_file_name}_author_db.xml")
        print(f"Extracting author's data...")
        extract_author_data(input_file_path, author_name, collaborators, output_file_path)
