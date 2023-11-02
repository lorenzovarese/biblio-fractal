import argparse
import os
import subprocess

def main(author_name):
    # Define the workspace and the paths for the input and output folders.
    workspace = os.getcwd()
    input_folder = os.path.join(workspace, "input")
    output_folder = os.path.join(workspace, "output")

    # Ensure input and output directories exist to avoid file not found errors.
    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)

    # Define file paths for various steps of the script.
    input_file_path = os.path.join(input_folder, "dblp.xml")
    cleaned_input_file_path = os.path.join(input_folder, "dblp_without_entities.xml")
    author_file_name = ''.join(char for char in str(author_name) if char.isalnum())
    author_specific_xml_path = os.path.join(output_folder, f"{author_file_name}_author_db.xml")
    author_specific_json_path = os.path.join(output_folder, f"{author_file_name}_author_db.json")

    # Step 1: Check for existence of the cleaned XML file and generate it if missing.
    if not os.path.isfile(cleaned_input_file_path):
        print(f"Starting Step 1: Generating '{cleaned_input_file_path}' as it does not exist.")
        subprocess.run(['python3', 'entities_remover.py', input_file_path, cleaned_input_file_path])
        print("Step 1 Complete: 'dblp_without_entities.xml' generated.")
    else:
        print(f"'{cleaned_input_file_path}' already exists. Moving to the next step.")

    # Step 2: Generate the XML file with data specific to the author.
    print(f"Starting Step 2: Extracting data for author '{author_name}'.")
    subprocess.run(['python3', 'xml_author_extractor.py', author_name])
    print(f"Step 2 Complete: XML file for author '{author_name}' generated.")

    # Step 3: Convert the author-specific XML file to JSON format.
    print(f"Starting Step 3: Converting XML data for author '{author_name}' to JSON.")
    subprocess.run(['python3', 'xml_to_json_converter.py', author_name])
    print(f"Step 3 Complete: JSON file for author '{author_name}' is now available at '{author_specific_json_path}'.")

    print("All steps completed successfully.")

if __name__ == "__main__":
    # Setup command-line argument parsing.
    parser = argparse.ArgumentParser(description='Process DBLP data for a specific author.')
    parser.add_argument('author_name', type=str, help='Name of the author to process data for')
    args = parser.parse_args()
    
    # Execute the main function with the provided author name.
    main(args.author_name)
