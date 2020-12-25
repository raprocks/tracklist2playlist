'''
module for scraping Livetracklist Page and give an Iterable
'''
from typing import Iterable
from bs4 import BeautifulSoup
import requests

class Livetracklist:
    '''
    Livetracklist.com Scraper
    '''
    def __init__(self, url: str):
        self.res = requests.get(url)
        self.soup = BeautifulSoup(self.res.content, features='html.parser')
        self.name = self.soup.find('title').text
    def tracklist(self) -> Iterable:
        '''
        livetracklist.com scraper

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
        titles = soup.findAll('span', class_="title")
        titles = [title.text for title in titles]
        artists = soup.findAll('span', class_="artist")
        artists = [artist.text for artist in artists]
        data = zip(titles, artists)
        return data
