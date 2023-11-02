# XML Entity Remover

The `XML Entity Remover` script is designed to cleanse XML files of their entities, simplifying them by replacing each entity with the first character of the entity name. This utility is particularly useful for processing XML files containing numerous entities that are unnecessary or can be simplified for further use.

## Getting Started

This script is ready to use with Python's standard environment. No additional installation steps are required apart from having Python itself.

### Prerequisites

Before running the script, you need to have:

- Python 3.x installed on your system.

### Installation

This script does not require any external dependencies. It solely uses the standard libraries available in Python 3.x.

### Usage

To run the script, place your XML file in an `input` directory within the same directory as the script. The script expects a file named `dblp.xml` by default but can be modified to accept any XML file.

Execute the script from the command line:

```sh
python xml_entity_remover.py
