#!/bin/bash

if [ $# -eq 0 ]; then
	echo "Missing articles directory path"
	exit 1
fi

SOURCE=$1
DIR="$(cd "$( dirname "$0" )" && pwd)"
DEST="$DIR/xml"

cd $DIR

echo "Reading articles from: ${SOURCE/$DIR\//}"

for ASCFILE in $(ls $SOURCE/*.asc)
do
	XMLFILE=${ASCFILE/.asc/.xml}
	XMLFILE=${XMLFILE/$SOURCE/$DEST}
	# echo "asciidoc --backend=docbook -a disable-javascript -o $XMLFILE $ASCFILE"
	asciidoc --backend=docbook -a disable-javascript -o $XMLFILE $ASCFILE

	HTMLFILE=${XMLFILE/.xml/.html}
	HTMLFILE=${HTMLFILE/$DEST/$SOURCE\/..}
	# echo ""
	# echo "xsltproc $DIR/index.xsl $XMLFILE > $HTMLFILE"
	xsltproc "$DIR/index.xsl" $XMLFILE > $HTMLFILE
	echo "Published article: $HTMLFILE" 
done
