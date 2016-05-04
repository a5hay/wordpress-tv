# Wordpress TV plugin for Kodi
# author: @a5hay
# date: 05.04.2016
# version: 0.0.1
# license: MIT

import os
import sys
import urllib
import urlparse
import xbmcaddon
import xbmcgui
import xbmcplugin
# http://docs.python-requests.org/en/latest/
import requests
import util

# http://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup

def build_url(query):
    base_url = sys.argv[0]
    return base_url + '?' + urllib.urlencode(query)
    

# Builds the main menu
def buildMenu():
    for key, value in OPTIONS_MAIN.iteritems():
        util.addMenuItem(value[0], value[1], value[2], value[2], True)
    util.endListing()


if __name__ == '__main__':
    WEB_PAGE_BASE = 'http://wordpress.tv/'
    ADDON_ID = 'plugin.video.wordpress-tv'
    OPTIONS_MAIN = {
        'WordCamp':["Word Camps","http://wordpress.tv/category/wordcamptv/","DefaultVideo.png"],
        'RelatedEvents':["Related Events","http://wordpress.tv/category/wordpress-related-events/","DefaultVideo.png"],
        'HowTos': ["How To", "http://wordpress.tv/category/how-to/",
                          "DefaultVideo.png"]
    }
    parameters = util.parseParameters()
    if parameters is None:
        buildMenu()
    else:
        handleParameter(parameters)