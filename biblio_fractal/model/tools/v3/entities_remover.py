import re
import os

def remove_entities(input_file, output_file):
    """
    This function removes XML entities from a given input file and writes the clean XML to an output file.
    
    XML entities are patterns in the form of "&entity_name;", where "entity_name" is typically a placeholder for
    a special character. This function aims to remove such entities and replace them with the first character 
    of the entity name for simplicity.
    
    Parameters:
    - input_file (str): The path to the XML file containing entities.
    - output_file (str): The path where the processed XML file will be saved.
    
    The function does not return any value. Instead, it writes the processed content to the output file.
    """
    
    # Read the content of the input file
    with open(input_file, 'r', encoding='utf-8') as infile:
        xml_content = infile.read()
    
    # Define a pattern to detect XML entities
    pattern = r'&([a-zA-Z]+);'
    
    def replacer(match):
        """
        This nested function serves as the replacement function for re.sub.
        It is called for every occurrence of the pattern and returns the first
        character of the entity name or an empty string if not found.
        
        Parameters:
        - match (re.Match): The match object corresponding to the found pattern.
        
        Returns:
        - str: The first character of the matched entity name or an empty string.
        """
        entity = match.group(1)
        return entity[0] if entity else ''
    
    # Replace the XML entities with the first character of the entity name
    new_xml_content = re.sub(pattern, replacer, xml_content)
    
    # Write the processed content to the output file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(new_xml_content)

# Entry point of the script
if __name__ == '__main__':
    # Get the current working directory
    workspace = os.getcwd()
    # Define the path to the input and output files
    input_file_path = os.path.join(workspace, "input", "dblp.xml")
    output_file_path = os.path.join(workspace, "input", "dblp_without_entities.xml")

    # Invoke the function to process the file
    remove_entities(input_file_path, output_file_path)
