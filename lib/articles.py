import path

def process(console, config):
    source_path = path.real(config['ASCIIDOC-DIR'])
    target_path = path.real(config['OUTPUT-DIR'])

    asciidocs = path.list(source_path, "asc")
    htmlfiles = path.list(target_path, "html")

    pairs = match(asciidocs, htmlfiles)
    regen = list(filter(need_update, pairs))

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
            if filename_match(a, b):
                pairs.append([a, b])
        if a not in dict(pairs):
            html = path.replace_fname(htmls[0], path.fname(a) + ".html")
            pairs.append([a, html])

    return pairs

def filename_match(a, b):
    return path.fname(a) == path.fname(b)

'''
filter function that includes asciidocs without a corresponding HTML file
or has a more recent modify time than their HTML sibling
'''
def need_update(pair):
    asc, html = pair
    if path.exists(html) is False:
        return True
    return path.mtime(asc) > path.mtime(html)
