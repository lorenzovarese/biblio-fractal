import argparse
from lxml import etree
import os


def process_tag(context, tag, f_out):
    """
    Processes each XML tag and writes relevant entries to the output file.

    Parameters:
    - context (iterparse context): Iterator providing (event, elem) pairs.
    - tag (str): The specific XML tag to look for (e.g., 'article').
    - f_out (file object): The output file to which the entries are written.
    """
    for event, elem in context:
        if elem.tag == tag:
            f_out.write(etree.tostring(elem, pretty_print=True, encoding='ISO-8859-1', xml_declaration=False))
            f_out.write(b"\n")
            elem.clear()
            # Clean up preceding siblings from memory to keep a small footprint
            while elem.getprevious() is not None:
                del elem.getparent()[0]

def extract_data(input_file, output_file):
    """
    Extracts and writes the data of a specified author and their collaborators to an output file.

    Parameters:
    - input_file (str): Path to the input XML file.
    - output_file (str): Path to the output XML file.
    """
    # Write XML header if output file is new or empty
    if not os.path.exists(output_file) or os.path.getsize(output_file) == 0:
        with open(output_file, 'wb') as f_out:
            f_out.write(b"<?xml version='1.0' encoding='ISO-8859-1'?>\n<dblp>\n")

    tags_to_process = ['article', 'incollection', 'inproceedings']
    with open(output_file, 'ab') as f_out:
        for tag in tags_to_process:
            context = etree.iterparse(input_file, events=('end',), tag=tag, huge_tree=True)
            process_tag(context, tag, f_out)

        # Finalize the output file with a closing tag
        f_out.write(b'</dblp>\n')

if __name__ == "__main__":
    # Define paths for input and output files
    workspace = os.getcwd()
    input_file_path = os.path.join(workspace, "input", "dblp_without_entities.xml")
    output_file_path = os.path.join(workspace, "output", f"all_author_db.xml")
    extract_data(input_file_path, output_file_path)
