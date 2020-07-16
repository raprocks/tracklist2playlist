from bs4 import BeautifulSoup
import requests
from typing import Iterable

def livetracklist(url : str) -> Iterable:
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
    res = requests.get(url)
    soup = BeautifulSoup(res.content, features="html.parser")
    titles = soup.findAll('span', class_="title")
    titles = [title.text for title in titles]
    artists = soup.findAll('span', class_="artist")
    artists = [artist.text for artist in artists]
    data = zip(titles, artists)
    return data
