"""Convert Asciidoc files to Docbook XML"""

from asciipress import command

def to_xml(asc_file, xml_file):
    args = ["asciidoc", "--backend=docbook", "-a disable-javascript",
            "-o", xml_file, asc_file]
    try:
        command.run(args, "Asciidoc to XML")
        return xml_file
    except Exception as e:
        # print "Error converting Asciidoc to XML: " + e
        print e

def to_rss(asc_files, rss_file):
	return None