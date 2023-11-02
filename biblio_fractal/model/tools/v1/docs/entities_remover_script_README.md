# README for `entities_remover_script` Script

## Script Name
`entities_remover_script.py`

## Description
This script is designed to remove HTML entities from an XML file. Specifically, it reads an XML file, applies a regular expression to identify and replace entities, and then writes the transformed XML content to a new file.

## Requirements

- Python 3.x
- `re` library for regular expression
- `os` library for file and directory manipulation

## Usage
To run the script, execute the following command in the terminal:

```
python entities_remover_script.py
```

## Pre-requisites

**Important**: Before running the script, ensure that you have the `dblp.xml` file placed inside the `input` folder. This file must be downloaded from [DBLP](https://dblp.org/xml/). After downloading, unzip it and move it into the `input` folder. The script heavily depends on this pre-existing setup.

## Functions

### `remove_entities(input_file, output_file)`

#### Parameters
- `input_file` (str): The path to the input XML file containing entities.
- `output_file` (str): The path where the output XML file without entities will be saved.

#### Description
This function reads the content of the input XML file, utilizes regular expressions to identify and remove entities, and writes the new content to an output file.

## Output
The transformed XML will be saved to a new file located in the `input` folder and named `dblp_without_entities.xml`.

## Note
- The estimated time for the entity removal is approximately 2 minutes. The terminal will display a message indicating the progress.
- The output file is intentionally placed inside the `input` folder to ensure compatibility with other scripts that may rely on it.
  
## Warning
Make sure your system has sufficient resources to handle the entity removal from a potentially large XML file. The script reads the entire file into memory for processing.