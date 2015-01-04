import multiprocessing as mp
import path, subprocess

class Publisher:
    def __init__(self, console):
        self.console = console
        self.converted = 0
        self.errors = 0

    def to_html(self, files, xslt):
        """Convert asciidoc files to HTML in parallel"""
        p = mp.Pool()

        for pair in files:
            p.apply_async(
                self.convert,
                args=(pair, xslt),
                callback=self.complete,
                error_callback=self.error
            )

        p.close()
        p.join()
        summary = (self.converted, self.errors)
        self.console.echo(
            "Generated %d HTML file(s) with %d error(s)" % summary
        )

    def convert(self, work, xslt):
        source, target = work
        xslt = "%s/xsl/%s" % (path.dir(source), xslt)
        exitcode = self.asc_to_html(source, target, xslt)
        work.append(exitcode)
        return work

    def complete(self, work):
        source, target, code = work
        if code == 0:
            self.converted += 1
        else:
            self.errors += 1
            self.console.echo("Error converting" + path.fname(source))

    def error(self, ex):
        self.errors += 1
        self.console.echo(str(ex))

    def asc_to_html(self, ascfile, htmlfile, xslt):
        asccmd = "asciidoc --backend=docbook -a disable-javascript -o - " + ascfile
        xslcmd = "xsltproc -o %s %s -" % (htmlfile, xslt)
        cmd = "%s | %s" % (asccmd, xslcmd)
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        proc.communicate()
        return proc.poll()
