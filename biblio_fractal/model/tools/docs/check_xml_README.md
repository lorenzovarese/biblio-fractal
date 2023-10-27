# README for `check_xml` Script

## Script Name
`check_xml.py`

## Description
This Python script is designed to verify whether an XML file is well-formed. The script attempts to parse the XML file and will output a success message if the XML is well-formed. Otherwise, it will display an error message indicating that the XML is not well-formed and also output the specific error encountered.

## Requirements

- Python 3.x
- `lxml` library

## Usage
Run the script from the terminal as follows:

```
python check_xml.py
```

Note: The XML file to be checked, `xmltest.xml`, should be present in the same directory as the script, or you will have to modify the script to point to the correct location of the XML file.

## Functions

### `check_xml(file_path)`

#### Parameters
- `file_path` (str): The path to the XML file that needs to be checked for well-formedness.

#### Description
The function uses the `etree.parse()` method from the `lxml` library to try to parse the XML file. If parsing is successful, it means the XML is well-formed. Otherwise, an `etree.XMLSyntaxError` exception is caught, and the script outputs an error message.

#### Return
None. The function prints out a message indicating whether the XML file is well-formed or not.

## Output Examples
- If the XML is well-formed:
  ```
  XML is well-formed.
  ```
- If the XML is not well-formed:
  ```
  XML is NOT well-formed!
  Error: [Specific error message]
  ```

## Note
Ensure that the XML file you wish to check is either located in the same directory as the script or specify the complete path to the XML file within the script.