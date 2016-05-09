import os
import sys
import urllib
import urlparse
import xbmcaddon
import xbmcgui
import xbmcplugin
import requests
from bs4 import BeautifulSoup


# Looping through pages

def homePage():
    url='http://google.com'
    addDir('WordCamp TV', url, 4, "DefaultAddonVideo.png", None, "wordCampTv")
    addDir('Related Events', url, 4, "DefaultAddonVideo.png", None, "relatedEvents")
    addDir('How To', url, 4, "DefaultAddonVideo.png", None, "howTo")
    addDir('Search', url, 4, "DefaultAddonVideo.png", None, "search")


# Utility Methods

def addDir(name, url, mode, iconimage, fanart=None, scrape_type=None, isFolder=True, info=None):
    params = get_params()
    ok = True
    u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(
        name) + "&scrape_type=" + urllib.quote_plus(str(scrape_type)) + "&icon_image=" + urllib.quote_plus(
        str(iconimage))
    liz = xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={"Title": name})
    if info != None:
        liz.setInfo(type="Video", infoLabels=info)

    liz.setProperty('fanart_image', fanart)
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=isFolder)
    xbmcplugin.setContent(int(sys.argv[1]), 'episodes')
    return ok


def get_params():
    param = []
    paramstring = sys.argv[2]
    if len(paramstring) >= 2:
        params = sys.argv[2]
        cleanedparams = params.replace('?', '')
        if (params[len(params) - 1] == '/'):
            params = params[0:len(params) - 2]
        pairsofparams = cleanedparams.split('&')
        param = {}
        for i in range(len(pairsofparams)):
            splitparams = {}
            splitparams = pairsofparams[i].split('=')
            if (len(splitparams)) == 2:
                param[splitparams[0]] = splitparams[1]

    return param


params = get_params()
url = None
name = None
mode = None
scrape_type = None
icon_image = None

try:
    url = urllib.unquote_plus(params["url"])
except:
    pass
try:
    name = urllib.unquote_plus(params["name"])
except:
    pass
try:
    mode = int(params["mode"])
except:
    pass
try:
    scrape_type = urllib.unquote_plus(params["scrape_type"])
except:
    pass
try:
    icon_image = urllib.unquote_plus(params["icon_image"])
except:
    pass

print "Mode: " + str(mode)
print "URL: " + str(url)
print "Name: " + str(name)
print "scrape_type:" + str(scrape_type)
print "icon image:" + str(icon_image)

if mode == None or url == None or len(url) < 1:
    homePage()
# elif mode == 1:
#     LIVE_AND_UPCOMING()
# elif mode == 2:
#     FEATURED(url)
# elif mode == 3:
#     GET_ALL_SPORTS()
# elif mode == 4:
#     SCRAPE_VIDEOS(url, scrape_type)

xbmcplugin.endOfDirectory(int(sys.argv[1]))
