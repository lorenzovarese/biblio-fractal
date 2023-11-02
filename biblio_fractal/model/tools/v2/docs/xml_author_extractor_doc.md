# Author Collaborator Data Extractor

The Author Collaborator Data Extractor is a script designed to parse through an XML database to extract information on publications by a specified author and, optionally, their collaborators.

## Features

- Extraction of publication records from XML database.
- Collection of unique collaborator names for a given author.
- Option to include collaborator's publication records in the output.

## Prerequisites

Before running this script, ensure that you have the following:

- Python 3.x
- lxml library installed in your Python environment.

## Usage

To run the script from the command line, navigate to the script's directory and use the following command:

```bash
python extract_author_data.py <author_name> [--collaborators]
```

- `<author_name>`: Replace this with the actual name of the author whose data you want to extract.
- `--collaborators`: Include this flag if you also want to extract data for the author's collaborators.

### Example

To extract data for an author named "John Doe" without collaborators:

```bash
python extract_author_data.py "John Doe"
```

To extract data for "John Doe" including their collaborators:

```bash
python extract_author_data.py "John Doe" --collaborators
```

## Output

The script generates an XML file with the extracted data:

- If the `--collaborators` flag is not used, the output will contain only the specified author's publications.
- If the `--collaborators` flag is used, the output will include both the specified author's and their collaborators' publications.

The output files will be named using a sanitized version of the author's name, with or without the suffix `_with_collaborators`, depending on the flags provided.
