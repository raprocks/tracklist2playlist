from setuptools import setup, find_packages

with open('README.md', 'r') as fd:
    long_description = fd.read()

setup(name="tracklist2playlist",
      install_requires=[
          "spotipy",
          "requests",
          "bs4",
          "click",
      ],
      version="0.0.1",
      author="Rohit Patil",
      author_email="rahulhimesh09@gmail.com",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://www.github.com/raprocks/tracklist2playlist",
      package_dir={"tracklist2playlist": "tracklist2playlist",
                   "tracklist2playlist_sources": "tracklist2playlist_sources/"
                   },
      packages=find_packages(),
      entry_points={
          "console_scripts": [
              "t2t = tracklist2playlist.main:main", ]
          }
      )
