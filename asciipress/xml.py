"""Convert Asciidoc files to Docbook XML"""

from asciipress import command
import os

def makedir(fpath):
    if not os.path.isdir(fpath):
        try:
            os.mkdir(fpath, 0775)
        except OSError as e:
            raise OSError("Cannot create working directory: " + fpath)

def get_xml_filepath(asc_file):
    script_path = os.path.dirname(os.path.dirname(__file__))
    xml_path    = os.path.join(script_path, "xml")
    makedir(xml_path)

    fname, ext = os.path.splitext(os.path.basename(asc_file))
    return os.path.join(xml_path, fname + ".xml")

def convert(asc_file):
    xml_file = get_xml_filepath(asc_file)
    args = ["asciidoc", "--backend=docbook", "-a disable-javascript",
            "-o", xml_file, asc_file]
    try:
        command.run(args)
        return xml_file
    except Exception as e:
        print "Error converting Asciidoc to XML: " + e

# def cleanup():
    # remove xml dir