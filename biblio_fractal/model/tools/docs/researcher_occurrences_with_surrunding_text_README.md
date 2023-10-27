# README for `researcher_occurrences_with_surrounding_text` Script

## Script Name
`researcher_occurrences_with_surrounding_text.py`

## Description
This script searches an XML database for occurrences of a specified author's name and writes those occurrences, along with surrounding XML text, to an output text file. The script also provides a count of the total number of occurrences of the author's name in the 'author' tags.

## Requirements

- Python 3.x
- `lxml` library for XML parsing
- `os` library for directory operations
- `argparse` library for command-line arguments parsing

## Usage

To run the script, execute the following command in the terminal:

```
python researcher_occurrences_with_surrounding_text.py <author_name>
```

Where `<author_name>` is the name of the author you want to search for.

## Functions

### `count_and_print_author_occurrences(file_path, author_name, output_file_path)`

#### Parameters

- `file_path` (str): The file path of the XML database.
- `author_name` (str): The name of the author to search for.
- `output_file_path` (str): The file path for the output text file.

#### Description

This function reads the XML database and counts the occurrences of the specified author's name in the 'author' tags. It writes these occurrences, along with the surrounding XML text, to an output text file.

## Output

The script generates a text file with the following sections:

1. A disclaimer about the tool's limitations regarding 'editor' and 'www' tags.
2. Instances where the author is found, along with 500 characters of surrounding XML text for each occurrence.
3. The total number of occurrences of the author's name in the 'author' tags.

## Disclaimer

The script includes a disclaimer about potential inaccuracies in the count due to the presence of the author's name in 'editor' or 'www' tags.

## Error Handling

If the XML file is not well-formed or if any other issue occurs, the script will not provide the desired output.

## Notes

- Place the XML database file (after removing entities using `entities_remover_script.py`) in the `input` folder to ensure proper execution.
  
By adhering to the guidelines in this README, you should be able to effectively search for occurrences of a specified author's name in an XML database and receive a text output file containing relevant details.