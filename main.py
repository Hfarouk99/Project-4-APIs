from flask import Flask, request, jsonify
from pymongo import MongoClient
import random
import tools.sqltools as sql
import markdown.extensions.fenced_code
import json
import os
import json
import random


app = Flask(__name__)

@app.route("/")  
def index():
    readme_file = open("README.md", "r")
    md_template = markdown.markdown(readme_file.read(), extensions = ["fenced_code"])
    return md_template

# Get everything: SQL
@app.route("/spotify")
def all_lines ():
    return jsonify(sql.get_everything())

# Get everything FROM someone: SQL & argument
@app.route("/playlists") #gives you a list of all the playlists
def all_playlists ():
    return jsonify(sql.list_of_all())

@app.route("/playlists/<playlist>") #gets you all the playlists
def playlists(playlist):
    return jsonify(sql.get_everything())

@app.route("/playlists/<playlist>/info") #gives you a list of all the songs in the playlist
def playlist_info(playlist):
    return jsonify(sql.get_info(playlist))

@app.route("/playlists/<playlist>/info/playlists/<song>/score") #gets you the score of the song chosen
def song_score(song):
    return jsonify(sql.get_sentiment_song(song))

@app.route("/playlists/<playlist>/info/<song>/lyrics")    #gets you songs and lyrics for it
def song_lyrics(song):
    return jsonify(sql.get_lyrics(song))

@app.route("/playlists/<playlist>/avgscore") #gets you the score of the playlist
def playlist_score(playlist):
    return jsonify(sql.get_sentiment_playlist(playlist))



#POST

@app.route("/post",methods=["POST"])
def insert_song():
    playlist = request.form.get("playlist")
    song = request.form.get("song")
    artist = request.form.get("artist")
    lyrics = request.form.get("lyrics")
    return sql.insert_song(playlist,song,artist,lyrics)

if __name__ == '__main__':
    app.run(port= 9000,debug=True)

