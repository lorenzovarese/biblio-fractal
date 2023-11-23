### README ###

1. Download entire db from dblp.org
2. Remove entities from the xml file with `entities_remover.py` script. The xml should be placed in the input folder of the solution
3. Run the `xml_to_json_dblp_light.py` to obtain the json file.
4. (Optional) If you want to generate mock data related to a single author, with coauthors, you can use the `filter_entire_json_db_with_only_one_author.py` script