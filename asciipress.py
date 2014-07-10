#!/usr/bin/env python

try:
    import argparse
    from asciipress import command
    from os import path, listdir, chdir, errno, mkdir
except Exception:
    print "Failed to import necessary libraries, Python 2.7+ required"
    exit(1)

def run_cmd(cmd, descript):
    try:
        command.run(cmd)
        return True
    except Exception as e:
        console.echo("Error occurred converting %s: %s" % (desc, e.strerror))
    return False

def asc_to_xml(asc_file, xml_file):
    """Convert an Asciidoc file to a Docbook XML file"""
    args = ["asciidoc", "--backend=docbook", "-a disable-javascript",
            "-o", xml_file, asc_file]
    return run_cmd(args, "Asciidoc to XML")

def xml_to_html(script_path, xml_file, xsl, html_file):
    """Convert a Docbook XML file to HTML via an XSL template"""
    # loop over xsl and produce index, article
    xslt_file = path.join(script_path, xsl["index"])
    args = ["xsltproc", "-o", html_file, xslt_file, xml_file]
    return run_cmd(args, "XML to HTML")

def only_asciidoc(fname):
    name, ext = path.splitext(fname)
    return ext == '.asc'

def list_asciidocs(path):
    return filter(only_asciidoc, listdir(path))

def main(console, config):
    script_path = path.dirname(path.realpath(__file__))
    source_path = path.realpath(path.join(script_path, config["ASCIIDOC_DIR"]))
    html_path   = path.realpath(path.join(script_path, config["OUTPUT_DIR"]))
    xml_path    = path.join(script_path, "xml")

    if not path.isdir(xml_path):
        try:
            mkdir(xml_path, 0775)
        except OSError as e:
            console.echo("Cannot create working directory: " + xml_path)
            exit(1)

    console.echo("Asciidoc files: " + source_path)
    console.echo("HTML output:    " + html_path)
    chdir(script_path)

    asciidocs = list_asciidocs(source_path)

    # only process asciidocs newer than existing html file
    for fname in asciidocs:
        name, ext = path.splitext(fname)

        asc_file  = path.join(source_path, fname)
        xml_file  = path.join(xml_path, name + ".xml")
        html_file = path.join(html_path, name + ".html")

        if asc_to_xml(asc_file, xml_file):
            if xml_to_html(script_path, xml_file, config["xsl"], html_file):
                console.echo("Converted %s -> %s.html" % (fname, name))

def configure_args():
    parser = argparse.ArgumentParser(
        description='Convert Asciidoc files to HTML via XSL templates'
    )
    parser.add_argument("ASCIIDOC_DIR",
                        help="File path to Asciidoc files to be converted")
    parser.add_argument("OUTPUT_DIR",
                        help="Destination path to output HTML files")
    parser.add_argument("-q", "--quiet",
                        action="store_true", help="Suppress output messages")
    return parser.parse_args()

class Console:
    """Print messages sent to console"""
    def echo(self, message):
        print message

class SilentConsole:
    """Suppress messages sent to console"""
    def echo(self, message):
        return True

def load_config(args):
    """Attempt to load config, otherwise return defaults"""
    defaults = {
        "xsl": {
            "index": "index.xsl",
            "article": "article.xsl",
            "rss": "index_rss.xsl"
        }
    }
    return dict(defaults.items() + args.__dict__.items())

if __name__ == '__main__':
    args = configure_args()
    console = SilentConsole() if args.quiet else Console()
    config = load_config(args)
    main(console, config)