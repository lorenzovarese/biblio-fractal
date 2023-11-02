import argparse
import os
import xml.etree.ElementTree as ET
import json

def parse_xml_to_json(input_file_path, output_file_path):
    """
    This function parses an XML file and converts it into a JSON file.

    Each element in the XML file is converted into a dictionary where the tag name
    is stored under the 'dblp_tag' key, attributes under their respective keys, and
    child elements are added with their tags as keys and text content as values.
    If an element has multiple children with the same tag (e.g., 'author'), they are
    aggregated into a list.

    Parameters:
    - input_file_path (str): The path to the XML file to be parsed.
    - output_file_path (str): The path to the JSON file to be created.

    The function does not return any value. The output is written to a JSON file.
    """
    # Parse the XML file and get the root element
    tree = ET.parse(input_file_path)
    root = tree.getroot()

    # Initialize a list to store all the records
    all_records = []

    # Iterate over each element in the root
    for elem in root:
        # Initialize a dictionary with the tag name of the element
        record_dict = {'dblp_tag': elem.tag}
        # List to store multiple authors
        author_list = []
        
        # Store the 'key' attribute in the dictionary, if it exists
        if 'key' in elem.attrib:
            key_parts = elem.attrib['key'].split('/')
            record_dict['key_parts'] = key_parts

        # Iterate over each child of the current element
        for child in elem:
            if child.tag == "author":
                # Append the text of each 'author' tag to the author list
                author_list.append(child.text)
            else:
                # Add other tags as keys and their text as values
                record_dict[child.tag] = child.text

        # Add the author list to the record dictionary under the key 'author'
        if author_list:
            record_dict["author"] = author_list

        # Append the record dictionary to the list of all records
        all_records.append(record_dict)

    # Open the output file and write the JSON data
    with open(output_file_path, 'w') as f:
        json.dump(all_records, f, indent=4)

# Command-line interface section
if __name__ == "__main__":
    # Define the command-line arguments
    parser = argparse.ArgumentParser(description='Converts XML data of a specified author to JSON format.')
    parser.add_argument('author_name', type=str, help='Name of the author to convert data for')

    # Parse the command-line arguments
    args = parser.parse_args()
    author_name = args.author_name
    author_file_name = ''.join(char for char in str(author_name) if char.isalnum())

    # Get the current working directory
    workspace = os.getcwd()
    # Construct the input and output file paths
    input_file_path = os.path.join(workspace, "output", f"{author_file_name}_author_db.xml")
    output_file_path = os.path.join(workspace, "output", f"{author_file_name}_author_db.json")

    # Call the function to convert the XML to JSON
    parse_xml_to_json(input_file_path, output_file_path)
