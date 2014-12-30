import path

def process(console, config):
    source_path = path.real(config['ASCIIDOC-DIR'])
    target_path = path.real(config['OUTPUT-DIR'])

    asciidocs = path.list(source_path, "asc")
    htmlfiles = path.list(target_path, "html")

    pairs = match(asciidocs, htmlfiles)
    regen = list(filter(html_newer, pairs))

    print(regen)

    # parallelise:
    #   generate html files where asciidoc is newer or no html file
    # consolidate
    # any work done = new index & rss file

# Match up asciidoc with corresponding HTML file
def match(ascs, htmls):
    pairs = []

    for a in ascs:
        for b in htmls:
            if fname_match(a, b):
                pairs.append([a, b])
    return pairs

def fname_match(a, b):
    return path.fname(a) == path.fname(b)

def html_newer(pair):
    asc, html = pair
    return path.mtime(asc) > path.mtime(html)
