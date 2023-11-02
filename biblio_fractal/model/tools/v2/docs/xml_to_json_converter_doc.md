# XML to JSON Conversion Script

This script is designed to parse an XML file and convert its contents into a JSON file format, organizing the data into a structured and easily readable format.

## Features

- Parses XML data into a structured dictionary format.
- Handles multiple elements with the same tag (e.g., multiple `author` tags).
- Generates a JSON file from the XML input.

## Prerequisites

Ensure you have Python installed on your system. The script is compatible with Python 3.x.

## Dependencies

The script uses Python's built-in modules, so no additional installation is necessary.

## Usage

To run this script, you must provide the name of the author for which you want to convert the XML data to JSON. The script is executed from the command line as follows:

```bash
python xml_to_json_converter.py "Author Name"
```

- `"Author Name"`: Replace this with the name of the author you want to convert the XML data for.

### Example

```bash
python xml_to_json_converter.py "John Doe"
```

## Output

The output is a JSON file named after the author, containing the parsed XML data. The output file will be saved in the `output` directory within the current working directory.
