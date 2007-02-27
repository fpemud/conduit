#!/bin/sh

APP="conduit/start_conduit.py"
if [ ! -f $APP ] ; then
    echo "ERROR: Must be run from top directory"
    exit 1
fi

#update flickrapi
wget http://beej.us/flickr/flickrapi/flickrapi.txt -O conduit/dataproviders/FlickrModule/FlickrAPI/flickrapi.py