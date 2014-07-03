#!/bin/bash

DIR="$(cd "$( dirname "$0" )" && pwd)"
SITE="$DIR/../gknapp.github.io"
SOURCE="$SITE/articles"
DEST="$DIR/xml"

echo "Reading articles from: ${SOURCE/$DIR\//}"

for ASCFILE in $(ls $SOURCE/*.asc)
do
	XMLFILE=${ASCFILE/.asc/.xml}
	XMLFILE=${XMLFILE/$SOURCE/$DEST}
	echo "asciidoc --backend=docbook -a disable-javascript -o $XMLFILE $ASCFILE"
	asciidoc --backend=docbook -a disable-javascript -o $XMLFILE $ASCFILE

	HTMLFILE=${XMLFILE/.xml/.html}
	HTMLFILE=${HTMLFILE/$DEST/$SITE}
	echo "xsltproc $DIR/index.xsl $XMLFILE > $HTMLFILE"
	echo ""
	xsltproc "$DIR/index.xsl" $XMLFILE > $HTMLFILE
	echo "Published article: $HTMLFILE" 
done

