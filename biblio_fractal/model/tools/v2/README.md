# DBLP Data Processing Toolkit

This repository contains a suite of scripts designed to process and convert bibliographic data from the DBLP computer science bibliography into a more accessible JSON format, focusing on data specific to individual authors. It's a toolkit that cleans XML files, extracts specific author's publications, optionally includes collaborator data, and converts the result into JSON.

## Contents

- `entities_remover.py`: Script to clean XML files by removing entities.
- `xml_author_extractor.py`: Script to extract records from the XML file for a given author.
- `xml_to_json_converter.py`: Script to convert the author-specific XML records into a JSON file.
- `main_dblp_script.py`: The main script that orchestrates the data processing from XML to JSON.

## Getting Started

### Prerequisites

- Python 3.x
- Access to a terminal or command-line interface

### Setup

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/dblp-data-processing.git
cd dblp-data-processing
```

Ensure that the `input` directory contains the original `dblp.xml` file.

## Usage

The toolkit is orchestrated by the `main_dblp_script.py`, which can be executed with the following command:

```bash
python main_dblp_script.py "Author Name" [--collaborators]
```

### Arguments

- `author_name` (required): The full name of the author whose records are to be processed.
- `--collaborators` (optional): A flag to include the author's collaborators in the output.

### Example

Process data for author "John Doe" including collaborators:

```bash
python main_dblp_script.py "John Doe" --collaborators
```

### Scripts Breakdown

#### `entities_remover.py`

Removes entities from the DBLP XML file to prevent parsing errors.

**Usage:**

```bash
python entities_remover.py <input_xml_path> <output_clean_xml_path>
```

#### `xml_author_extractor.py`

Extracts records for a specified author from the DBLP XML file.

**Usage:**

```bash
python xml_author_extractor.py <author_name> [--collaborators]
```

#### `xml_to_json_converter.py`

Converts the extracted XML data for the author into a JSON file.

**Usage:**

```bash
python xml_to_json_converter.py <author_name>
```

## Output

The scripts will generate the following files in the `output` folder:

- Cleaned XML file without entities.
- XML file with publications of the specified author.
- JSON file containing the author's publications.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the project repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.
