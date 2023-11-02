# README for `all_tags_with_specific_subtag` Script

## Script Name
`all_tags_with_specific_subtag.py`

## Description
This Python script is designed to find and list unique XML tags that contain a specified subtag. The script works by parsing an XML file and searching for the specified subtag within all tags. It then accumulates the unique parent tags that contain the subtag.

## Requirements

- Python 3.x
- `lxml` library
- `argparse` library
- `os` library

## Usage
Run the script from the terminal as follows:

```
python all_tags_with_specific_subtag.py [subtag]
```

- `subtag`: The subtag name that you are looking to find within the XML file.

## Functions

### `find_tags_containing_subtag(file_path, subtag)`

#### Parameters
- `file_path` (str): The path to the XML file that needs to be parsed.
- `subtag` (str): The name of the subtag to search for.

#### Description
The function uses `lxml.etree.iterparse` to perform iterative parsing of the XML file. It checks each XML element to see if it contains the specified subtag and accumulates these in a set to remove duplicates.

#### Return
A set of unique XML tags that contain at least one specified subtag.

## Main Execution
When executed, the script reads the `subtag` parameter from the command line using the `argparse` library. It then calls the `find_tags_containing_subtag()` function with an XML file located in the `input` directory of the workspace, and prints the unique parent tags that contain the subtag.

## Output Examples
- Example 1: 
  ```
  Unique tags that can contain at least one 'author': {'inproceedings', 'mastersthesis', 'book', 'article', 'data', 'incollection', 'www', 'phdthesis', 'proceedings'}
  ```
- Example 2: 
  ```
  Unique tags that can contain at least one 'editor': {'inproceedings', 'www', 'proceedings', 'article', 'book'}
  ```

## Note
This script performs iterative parsing and clears each element after processing to minimize memory usage. Nonetheless, make sure your system has enough resources to process large XML files if applicable.