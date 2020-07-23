"""
Helper Class For Spotify operations
"""
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class Spoti:
    '''
    Class Spoti
    wrapper around Spotipy
    '''
    def __init__(self, username):
        self.username = username
        client_id = '8c65fad6a2604403b75d06c812786650'
        client_secret = '1aa1a70b0cd74dcc82aae173bd6fc822'
        redirect_uri = 'https://www.google.com/'
        scope = 'playlist-modify-private playlist-modify-public'
        client_credentials = SpotifyOAuth(client_id=client_id,
                                          client_secret=client_secret,
                                          redirect_uri=redirect_uri,
                                          scope=scope, username=username)
        self.spoti = spotipy.Spotify(auth_manager=client_credentials)
        self.searched = []
        self.playlist_id = ''
    @classmethod
    def query_builder(cls, title, artist):
        '''
        builds query for searchinf
        '''
        artist = artist.split("ft.")[0]
        query = '\"'+title+'\"'+' artist:'+artist
        query = query.replace(" X ", " AND ")
        query = query.replace(" x ", " AND ")
        query = query.replace(" & ", " AND ")
        return query

    def search(self, title, artist):
        '''
        searches the spotify database for song
        '''
        query = self.query_builder(title, artist)
        results = self.spoti.search(q=query, limit=1, type='track')
        if len(results['tracks']['items']) == 0:
            temp = artist.split("&")
            artist_2 = temp[-1]
            for name in temp:
                if " " in name:
                    continue
                else:
                    artist_2 = name
            query = self.query_builder(title, artist_2)
            results = self.spoti.search(q=query, limit=1, type='track')
            if len(results['tracks']['items']) == 0:
                artist_3 = artist.split("vs")[0]
                query = self.query_builder(title, artist_3)
                results = self.spoti.search(q=query, limit=1, type='track')
                if len(results['tracks']['items']) == 0:
                    print("cannot find ", title, "by", artist)
                    return ""
        print(results['tracks']['items'][0]['name'])
        uri = results['tracks']['items'][0]['id']
        self.searched.append(uri)
        return results

    def make_playlist(self, playlist_name, description=''):
        '''
        makes playlist for user
        '''
        playlist = self.spoti.user_playlist_create(self.username,
                                                   name=playlist_name,
                                                   public=False,
                                                   description=description)
        self.playlist_id = playlist['id']
        return self.playlist_id

    def add_tracks_to_playlist(self, tracks):
        '''
        adds tracks to playlist from a list of URIs
        '''
        print(self.spoti.user_playlist_add_tracks(self.username,
                                                  self.playlist_id,
                                                  tracks=tracks,
                                                  position=None))

if __name__ == "__main__":
    print("run main.py")
