from lxml import etree
import csv
import os
import argparse

def generate_csv_from_xml(xml_file_path, author_name, csv_file_path):
    try:
        # Initialize lxml parser and get the root
        tree = etree.parse(xml_file_path)
        root = tree.getroot()

        # Open a CSV file for writing
        with open(csv_file_path, 'w', newline='') as csvfile:
            fieldnames = ['Author Name', 'Type of the Article', 'Year', 'Article Title']
            csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            
            # Write the header
            csv_writer.writeheader()

            # Types of elements to find
            element_types = ['inproceedings', 'mastersthesis', 'book', 'article', 'data', 'incollection', 'phdthesis', 'proceedings']
            
            # Iterate over each element type
            for element_type in element_types:
                for elem in root.findall(f".//{element_type}"):
                    authors = [author.text for author in elem.findall(".//author") if author.text]
                    if author_name and author_name not in authors:
                        continue

                    # Get the 'key' attribute to determine the type of the article
                    key = elem.get('key', '')
                    article_type = key.split('/')[0] if key else 'Unknown'
                    
                    # Get the year and title
                    year = elem.find(".//year").text if elem.find(".//year") is not None else 'Unknown'
                    title = elem.find(".//title").text if elem.find(".//title") is not None else 'Unknown'
                    
                    # Write to the CSV file
                    csv_writer.writerow({'Author Name': author_name, 'Type of the Article': article_type, 'Year': year, 'Article Title': title})

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate a CSV file from XML data.')
    parser.add_argument('input_xml_db', type=str, help='Filename of the db in XML format')
    parser.add_argument('author_name', type=str, help='Name of the author in the first column of the csv')

    args = parser.parse_args()
    input_xml_db = args.input_xml_db
    input_xml_db_name, _ = os.path.splitext(input_xml_db)
    author_name = args.author_name

    workspace = os.getcwd()
    input_xml_file_path = os.path.join(workspace, "input", f"{input_xml_db}")
    output_csv_file_path = os.path.join(workspace, "output", f"{input_xml_db_name}_table.csv")
    
    generate_csv_from_xml(input_xml_file_path, author_name, output_csv_file_path)
