import json

# Path to the JSON file
file_path = 'MicheleLanza_author_db.json'

# Reading the JSON data from the file
with open(file_path, 'r') as file:
    data = json.load(file)

# Dictionary to store the results
results = {}

# Process each entry in the JSON data
for entry in data:
    year = entry["year"]
    key_part = entry["key_parts"][0]

    # Initialize the year in the results if not present
    if year not in results:
        results[year] = {}

    # Increment the count for the key_part
    results[year][key_part] = results[year].get(key_part, 0) + 1

# Sort the years and print the results
for year in sorted(results):
    counts = results[year]
    print(f"year: {year} -> ", end="")
    print(", ".join([f'"{key}"={value}' for key, value in counts.items()]))