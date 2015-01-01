import path

def scan(asc_dir, html_dir):
    asciidocs = path.list(path.real(asc_dir), "asc")
    htmlfiles = path.list(path.real(html_dir), "html")
    pairs = match(asciidocs, htmlfiles)
    return list(filter(need_update, pairs))

def match(ascs, htmls):
    """Match up asciidoc with corresponding HTML file"""
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

def need_update(pair):
    """
    filter function that includes asciidocs without a corresponding HTML file
    or has a more recent modify time than its HTML sibling
    """
    asc, html = pair
    if path.exists(html) is False:
        return True
    return path.mtime(asc) > path.mtime(html)
