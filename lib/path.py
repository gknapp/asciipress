import os, sys, glob

def exists(path):
    return os.path.exists(path)

def join(*args):
    return os.path.join(*args)

def script():
    return sys.path[0]

def cwd():
    return os.getcwd()

def real(relative):
    return os.path.realpath(join(script(), relative))

def list(dir, ext="*"):
    if os.path.exists(dir) is False:
        raise FileNotFoundError("Directory not found: " + dir)

    if ext is not "*":
        dir = "%s/*.%s" % (dir, ext)

    return glob.glob(dir)

def fname(path):
    name = os.path.basename(path)
    return os.path.splitext(name)[0]

def replace_fname(path, fname):
    dir, file = os.path.split(path)
    return os.path.join(dir, fname)

def mtime(file):
    return os.path.getmtime(file)