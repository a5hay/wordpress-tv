#!/bin/bash

PLUGIN_NAME=plugin.video.wordpresstv
VERSION=0.0.1
EXCLUDE_PARAMS="--exclude=*.svn* --exclude=*.git* --exclude=*.DS_Store --exclude=*.idea* --exclude=*.pyc* --exclude=*.sh --exclude=*.md"
rm -rf "$PLUGIN_NAME-$VERSION.zip"
mkdir $PLUGIN_NAME
rsync -av --exclude $EXCLUDE_PARAMS --exclude $PLUGIN_NAME . $PLUGIN_NAME
zip -r "$PLUGIN_NAME-$VERSION.zip" $PLUGIN_NAME
rm -rf $PLUGIN_NAME/
