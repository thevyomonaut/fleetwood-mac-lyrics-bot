import lyricsgenius
import random
import tweepy

keys = {
    'CONSUMER_API_KEY': 'hHREF1LxRe46RU4L47u7VoNxc',
    'CONSUMER_API_SECRET_KEY': 'RsSrAcngIEOUbJjz1yZLeE26bnN84ifbMwB4I7WV0IonWAByKK',
    'ACCESS_TOKEN': '1564293829385400320-rnKGaFsH4DLJVYbvf90M2m0gqUPm4g',
    'ACCESS_TOKEN_SECRET': '5oJUr2nkJzRFLfICG4a3zYiAYMAplIYApJLLDp3ervAK5'
}

genius = lyricsgenius.Genius("scf3dQEaBIpERmPHRvcN2TpCRgvLl3Stb1dtz9HZD6lVinqwJNJ4AwfUYgLiVPQ5")
artist = genius.search_artist("Fleetwood Mac")

all_songs = [song for song in artist.songs]

def get_raw_lyrics():
    genius_client_access_token = "scf3dQEaBIpERmPHRvcN2TpCRgvLl3Stb1dtz9HZD6lVinqwJNJ4AwfUYgLiVPQ5"
    genius = lyricsgenius.Genius(genius_client_access_token)
    random_song_title = random.choice(all_songs)
    lyrics = genius.search_song(random_song_title, "Fleetwood Mac").lyrics
    song = random_song_title.upper()
    return lyrics, song

def get_tweet_from(lyrics):
    lines = lyrics.split('\n')
    for index in range(len(lines)):
        if lines[index] == "" or "[" in lines[index]:
            lines[index] = "XXX"
    lines = [i for i in lines if i != "XXX"]

    random_num = random.randrange(0, len(lines)-1)
    tweet = lines[random_num] + "\n" + lines[random_num+1]
    tweet = tweet.replace("\\", "")
    return tweet

def handler(event, context):
    auth = tweepy.OAuthHandler(
        keys['hHREF1LxRe46RU4L47u7VoNxc'],
        keys['RsSrAcngIEOUbJjz1yZLeE26bnN84ifbMwB4I7WV0IonWAByKK']
    )
    auth.set_access_token(
        keys['1564293829385400320-rnKGaFsH4DLJVYbvf90M2m0gqUPm4g'],
        keys['5oJUr2nkJzRFLfICG4a3zYiAYMAplIYApJLLDp3ervAK5']
    )
    api = tweepy.API(auth)
    lyrics, song = get_raw_lyrics()
    tweet = get_tweet_from(lyrics)
    status = api.update_status(tweet)

    return tweet

