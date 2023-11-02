import argparse
import os
from lxml import etree

def count_and_print_occurrences(file_path, name):
    # Initialize lxml parser
    context = etree.iterparse(file_path, events=("end",), tag=("author", "editor"))
    
    # Counters for occurrences
    author_count = 0
    editor_count = 0
    
    for event, elem in context:
        if elem.text == name:
            if elem.tag == 'author':
                author_count += 1
                print(f"Found {name} as author in line {elem.sourceline}.")
            elif elem.tag == 'editor':
                editor_count += 1
                print(f"Found {name} as editor in line {elem.sourceline}.")
        
        # Clear the element to save memory
        elem.clear()
    
    print(f"Total occurrences of '{name}' as author: {author_count}")
    print(f"Total occurrences of '{name}' as editor: {editor_count}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Count and print occurrences of a name as author and editor in an XML file.')
    parser.add_argument('name', type=str, help='Name to search for as author and editor')
    
    args = parser.parse_args()
    
    workspace = os.getcwd()
    name = args.name
    input_file_path = os.path.join(workspace, "input", "dblp_without_entities.xml")
    
    count_and_print_occurrences(input_file_path, name)
