from config.sqlconfig import engine
import pandas as pd

## GET 
def get_everything ():      #gets the whole spotify database
    query = (f"""SELECT *FROM spotify;""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

def list_of_all():        #gives a count of all five playlists
    
    query = (f"""SELECT DISTINCT Playlist from spotify;""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

def get_playlist(playlist):   #this will return the playlist of the users choosing with everything inside the playlist
    query = (f"""SELECT * FROM spotify WHERE Playlist = '{playlist}';""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

def get_info(playlist): #will return the list of songs and artists for the playlist
    query = (f"""SELECT distinct count(*) as `Song Info`, 
    Playlist , Artist, Song from spotify 
    where Playlist = '{playlist}' group by Artist;""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

def get_lyrics(song): #will return the lyrics of the chosen song
    query = (f"""select Song,Artist,Lyrics from spotify where Song = "{song}" group by Song limit 1;""")
    df=pd.read_sql_query(query,con=engine)
    return df.to_dict(orient='records')

def get_sentiment_playlist(playlist):
    query = (f"""select Playlist, avg(Sentiment_Score) from spotify where Playlist = "{playlist}"; 
 """)
    df=pd.read_sql_query(query,con=engine)    
    return df.to_dict(orient='records')


def get_sentiment_song(song):
    query = (f"""select Song, Artist, Sentiment_Score from spotify where Song = '{song}';""")    
    df=pd.read_sql_query(query,con=engine)    
    return df.to_dict(orient='records')


## POST
def insert_song (playlist, song, artist, lyrics):
    query=(f"""INSERT INTO spotify (Playlist, Song, Artist, Lyrics) VALUES ("{playlist}", {song}", "{artist}","{lyrics}");""")
    return f"{song},{artist}, and Lyrics for it has been added to {playlist}"
