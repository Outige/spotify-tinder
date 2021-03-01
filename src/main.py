import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

def spotipy_example():
    cid = os.environ['SPOTIFY_CID']
    secret = os.environ['SPOTIFY_SECRET']
    print(cid)
    print(secret)
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    artist_name = []
    track_name = []
    popularity = []
    track_id = []
    limit = 50
    for i in range(0, 200, limit):
        track_results = sp.search(q='year:2018', type='track', limit=limit, offset=i)
        for _, t in enumerate(track_results['tracks']['items']):
            artist_name.append(t['artists'][0]['name'])
            track_name.append(t['name'])
            track_id.append(t['id'])
            popularity.append(t['popularity'])
    
    print(artist_name)

def parse_artists_from_csv(csv_path):
    artists = []
    with open(csv_path) as fp:
        line = fp.readline()
        while line:
            artist = {}
            artist['id'] = line.split(',')[-1]
            artist['name'] = line[0:-len(artist['id'])-1]
            artists.append(artist)
            line = fp.readline()
    return artists

if __name__ == '__main__':
    artists = parse_artists_from_csv('artist_uris_reduced.csv')
    print(artists[:5])