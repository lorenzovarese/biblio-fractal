# Smalltalk Research XML Parser 📜👨‍💻

This project contains Smalltalk classes and methods to parse dblp data that includes information about researchers and their publications.

## Table of Contents

1. [Files](#files)
2. [Installation](#installation)
3. [Usage](#usage)

## Files

- `researcher.st`: Contains the `Researcher` class, which models a researcher and stores publications by year.
- `publication.st`: Contains the `Publication` class, which models a publication with authors.
- `global_dict_researchers.st`: Contains the global dictionary that keeps track of all `Researcher` instances.
- `dblp_xml_parser.st`: Contains the main parser logic to populate `Researcher` and `Publication` objects from XML data.

## Installation

1. Install your Smalltalk environment (e.g., Pharo, Squeak).
2. Load the `.st` files into the Smalltalk environment.
3. Initialize the global `allResearchers` dictionary with `allResearchers := Dictionary new.`.

## Usage

1. Run the `dblp_xml_parser.st` code to start the parsing.
2. All `Researcher` and `Publication` instances will be populated based on the XML data.

Example:

```smalltalk
| xmlDoc rootNode |
"Read XML file"
xmlDoc := (XMLDOMParser onFileNamed: 'path/to/your/xml/file') parse.
rootNode := xmlDoc root.

"Execute the parser logic"
```
