def create(args):
    defaults = {
        "xsl": {
            "index": "index.xsl",
            "article": "article.xsl",
            "rss": "index_rss.xsl"
        }
    }
    args.pop('--quiet', None)
    defaults.update(args)
    return defaults