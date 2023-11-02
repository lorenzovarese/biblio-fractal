# README for `get_csv_from_single_author_db` Script

## Script Name
`get_csv_from_single_author_db.py`

## Description
This script takes an XML database file and an author name as inputs, and generates a CSV file containing the publications associated with the given author. The output CSV file has columns for the author's name, type of article, year, and article title.

## Requirements

- Python 3.x
- `lxml` library for XML parsing
- `csv` library for CSV writing
- `os` library for directory operations
- `argparse` library for command-line arguments parsing

## Usage

To run the script, execute the following command in the terminal:

```
python get_csv_from_single_author_db.py <input_xml_db> <author_name>
```

Where `<input_xml_db>` is the filename of the database in XML format and `<author_name>` is the name of the author for whom you want to generate the CSV file.

## Functions

### `generate_csv_from_xml(xml_file_path, author_name, csv_file_path)`

#### Parameters

- `xml_file_path` (str): The file path of the XML database.
- `author_name` (str): The name of the author to filter by.
- `csv_file_path` (str): The path where the generated CSV file will be saved.

#### Description

This function parses the input XML database to extract information on publications by the specified author. It writes this information into a CSV file, formatted according to predefined field names.

## Output

The script will output a CSV file in the `output` directory. The name of the output file will be the same as the input XML database, suffixed with `_table.csv`.

## Error Handling

If an error occurs while running the script, an error message will be printed to the console.

## Notes

- It is crucial to place the input XML database inside the `input` directory for the script to locate it.
- The script filters publications by the specified author. If an author name is not provided, the script will proceed without any filtering.

By following the guidelines in this README, you should be able to successfully generate a CSV file from an XML database, filtered by a specific author's name.