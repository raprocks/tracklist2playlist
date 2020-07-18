from spotitools import Spoti
from sources.livetracklist import Livetracklist
from sources.thousandonetracklists import Thousandonetracklists
import click
import sys
@click.command()
@click.option('-u', '--username', required=True, help="your spotify username", prompt="Please Enter Username: ")
@click.option('--url', required=True, help="live url from livetracklist.com or 1001tracklists.com", prompt="Please Enter URL: ")
def main(username, url):
    sp = Spoti(username)
    if "1001tracklists.com" in url:
        tracklist = Thousandonetracklists(url)
    elif "livetracklist.com" in url:
        tracklist = Livetracklist(url)
    else:
        print("URL does not correspond to a Tracklist. Check the URL again!")
        sys.exit()
    print("Making a playlist named", tracklist.name)
    sp.make_playlist(playlist_name=tracklist.name, description=tracklist.name)
    for title, artist in tracklist.tracklist():
        sp.search(title, artist)
    sp.add_tracks_to_playlist(sp.searched)

if __name__=="__main__":
    main()