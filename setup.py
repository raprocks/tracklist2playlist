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
      description="converts the tracklists to spotify playlists",
      version="0.1",
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
          },
      license="MIT",
      classifiers=[
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3 :: Only",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
          "Topic :: Multimedia :: Sound/Audio",
          "Development Status :: 5 - Production/Stable",
          "Environment :: Console",
          ]
      )
