from flask import Flask, request
import twitter
from app import app
import spotify

# static url
@app.route('/')
def index():
    return "Hello, World!"

# url parameters
@app.route('/endpoint/<input>')
def endpoint(input):
    return input

# api with endpoint
# localhost:5000/nameEndpoint?artist=kanye
@app.route('/nameEndpoint', methods=['GET'])
def nameEndpoint():
    if 'html' in request.args: # Test html here
        return "<b>This string is bold</b>"

@app.route('/tweet/hashtag', methods=['GET'])
def hashtagEndpoint():
    if 'hashtag' in request.args:
        hashtag = request.args['hashtag']
        return twitter.getTweetsByHashtag(hashtag)

@app.route('/tweet/keyword', methods=['GET'])
def keywordEndpoint():
    if 'keyword' in request.args:
        keyword = request.args['keyword']
        return twitter.getTweetsByKeyword(keyword)

@app.route('/tweet/location', methods=['GET'])
def locationEndpoint():
    if 'location' in request.args:
        locationString = request.args['location']
        return twitter.getTweetsByLocation(locationString)

@app.route('/artist', methods = ['GET'])
def artistEndpoint():
    if 'artist' in request.args:
        artistName = request.args['artist']
        return spotify.getTopTracks(artistName)
