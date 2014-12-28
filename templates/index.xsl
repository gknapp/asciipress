<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output encoding="utf-8" />

<!-- <ulink> to <a> -->
<xsl:template match="ulink">
  <a href="{@url}"><xsl:apply-templates /></a>
</xsl:template>

<!-- <simpara> to <p> -->
<xsl:template match="simpara">
  <p><xsl:apply-templates /></p>
</xsl:template>

<xsl:template match="article">
<xsl:text disable-output-escaping="yes">&lt;!doctype html></xsl:text>
<html>
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge;chrome=1" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title><xsl:value-of select="articleinfo/title" /></title>
    <link rel="stylesheet" type="text/css" href="css/reset.css" />
    <link rel="stylesheet" type="text/css" href="css/main.css" />
    <link rel="alternate"  type="application/rss+xml" href="feed.xml" title="RSS 2.0" />
  </head>
  <body>
    <header>
    <xsl:text disable-output-escaping="yes">&lt;!--[if lt IE 8]></xsl:text>
    <p>You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com">upgrade your browser</a> to improve your experience.</p>
    <xsl:text disable-output-escaping="yes">&lt;![endif]--></xsl:text>
    <h1>(serial failure)</h1>
    </header>
    <section id="content">
      <article>
        <h2><xsl:value-of select="articleinfo/title" /></h2>
        <xsl:apply-templates select="simpara" />
      </article>
    </section>
    <footer>Opinions expressed here are my own and not those of my employer.</footer>
    <script type="text/javascript">
      WebFontConfig = {
        google: { families: [ 'Love+Ya+Like+A+Sister::latin', 'Roboto:400,700italic,400italic,700:latin' ] }
      };
      (function() {
        var wf = document.createElement('script');
        wf.src = ('https:' == document.location.protocol ? 'https' : 'http') +
          '://ajax.googleapis.com/ajax/libs/webfont/1/webfont.js';
        wf.type = 'text/javascript';
        wf.async = 'true';
        var s = document.getElementsByTagName('script')[0];
        s.parentNode.insertBefore(wf, s);
      })();
    </script>
  </body>
</html>
</xsl:template>
</xsl:stylesheet>
