#!/usr/bin/env python
"""A simple script that searches for a release in the MusicBrainz
database and prints out a few details about the first 5 matching release.

    $ ./releasesearch.py "the beatles" revolver
    Revolver, by The Beatles
    Released 1966-08-08 (Official)
    MusicBrainz ID: b4b04cbf-118a-3944-9545-38a0a88ff1a2
"""
from __future__ import print_function
from __future__ import unicode_literals
import musicbrainzngs
import pprint

musicbrainzngs.set_useragent(
    "python-musicbrainzngs-example",
    "0.1",
    "https://github.com/alastair/python-musicbrainzngs/",
)
def artistID(artistName):
    result = musicbrainzngs.search_artists(artist=artistName, type="group",country="US")
    artistDetails = result['artist-list']

    return artistDetails[0]['id']

def returnSongData(artistName, songName):
    songInfo = musicbrainzngs.search_recordings(query='artist:{} recording:{}'.format(artistName, songName))
    songInfo = songInfo['recording-list'][0]

    return songInfo

#print(returnSongData("Metallica", "One"))
pprint.pprint(returnSongData("Metallica", "One"))

#single = musicbrainzngs.search_recordings(query='artist:"Metallica recording:"Enter Sandman')
#print(single)
'''artist_id = artistID("Metallica")
#artist_id = "65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab"

result = musicbrainzngs.get_artist_by_id(artist_id,
              includes=["release-groups"], release_type=["single"])
for release_group in result["artist"]["release-group-list"]:
    print("{title} ({type})".format(title=release_group["title"],
                                    type=release_group["type"]))


try:
    result = musicbrainzngs.get_artist_by_id(artist_id)
except WebServiceError as exc:
    print("Something went wrong with the request: %s" % exc)
else:
    artist = result["artist"]
    print("name:\t\t%s" % artist["name"])
    print("sort name:\t%s" % artist["sort-name"])
'''