import multiprocessing as mp
import path

class Publisher:
    def __init__(self, console):
        self.console = console

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

    def convert(self, work, xslt):
        source, target = work
        self.console.echo(
            "Converting %s using %s" % (path.fname(source), xslt)
        )
        return work

    def complete(self, work):
        source, target = work
        self.console.echo("Converted " + path.fname(source))

    def error(self, ex):
        self.console.echo(str(ex))
