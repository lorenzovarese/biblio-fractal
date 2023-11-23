import ijson
import json

def collect_and_filter_publications(input_file, output_file):
    authors_set = set()

    # First pass: collect authors
    with open(input_file, 'rb') as file:
        for publication in ijson.items(file, 'item'):
            if 'Author Name' in publication.get('authors', []):
                authors_set.update(publication['authors'])

    # Second pass: filter publications and write incrementally
    with open(input_file, 'rb') as file, open(output_file, 'w') as outfile:
        outfile.write('[')
        first_item = True
        for publication in ijson.items(file, 'item'):
            if any(author in authors_set for author in publication.get('authors', [])):
                if not first_item:
                    outfile.write(',')
                json.dump(publication, outfile)
                first_item = False
        outfile.write(']')

    return authors_set

# Example usage
input_file = 'path/light_dblp_db.json'  # Replace with your JSON file path
output_file = 'path/result.json'
authors_set = collect_and_filter_publications(input_file, output_file)
print("Authors associated:", authors_set)
