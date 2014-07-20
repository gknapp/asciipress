"""Convert Asciidoc files to Docbook XML"""

from asciipress import command

def convert(asc_file, xml_file):
    args = ["asciidoc", "--backend=docbook", "-a disable-javascript",
            "-o", xml_file, asc_file]
    try:
        command.run(args)
        return xml_file
    except Exception as e:
        print "Error converting Asciidoc to XML: " + e
