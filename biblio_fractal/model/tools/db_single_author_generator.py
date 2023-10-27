from lxml import etree
from copy import deepcopy
import argparse, os, sys
from tqdm import tqdm

def generate_author_db(file_path, author_name, output_file_path):
    # Initialize an empty tree for the output
    root = etree.Element("dblp")
    output_tree = etree.ElementTree(element=root)

    # Add XML comment at the top of the output tree
    script_name = sys.argv[0]
    comment = etree.Comment(f"\n WARNING\n The '{script_name}' generates a database that includes entries where the specified name appears as an <author>. \nIf the person is listed under other roles such as <editor>, those entries will be ignored and not included in the database.\n")
    root.addprevious(comment)

    # Initialize lxml parser
    context = etree.iterparse(file_path, events=("end",), tag=("article", "incollection", "proceedings", "inproceedings", "series", "journal", "book", "www"))

    # Initialize a counter for the total number of elements found
    count = 0

    # Wrap the context with tqdm for a progress bar
    for event, elem in tqdm(context):
        # Search for articles or incollections with the given author
        author_elements = elem.findall(".//author")

        for author in author_elements:
            if author.text == author_name:
                root.append(deepcopy(elem))
                count += 1  # Increment the counter
                break  # No need to check other authors for this article/incollection

        # Clear the element to save memory
        elem.clear()

    # Print the total count of elements found
    print(f"Total count of elements found for author {author_name}: {count} (please verify if it matches the website)")
    print(f"The count of elements attributed to '{author_name}' as <author> in the output XML file might be lower." )

    # Write the output XML tree to a file
    output_tree.write(output_file_path, pretty_print=True, xml_declaration=True, encoding="ISO-8859-1")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a new XML file with all the data of a single author.')
    parser.add_argument('author_name', type=str, help='Name of the author to search for')

    args = parser.parse_args()
    author_name = args.author_name
    author_file_name = ''.join(char for char in str(author_name) if char.isalnum())

    workspace = os.getcwd()
    input_file_path = os.path.join(workspace, "input", "dblp_without_entities.xml")
    output_file_path = os.path.join(workspace, "output", f"{author_file_name}_author_db.xml")

    # Path to your XML file and the author name to search for
    generate_author_db(input_file_path, author_name, output_file_path)
