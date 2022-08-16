# Project-4-APIs
![ alt text for screen readers](https://c.tenor.com/iczjaEFdW20AAAAC/spotify-music.gif)
# Introduction
## In this project I have collected 5 playlists that I have made and have tried to compare the sentiment that they have. I have designed an API that can call the songs in the playlists and give a score per song and playlist.

# How to Use

## The basic commards are to get:

- /spotify (will give you the whole database)
- /playlists (will give you a list of all the playlists)
- /playlists/<"playlist"> (will get you everything in the playlist of your desire)
- /playlists/<"playlist">/info(will give you a list of everything without the lyrics so a user can have a look at it)
-/playlists/<"playlist">/info/<"song">/score") gets you the sentiment score of the song you chose.
- /playlists/<"playlist">/avgscore will get you the avg score of the playlists

## To post:
- Save your song as a dictionary with the following keys in this order: playlist, song, artist lyrics.
#
#
#
![ alt text for screen readers](https://pbs.twimg.com/tweet_video_thumb/FEyb6P3WUAIFn_W.jpg)

# Findings

### The sad playlist got a score of 0.09751
### A nostalgic playlist filled with 2000's hits got a score of 0.58668
### A chill playlist got -0.00092
### And a happy playlist got  0.51369

# Some things to note
### Post is not working correctly.
### Neither of the playlist had the same amount of songs. 

# This led to a lot of problems during my ETL

![ alt text for screen readers](https://c.tenor.com/7l1DWtSkxdgAAAAM/losing-it-snapped.gif)

#
#
#

###  Not every playlist had a lot of mainstream music which made it harder to find songs. 4/5 playlists ended up having missing songs due to the api not being able to find then when first building my data base. 

### Due to this, some songs were duplicated when finding lyrics.

![ alt text for screen readers](https://c.tenor.com/WjjzGvWCKi8AAAAC/thank-you.gif)