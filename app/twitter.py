import tweepy
import json, oauth2, urllib, re

CONSUMER_KEY = "ct9opqh8aJdoKnRyQNjKsssWc"
CONSUMER_SECRET = "GCno4t1PXz9ebfXRnYdCy7YEY14CdgyVlz7HHYjExM6SPkm9dr"
TOKEN_KEY = "3429309909-r12skK0hKblYjmcM1vlKcT6khPnZ0CiEJpiXiAH"
TOKEN_SECRET = "GgjaDvKuX5qWtDInkZDDtIzZaXiAZHGhy5wpdcc1LTEqP"
BASE_URL = "https://api.twitter.com/1.1/search/tweets.json?q="

auth = tweepy.OAuthHandler("ct9opqh8aJdoKnRyQNjKsssWc", "GCno4t1PXz9ebfXRnYdCy7YEY14CdgyVlz7HHYjExM6SPkm9dr")
auth.set_access_token("3429309909-r12skK0hKblYjmcM1vlKcT6khPnZ0CiEJpiXiAH", "GgjaDvKuX5qWtDInkZDDtIzZaXiAZHGhy5wpdcc1LTEqP")

api = tweepy.API(auth)
max_tweets = 10
searchText = "#AAPL"

# def getTweetsByHashtag(hashtag):
#     searchedTweets = [status._json for status in tweepy.Cursor(api.search, q=hashtag).items(max_tweets)]
#     jsonStrings = [json.dumps(json_obj) for json_obj in searchedTweets]
#     print(jsonStrings)
#     # tweetList = api.search(hashtag)
#     # tweetString = ""
#     # for tweet in tweetList:
#     #     tweetString += tweet.text + '\n'
#     # return tweetString

def getTweetsByHashtag(hashtag):
    twitterResponse = getTwitterResponse(formatHashtag(hashtag))
    jsonData = json.loads(twitterResponse)
    return str(jsonData)

def getTweetsByKeyword(keyword):
    twitterResponse = getTwitterResponse(keyword)
    jsonData = json.loads(twitterResponse)
    return str(jsonData)

def getTweetsByLocation(locationString): # Implement geocoding so don't have to pass in lat and long
    twitterResponse = getTwitterResponse(locationString, True)
    jsonData = json.loads(twitterResponse)
    return str(jsonData)

def getTwitterResponse(query, location=False):
    requestClient = getSignedRequestClient() # Make an instance variable so don't have to make it for each request
    encodedQuery = urllib.quote_plus(query)
    requestUrl = getRequestUrl(encodedQuery, location)
    resp, twitterResponse = requestClient.request(requestUrl, method = "GET", body = "", headers = None)
    return twitterResponse

def getSignedRequestClient():
    consumer = oauth2.Consumer(key = CONSUMER_KEY, secret = CONSUMER_SECRET)
    token = oauth2.Token(key = TOKEN_KEY, secret = TOKEN_SECRET)
    return oauth2.Client(consumer, token)

def getRequestUrl(endpoint, location=False):
    if (location):
        locationElements = extractLocation(endpoint)
        print(locationElements)

        return BASE_URL + locationElements[0] + "&geocode=" + locationElements[1]
    return BASE_URL + endpoint

def parseJSON(JSON):
    pass

# "https://api.twitter.com/1.1/search/tweets.json?q=%40twitterapi"
def callTwitterApi(hashtag):
    url = "https://api.twitter.com/1.1/search/tweets.json?q=" + hashtag
    twitterResponse = oauth_req(url, "TOKEN_KEY", "TOKEN_SECRET")
    jsonData = json.loads(twitterResponse)
    return str(jsonData)

def oauth_req(url, key, secret, http_method="GET", post_body= "", http_headers=None):
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    return client
    #resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    #return content

def formatHashtag(hashtag):
    if (hashtag[0] != "#"):
        return "#" + hashtag
    return hashtag

def extractLocation(locationString):
    index = re.search("\d", locationString)
    query = locationString[0:index.start()]
    location = locationString[index.start():len(locationString)].replace("+", " ")
    return (query, location)

#
# artistResponse = urllib2.urlopen("https://api.spotify.com/v1/search?q=tania%20bowra&type=artist").read()
#
#
# artistJson = json.loads(artistResponse)
# print artistResponse['artists']['items'][0]
#
#
# uid = artistJson['artists']['items'][0]['id']
# topTracks = urllib2.urlopen("https://api.spotify.com/v1/artists/" + uid + "/top-tracks?country=SE").read()
#
# topTracksJson = json.loads(topTracks)
# print topTracksJson['tracks']
# import json
# api = tweepy.API(auth)
# max_tweets=100
# query='Ipython'
# searched_tweets = [status._json for status in tweepy.Cursor(api.search,  q=query).items(max_tweets)]
# json_strings = [json.dumps(json_obj) for json_obj in searched_tweets]
