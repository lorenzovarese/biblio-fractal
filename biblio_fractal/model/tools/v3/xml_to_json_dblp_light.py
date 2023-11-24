from lxml import etree
import json
import os

def parse_xml_to_json(input_file_path, output_file_path):
    """
    This function parses an XML file and converts it into a JSON file.

    It iterates over all elements in the XML file, converting each valid element
    into a dictionary, formatted as specified. Records are only appended if the
    author list is not empty and the tag is not 'www'.

    Parameters:
    - input_file_path (str): The path to the XML file to be parsed.
    - output_file_path (str): The path to the JSON file to be created.
    """
    # Use lxml for parsing
    tree = etree.parse(input_file_path)
    root = tree.getroot()

    # Initialize a list to store all the records
    all_records = []

    # Iterate over each element in the root
    for elem in root.iter():
        # Skip the element if it's tagged with 'www'
        if elem.tag == 'www':
            continue

        # Collect authors
        authors = [author.text for author in elem.findall('author')]

        # Only proceed if authors list is not empty
        if authors:
            record_dict = {
                'dblp_tag': elem.tag,
                'key_parts': elem.get('key').split("/") if elem.get('key') else [],
                'authors': authors,
                'title': elem.find('title').text if elem.find('title') is not None else "",
                'year': int(elem.find('year').text) if elem.find('year') is not None else "",
                'url': elem.find('url').text if elem.find('url') is not None else ""
            }

            # Append the record dictionary to the list of all records
            all_records.append(record_dict)

    # Open the output file and write the JSON data
    with open(output_file_path, 'w') as f:
        json.dump(all_records, f, indent=1)

# Example usage
if __name__ == "__main__":
    workspace = os.getcwd()
    input_file_path = os.path.join(workspace, "input", "dblp_without_entities.xml")
    output_file_path = os.path.join(workspace, "light_db_dblp.xml")
    parse_xml_to_json(input_file_path, output_file_path)
