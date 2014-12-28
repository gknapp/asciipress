import argparse

"""Command line argument management"""

def parse():
    parser = argparse.ArgumentParser(
        description="Convert Asciidoc files to HTML via XSL templates"
    )
    parser.add_argument("ASCIIDOC_DIR",
                        help="File path to Asciidoc files to be converted")
    parser.add_argument("OUTPUT_DIR",
                        help="Destination path to output HTML files")
    parser.add_argument("-q", "--quiet",
                        action="store_true", help="Suppress output messages")
    return parser.parse_args()