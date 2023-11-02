from lxml import etree
import os
import argparse

def find_tags_containing_subtag(file_path, subtag):
    # Initialize lxml parser
    context = etree.iterparse(file_path, events=("end",))
    
    # Set to store unique tags containing the specified sub-tag
    unique_tags_with_subtag = set()
    
    for event, elem in context:
        # Check for the presence of the specified sub-tag
        subtag_elements = elem.findall(f".//{subtag}")
        
        if len(subtag_elements) > 0:
            # Add the tag to the set of unique tags containing the sub-tag
            unique_tags_with_subtag.add(elem.tag)
        
        # Clear the element to save memory
        elem.clear()

    # Return unique tags containing the sub-tag
    return unique_tags_with_subtag

if __name__ == "__main__":
    # Argument parsing
    parser = argparse.ArgumentParser(description="Find unique tags containing a specified subtag in an XML file.")
    parser.add_argument("subtag", type=str, help="Subtag to search for")
    args = parser.parse_args()

    # Path to your XML file
    workspace = os.getcwd()
    input_file_path = os.path.join(workspace, "input", "dblp_without_entities.xml")

    # Search for tags containing the subtag passed as a command-line argument
    unique_tags_with_subtag = find_tags_containing_subtag(input_file_path, args.subtag)

    print(f"Unique tags that can contain at least one '{args.subtag}':", unique_tags_with_subtag)

    #output example 1: Unique tags that can contain at least one 'author': {'inproceedings', 'mastersthesis', 'book', 'article', 'data', 'incollection', 'www', 'phdthesis', 'proceedings'}
    #output example 2: Unique tags that can contain at least one 'editor': {'inproceedings', 'www', 'proceedings', 'article', 'book'}