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
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <title>(serial failure)</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="stylesheet" type="text/css" href="css/reset.css" />
    <link rel="stylesheet" type="text/css" href="css/main.css" />
    <link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Inconsolata:700|Roboto:400,700,400italic,700italic" />
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
  </body>
</html>
</xsl:template>
</xsl:stylesheet>
