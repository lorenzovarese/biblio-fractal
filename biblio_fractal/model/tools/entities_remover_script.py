import re
import os

def remove_entities(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        xml_content = infile.read()

    # Regex to match &something;
    pattern = r'&([a-zA-Z]+);'

    def replacer(match):
        entity = match.group(1)
        return entity[0] if entity else ''

    # Replace entities
    new_xml_content = re.sub(pattern, replacer, xml_content)

    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(new_xml_content)

if __name__ == '__main__':

    workspace = os.getcwd()
    input_file_path = os.path.join(workspace, "input", "dblp.xml")
    
    # The file will be placed inside the 'input' folder to ensure compatibility with other scripts that rely on it.
    output_file_path = os.path.join(workspace, "input", "dblp_without_entities.xml")

    print("Removal in progress. Estimated completion time: ~2 minutes.")
    remove_entities(input_file_path, output_file_path)
