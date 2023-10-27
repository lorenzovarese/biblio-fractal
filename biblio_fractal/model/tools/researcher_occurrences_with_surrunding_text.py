import os
import argparse
from lxml import etree

def count_and_print_author_occurrences(file_path, author_name, output_file_path):
    # Counter for occurrences
    count = 0

    #Disclamer
    disclaimer_author_editor = f"#WARNING: This tool prints all occurrences of '{author_name}', but please note that there is one occurrence related to the '<www ...>' tag, which collects data about webpages and the author's affiliation. \nAdditionally, there may be one or more occurrences of the author's name that are NOT related to '<author>' but are associated with '<editor>' in proceedings. \nKeep this in mind if you observe a count of occurrences higher than the actual results in the 'db_single_researcher_generator.py' output.\n\n"

    with open(file_path, 'r', encoding='ISO-8859-1') as f:
        xml_content = f.read()
    
    # Remove the encoding declaration from the XML string
    xml_content = xml_content.replace('<?xml version="1.0" encoding="ISO-8859-1"?>', '')
    
    # Initialize lxml parser
    root = etree.fromstring(xml_content)
    
    # Keep track of the last found position
    last_found_pos = 0
    
    with open(output_file_path, 'w') as out_f:
        out_f.write(f"{disclaimer_author_editor}")
        for elem in root.iter("author"):
            if elem.text == author_name:
                count += 1
                
                pos = xml_content.find(elem.text, last_found_pos)
                last_found_pos = pos + len(elem.text)
                
                start = max(0, pos - 500)
                end = pos + len(elem.text) + 500
                
                surrounding_text = xml_content[start:end]
                
                out_f.write(f"# Author Found [{count}] #\n{surrounding_text}\n\n")
        
        out_f.write(f"\n### Total occurrences of {author_name}: {count}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find occurrences of an author in an XML file.')
    parser.add_argument('author_name', type=str, help='Name of the author to search for')

    args = parser.parse_args()
    author_name = args.author_name
    author_file_name = ''.join(char for char in str(author_name) if char.isalnum())

    workspace = os.getcwd()
    input_file_path = os.path.join(workspace, "input", "dblp_without_entities.xml")
    output_file_path = os.path.join(workspace, "output", f"{author_file_name}_findings.txt")

    count_and_print_author_occurrences(input_file_path, author_name, output_file_path)
