"""AsciiPress file operations"""

import os, types

def mkdir(path):
    if not os.path.isdir(path):
        try:
            os.mkdir(path, 0775)
        except OSError as e:
            raise OSError("Cannot create working directory: " + path)

def list(dir, filter_by=None):
	contents = os.listdir(dir)

	if isinstance(filter_by, types.FunctionType):
		contents = filter(filter_by, contents)

	return contents
