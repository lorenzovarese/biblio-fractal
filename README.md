# BiblioFractal 📚🌀
## Tools for parsing the DBLP database 🛠️📑

Welcome to the DBLP Data Processing Toolkit. This suite of scripts is expertly crafted to transform the rich data from the DBLP computer science bibliography into a user-friendly JSON format, prioritizing information pertinent to individual authors. Dive into a toolkit that cleans XML files, selectively extracts an author's publications, considers collaborator data upon request, and seamlessly converts the dataset into JSON.

## Contents 📂

- `entities_remover.py`: A utility to sanitize XML files by eliminating entities 🧹.
- `xml_author_extractor.py`: A specialized extractor to sift through the XML file for data associated with a specified author 🔍.
- `xml_to_json_converter.py`: A converter that transitions author-specific XML records into a structured JSON file 🔄.
- `main_dblp_script.py`: The orchestrator script, handler of the transition from the dblp.xml to final DBs.

## Getting Started 🚀

### Prerequisites

- Python 3.x 🐍
- Terminal or Command-line interface 💻

### Setup

Clone the repository on data processing:

```bash
git clone https://github.com/your-username/biblio-fractal.git
cd biblio-fractal
```

Ensure you have a copy of the `dblp.xml` in the `input` directory before proceeding.

## Prerequisites and Setup ⚙️

1. **XML Database Acquisition**: Download the `dblp.xml` from [DBLP's official repository](https://dblp.org/xml/).
2. **Decompression**: Unzip and house the `dblp.xml` in the `input` folder of this toolkit.

## Usage 📘

The `main_dblp_script.py` is the maestro of the toolkit and can be invoked with the following command:

```bash
python main_dblp_script.py "Author Name" [--collaborators]
```

### Arguments

- `author_name` (required): The distinguished name of the author for whom data is to be processed.
- `--collaborators` (optional): A switch to incorporate the entire dataset related to authors that have collaborated at least one time with the author specified in the "Author name" argument.

### Example

To engage the toolkit for author "John Doe" with collaborators:

```bash
python main_dblp_script.py "John Doe" --collaborators
```

### Scripts Breakdown

#### `entities_remover.py`

It purges the DBLP XML of entities for parsing compatibility.

**Usage:**

```bash
python entities_remover.py <input_xml_path> <output_clean_xml_path>
```

#### `xml_author_extractor.py`

This script mines the DBLP XML for records tagged to a given author.

**Usage:**

```bash
python xml_author_extractor.py <author_name> [--collaborators]
```

#### `xml_to_json_converter.py`

Convert the XML data for the author into a JSON format.

**Usage:**

```bash
python xml_to_json_converter.py <author_name> [--collaborators]
```

## Output 📦

Executing the scripts will yield:

- An XML file scrubbed clean of entities.
- An author-centric XML file detailing publications.
- A JSON with the author's bibliography.

## Contributing 🤝

Enthusiastic about contributing?

1. Fork the repository.
2. Carve out your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your enhancements (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Craft a Pull Request.
