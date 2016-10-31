from flask import Flask, request
import twitter
from app import app
import spotify
import wikipedia

# static url

@app.route('/tweet', methods=['GET'])
def keywordEndpoint():
    if 'keyword' in request.args:
        keyword = request.args['keyword']
        return twitter.getTweetsByKeyword(keyword)

@app.route('/wikipedia', methods=['GET'])
def articleEndpoint():
    if 'article' in request.args:
        articleName = request.args['article']
        return wikipedia.getExcerpt(articleName)

@app.route('/spotify', methods = ['GET'])
def spotifyEndpoint():
    if 'artist' in request.args:
        artistName = request.args['artist']
        return spotify.getTopTracks(artistName)
    elif 'song' in request.args:
        songName = request.args['song']
        songList =  spotify.getSong(songName)
        songs = ""
        for song in songList:
            songs += song + "\n"
        return song
