# README for `researcher_occurrences_counter_fast` Script

## Script Name
`researcher_occurrences_counter_fast.py`

## Description
This script takes an XML database file and a name as inputs, and counts the occurrences of that name in the roles of both 'author' and 'editor'. It prints the count and the line numbers where the name appears in the XML file.

## Requirements

- Python 3.x
- `lxml` library for XML parsing
- `os` library for directory operations
- `argparse` library for command-line arguments parsing

## Usage

To run the script, execute the following command in the terminal:

```
python researcher_occurrences_counter_fast.py <name>
```

Where `<name>` is the name you want to search for in the roles of 'author' and 'editor'.

## Functions

### `count_and_print_occurrences(file_path, name)`

#### Parameters

- `file_path` (str): The file path of the XML database.
- `name` (str): The name to search for as both author and editor.

#### Description

This function reads the XML database and counts the occurrences of the given name as an author or an editor. It prints these counts and also indicates the line numbers in the XML file where the name appears.

## Output

The script prints the following information to the console:

1. Each line number where the name appears as an 'author' or 'editor'.
2. Total occurrences of the name as 'author'.
3. Total occurrences of the name as 'editor'.

## Error Handling

If the XML file is not well-formed or if any other issue occurs, the script will not provide the desired output.

## Notes

- Place the XML database file in the `input` folder to ensure that the script can locate it properly.
  
By following the guidelines in this README, you should be able to run the script successfully and obtain the count of occurrences of a specified name as an 'author' and 'editor' in the given XML database.