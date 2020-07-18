from bs4 import BeautifulSoup
import requests
from typing import Iterable

class Thousandonetracklists:
    def __init__(self, url: str):
        headers = {'user-agent': 'Mozilla/5.0 (Linux; Android 10; ZenFone Max Pro M1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36'}
        self.res = requests.get(url, headers=headers)
        self.soup = BeautifulSoup(self.res.content, features="html.parser")
        self.name = self.soup.find('title').text
    def tracklist(self) -> Iterable:
        '''
        1001traclist.com scraper
        
        get tracklist in text format to be processed with song title and artist(s)
        
        Parameters
        ----------
        url : str
            url of page from which to scrape tracklist
        
        Returns
        -------
        Iterable
            yeilds tuple of length 2 and has content (song_title, artist(s))
        '''
        soup = self.soup
        tracks = soup.findAll('div', itemprop="tracks")
        artists = []
        song_titles = []
        for each in tracks:
            full_info = each.find('span', class_="trackFormat")
            full_info = full_info.text.strip()
            artists_each,song_name = tuple(full_info.split("-"))
            song_titles.append(song_name.strip().replace("\xa0", " "))
            artists.append(artists_each.strip().replace("\xa0", " "))
        data = zip(song_titles, artists)
        return data