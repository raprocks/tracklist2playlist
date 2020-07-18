import spotipy
from spotipy.oauth2 import SpotifyOAuth

class Spoti:
    def __init__(self, username):
        self.username = username
        client_id = '8c65fad6a2604403b75d06c812786650'
        client_secret = '1aa1a70b0cd74dcc82aae173bd6fc822'
        redirect_uri='https://www.google.com/'
        scope = 'playlist-modify-private playlist-modify-public'
        client_credentials = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope, username=username)
        self.spoti = spotipy.Spotify(auth_manager=client_credentials)
        self.searched = []

    def _query_builder(self, title, artist):
        artist = artist.split("ft.")[0]
        q = title+" artist:"+artist
        q = q.replace(" X ", " AND ")
        q = q.replace(" x ", " AND ")
        q = q.replace(" & ", " AND ")
        return q
        
    def search(self, title, artist):
        self.query = self._query_builder(title, artist)
        results = self.spoti.search(q=self.query,limit=1, type='track')
        if len(results['tracks']['items'])==0:
            artist_2 = artist.split("&")[0]
            self.query = self._query_builder(title, artist_2)
            results = self.spoti.search(q=self.query, limit=1, type='track')
            if len(results['tracks']['items'])==0:
                print("cannot find ", title ,"by", artist)
                return ""
        uri = results['tracks']['items'][0]['id']
        self.searched.append(uri)
        return results

    def make_playlist(self, playlist_name, description=''):
        playlist = self.spoti.user_playlist_create(self.username, name=playlist_name, public=False, description=description)
        self.playlist_id = playlist['id']
        return self.playlist_id

    def add_tracks_to_playlist(self,tracks):
        print(self.spoti.user_playlist_add_tracks(self.username, self.playlist_id, tracks=tracks, position=None))
        
    

if __name__=="__main__":
    print("run main.py")