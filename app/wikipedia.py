import json
import urllib, urllib2

def getExcerpt(article):
    articleName = urllib.quote_plus(article)
    pageResponse = urllib2.urlopen("https://en.wikipedia.org/w/api.php?action=query&titles="+articleName+"&format=json").read()
    pageJson = json.loads(pageResponse)
    pageDict = pageJson['query']['pages']
    pageID = ""
    for key,page in pageDict.iteritems():
        pageID = key
        break
    firstPart = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles="
    artistResponse = urllib2.urlopen(firstPart + articleName).read()
    artistJson = json.loads(artistResponse)
    extract = artistJson['query']['pages'][pageID]['extract']
    return extract
