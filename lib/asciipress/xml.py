"""Convert Docbook XML to HTML via XSL"""

from os.path import dirname, realpath, join
from asciipress import command

def convert_article(xml_file, html_file):
    """Convert a Docbook XML file to HTML via an XSL template"""
    xml_dir  = realpath(dirname(dirname(xml_file)))
    xsl_path = join(xml_dir, "templates")
    xsl_file = join(xsl_path, "index.xsl")

    # check index.xsl exists
    args = ["xsltproc", "-o", html_file, xsl_file, xml_file]
    return command.run(args, "XML to HTML")

def convert_index(xml_files, html_file):
	return None
