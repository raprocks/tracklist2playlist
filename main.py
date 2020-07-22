'''
Module for Command Line Implementation and usage
'''

import sys
import click
from spotitools import Spoti
from sources.livetracklist import Livetracklist
from sources.thousandonetracklists import Thousandonetracklists


@click.command()
@click.option('-u', '--username', required=True,
              help="your spotify username",
              prompt="Please Enter Username: ")
@click.option('--url', required=True,
              help="live url from livetracklist.com or 1001tracklists.com",
              prompt="Please Enter URL: ")
def main(username, url):
    '''
    main click Function
    '''
    spoti = Spoti(username)
    if "1001tracklists.com/tracklist" in url:
        tracklist = Thousandonetracklists(url)
    elif "livetracklist.com" in url:
        tracklist = Livetracklist(url)
    else:
        print("URL does not correspond to a Tracklist. Check the URL again!")
        sys.exit()
    print("Making a playlist named", tracklist.name)
    spoti.make_playlist(playlist_name=tracklist.name,
                        description=tracklist.name)
    for title, artist in tracklist.tracklist():
        spoti.search(title, artist)
    spoti.add_tracks_to_playlist(spoti.searched)


if __name__ == "__main__":
    main()
