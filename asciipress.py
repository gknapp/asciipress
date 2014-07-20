#!/usr/bin/env python

try:
    import argparse
    from asciipress import command, xml
    from os import path, listdir, chdir, errno, mkdir
except Exception as e:
    print "Failed to import necessary libraries, Python 2.7+ required"
    print e
    exit(1)

# ====================

def makedir(fpath):
    if not os.path.isdir(fpath):
        try:
            os.mkdir(fpath, 0775)
        except OSError as e:
            raise OSError("Cannot create working directory: " + fpath)

def get_xml_filepath(asc_file):
    script_path = os.path.dirname(__file__)
    xml_path    = os.path.join(script_path, "xml")
    makedir(xml_path)

    fname, ext = os.path.splitext(os.path.basename(asc_file))
    return os.path.join(xml_path, fname + ".xml")

# ====================

def run_cmd(cmd, descript):
    try:
        command.run(cmd)
        return True
    except Exception as e:
        console.echo("Error occurred converting %s: %s" % (desc, e.strerror))
    return False

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
    chdir(script_path)

    source_path = path.realpath(path.join(script_path, config["ASCIIDOC_DIR"]))
    html_path   = path.realpath(path.join(script_path, config["OUTPUT_DIR"]))

    console.echo("Asciidoc files: " + source_path)
    console.echo("HTML output:    " + html_path)

    asciidocs = list_asciidocs(source_path)

    # only process asciidocs newer than existing html file
    for fname in asciidocs:
        name, ext = path.splitext(fname)

        asc_file  = path.join(source_path, fname)
        xml_file  = get_xml_filepath(asc_file)
        html_file = path.join(html_path, name + ".html")

        try:
            xml_file = xml.convert(asc_file)
            xml_to_html(script_path, xml_file, config["xsl"], html_file)
            console.echo("Converted %s -> %s.html" % (fname, name))
        except Exception as e:
            console.echo(e)
            exit(1)

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