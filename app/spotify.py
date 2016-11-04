import json
import urllib, urllib2

def getTopTracks(artistName):
    uid = getArtistID(artistName)
    topTracks = urllib2.urlopen("https://api.spotify.com/v1/artists/"+ uid + "/top-tracks?country=US").read()
    return str(topTracks)
    # topTracksJson = json.loads(topTracks)
    # trackList = topTracksJson['tracks']
    # trackString = ""
    # for track in trackList:
    #     trackString += track['name'] + "\n"
    #return trackString

    #http://localhost:5000/nameEndpoint?artist=kanye
def getSong(songName):
    songID = urllib.quote_plus(songName)
    songResponse = urllib2.urlopen("https://api.spotify.com/v1/search?q=" + songID + "&type=track").read()
    songJson = json.loads(songResponse)
    artistID = songJson['tracks']['items'][0]['artists'][0]['id']
    relatedArtistResponse = urllib2.urlopen("https://api.spotify.com/v1/artists/"+artistID+"/related-artists").read()
    relatedJson = json.loads(relatedArtistResponse)
    artistArray = relatedJson['artists']
    relatedSongList = []
    for i in xrange(5):
        artistName = artistArray[i]['name']
        relatedSongList.append(getTopTracks(artistName))
    return relatedSongList

def getArtistID(artistName):
    artistName = urllib.quote_plus(artistName)
    artistResponse = urllib2.urlopen("https://api.spotify.com/v1/search?q=" + artistName + "&type=artist").read()
    artistJson = json.loads(artistResponse)
    uid = artistJson['artists']['items'][0]['id']
    return uid

def getRecommendations(artistIDArray, trackIDArray):
    #?BQCqipoZh2c2pgYYZd4ndn7pTPdtRdPl7mHPJlZGj78nlZ1eR-wK1u7lZNAMuRE4JDMNCwAO1hayB0K-CjYUdebJ127Fv2QRn732xtVrlshW5RhlrDwb72SFLUZ7Ih63alfT9Cnd
    #urlLink = "https://api.spotify.com/v1/recommendations?seed_artists=" + artistIDArray + "&seed_tracks=" + trackIDArray +  -H "Authorization: Bearer {your access token}"
    pass
