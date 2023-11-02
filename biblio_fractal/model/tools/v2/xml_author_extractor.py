import argparse
from lxml import etree
import os

def process_tag(context, tag, author_name, f_out):
    """
    This function processes the XML elements from the parsed file. If an element has the specified tag
    and contains the given author's name, it is written to the output file.

    Parameters:
    - context (iterparse context): The iterator providing (event, elem) pairs.
    - tag (str): The specific tag that we are interested in (e.g., 'article').
    - author_name (str): The name of the author whose entries are being extracted.
    - f_out (file object): The file object to write the output to.

    The function has no return value since it performs file I/O operations.
    """
    for event, elem in context:
        if elem.tag == tag:
            if any(author.text == author_name for author in elem.findall('author')):
                f_out.write(etree.tostring(elem, pretty_print=True, encoding='ISO-8859-1', xml_declaration=False))
                f_out.write(b"\n")
            elem.clear()
            # Clean up preceding siblings to free memory
            while elem.getprevious() is not None:
                del elem.getparent()[0]

def extract_entities_by_author(input_file, author_name, output_file):
    """
    Extracts entities related to a specific author from an XML file and writes them to a separate file.

    Parameters:
    - input_file (str): The path to the source XML file.
    - author_name (str): The author name to filter the XML data by.
    - output_file (str): The path to the output XML file where filtered data is written.

    The function checks if the output file exists and whether it is empty before appending content to it.
    It does not return a value.
    """
    # Check if the output file is empty or doesn't exist, then write the header
    if not os.path.exists(output_file) or os.path.getsize(output_file) == 0:
        with open(output_file, 'wb') as f_out:
            f_out.write(b"<?xml version='1.0' encoding='ISO-8859-1'?>\n<dblp>\n")

    tags_to_process = ['article', 'incollection', 'inproceedings']
    with open(output_file, 'ab') as f_out:
        for tag in tags_to_process:
            context = etree.iterparse(input_file, events=('end',), tag=tag, huge_tree=True)
            process_tag(context, tag, author_name, f_out)

        # Append the final closing tag for the root element
        f_out.write(b'</dblp>\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a new XML file with all the data of a single author.')
    parser.add_argument('author_name', type=str, help='Name of the author to search for')

    args = parser.parse_args()
    author_name = args.author_name
    author_file_name = ''.join(char for char in str(author_name) if char.isalnum())

    workspace = os.getcwd()
    input_file_path = os.path.join(workspace, "input", "dblp_without_entities.xml")
    output_file_path = os.path.join(workspace, "output", f"{author_file_name}_author_db.xml")

    extract_entities_by_author(input_file_path, author_name, output_file_path)
