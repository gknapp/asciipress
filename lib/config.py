import configparser, os, collections

def create(args):
    args.pop('--quiet', None)
    config = load('./asciipress.cfg')
    settings = update(config, args)
    return settings

def load(cfg_file):
    defaults = {
        "stylesheet": {
            "article": "article.xsl",
            "index": "index.xsl",
            "rss": "rss.xsl"
        }
    }
    config = defaults.copy()

    if os.path.isfile(cfg_file) and os.access(cfg_file, os.R_OK):
        parser = configparser.ConfigParser()
        parser.read(cfg_file)
        update(config, to_dict(parser))

    return config

def to_dict(cfg):
    data = {}
    for section in cfg.sections():
        data[section] = {}
        for k, v in cfg.items(section):
            data[section][k] = v
    return data

# non-destructive recursive update dict
# (Alex Martelli's SO solution)
def update(d, u):
    for k, v in u.items():
        if isinstance(v, collections.Mapping):
            r = update(d.get(k, {}), v)
            d[k] = r
        else:
            d[k] = u[k]
    return d