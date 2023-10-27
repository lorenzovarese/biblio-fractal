# BiblioFractal
Tools for parsing dblp database

# README for the Tools Folder Codebase

## Overview

This folder contains a set of Python scripts designed for interacting with academic citation data in XML format, specifically from the DBLP database. These scripts provide functionalities such as removing XML entities, generating CSV files based on authors, and counting occurrences of researchers as authors or editors.

## Prerequisites and Setup

1. **Download XML Database**: Download the `dblp.xml` file from the DBLP website at [https://dblp.org/xml/](https://dblp.org/xml/).
2. **Unzip the File**: Extract the downloaded file and place it in the `input` folder within this codebase.
3. **Run Entity Remover**: Execute the `entities_remover_script.py` to clean the XML file, producing a new XML file without entities.

### Important Note:

You must remove all XML entities from `dblp.xml` before running any of the other scripts. Failing to remove entities may result in parsing errors due to limitations in the XML parsing library and the DTD file provided by DBLP.

## General Usage Flow

1. Place the unzipped `dblp.xml` file in the `input` folder.
2. Run `python entities_remover_script.py` to generate `dblp_without_entities.xml`.
3. Once `dblp_without_entities.xml` is generated, you can use the other scripts in this tools folder.

## Script Summary and Example Usage

### `entities_remover_script.py`

- **Purpose**: Removes XML entities from an XML file.
- **Example Usage**: `python3 entities_remover_script.py`

### `get_csv_from_single_author_db.py`

- **Purpose**: Generates a CSV file containing articles, proceedings, books, etc., written by a specified author.
- **Example Usage**: `python3 get_csv_from_single_author_db.py "John Doe"`

### `researcher_occurrences_counter_fast.py`

- **Purpose**: Counts and prints occurrences of a name as an author or editor in an XML database.
- **Example Usage**: `python3 researcher_occurrences_counter_fast.py "John Doe"`

### `researcher_occurrences_with_surrounding_text.py`

- **Purpose**: Searches for occurrences of an author’s name in an XML database and outputs those occurrences along with surrounding XML text to a file.
- **Example Usage**: `python3 researcher_occurrences_with_surrounding_text.py "John Doe"`

By following the guidelines and example usages provided in this README, you should be able to manipulate and analyze academic citation data in XML format effectively.
