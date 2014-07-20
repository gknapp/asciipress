from subprocess import check_call

def not_found(ex):
    return ex.errno == errno.ENOENT

def run(cmd, desc):
    try:
        check_call(cmd)
    except OSError as e:
        if not_found(e):
            raise EnvironmentError("command not found '%s'" % cmd[0])
        else:
        	raise EnvironmentError("error occured converting " + desc)