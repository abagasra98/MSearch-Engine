# MSearch-Engine
# Interfaces

### GET /api/v1/tweet/

Get Tweets based on specific keywords

##### Request Parameters

Request parameter | Value type | Value
---|---|---
keyword | string | The keyword that you would like to search

##### Response

This method returns a JSON object containing the Tweet as well as other relevant information

### GET /api/v1/wikipedia

Grab the Wikipedia page of an artist/song

##### Request Parameters

Request parameter | Value type | Value
---|---|---
article | string | The name of the artist or song

##### Response

This method returns a String excerpt from Wikipedia:

Response | Value type | Value
---|---|---
excerpt | string | The excerpt of the Wikipedia article

### GET /api/v1/spotify

Grab a list of the top tracks by a given artist.

##### Request Parameters

Request parameter | Value type | Value
---|---|---
artist | string | The name of the artist that you would like to search

##### Response

This method returns a JSON object containing the top tracks by the artist as well as other related information.

### GET /api/v1/spotify

Grab a list of the similar tracks based on a given song name.

##### Request Parameters

Request parameter | Value type | Value
---|---|---
song | string | The name of the song that you would like to search

##### Response

This method returns a JSON object containing the tracks that are similar to the song that was searched.

# TECHNOLOGY STACK
###python
###flask (backend for web architecture)
###restful API
###HEROKU
###Git
###Google Maps/Geocoder
