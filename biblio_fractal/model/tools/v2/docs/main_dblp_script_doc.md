# DBLP Data Processing Script

This script facilitates the extraction and transformation of bibliographic data for a specific author from the DBLP database. It is part of a larger pipeline that cleans XML data, extracts author-specific records, and converts them into JSON format.

## Features

- Cleans the DBLP XML file by removing entities.
- Extracts records related to a specified author.
- Optionally includes data on the author's collaborators.
- Converts the extracted XML data into a JSON file.

## Prerequisites

Before running this script, ensure that Python is installed on your system. The script requires Python 3.x.

## Dependencies

This script calls other Python scripts which should be present in your project directory:
- `entities_remover.py`
- `xml_author_extractor.py`
- `xml_to_json_converter.py`

## Usage

Execute the script from the command line by providing the author's name. Optionally, you can include the author's collaborators in the output by using the `--collaborators` flag.

```bash
python process_dblp_data.py "Author Name" [--collaborators]
```

- `"Author Name"`: Replace with the actual name of the author whose data you want to process.
- `--collaborators`: Include this flag if you want to include the author's collaborators in the output.

### Example

```bash
python process_dblp_data.py "Jane Doe" --collaborators
```

## Output

The script outputs an author-specific XML file and a corresponding JSON file containing the processed data. These files will be located in the `output` directory of the current working directory.
