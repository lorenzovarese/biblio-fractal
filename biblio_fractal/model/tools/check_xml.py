from lxml import etree

def check_xml(file_path):
    try:
        tree = etree.parse(file_path)
        print("XML is well-formed.")
    except etree.XMLSyntaxError as e:
        print("XML is NOT well-formed!")
        print("Error:", e)

check_xml("xmltest.xml")