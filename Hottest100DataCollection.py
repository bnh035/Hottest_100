#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Hottest 100 data collection

File name: Hottest100DataCollection.py
Author: Brice Hilliard
Date created: 23/01/2018
Date last modified: 24/01/2018
Python version: 3.6.1

This file collects data from the JJJ Hottest 100 in 2 parts, these are:
* Collect ranking list from each of the years that it has been running in it's current form^
* Collect data from Genius.com regarding release dates and some other data^^

^ It is taken that the starting years is 1993 as that is what is available from:
    http://www.abc.net.au/triplej/hottest100/archive
^^ At the moment the current scope only includes release date, but could possibly expand to include more data

Todo:
* Come up with an algorithm to search through Genius.com. This would include:
    > Release date lies inside the HTML snippet:
          <div class="metadata_unit metadata_unit--table_row">
            <span class="metadata_unit-label">Release Date</span>
            <span class="metadata_unit-info metadata_unit-info--text_only">January 10, 1989</span>
          </div>
    > Potentially look into BeautifulSoup, this has already been imported, but not used
    > Possibly need to search through plain text to match with the current data. Could then also store this as a dict
      that could be referred to later. The match would have to include special characters from umlaut.+
* Combine the data from Genius.com with the current dataframe containing the Hottest 100 data
* Standardise camel/snake case
* Create a function that reads from the files containing the relevant data. Should speed things up
*
"""

import requests
import re
from bs4 import BeautifulSoup
from string import ascii_lowercase
import pandas as pd
import csv
import pprint

current_year = 2016  #: This is the last year that is archived as of 24/01/2018
first_year = 1993  #: First of lists archived
columns = ['Year', 'Position', 'Artist', 'Song']
songDF = pd.DataFrame(columns=columns)
linkList = []
nameList = []


def find_between(s, first, last, searchString):
    """Find in the string 's', the substring between the 2 substrings 'first' and 'last'

    :param s: The main string that the search will be conducted through
    :param first: The initial substring that encloses the returned substring
    :param last: The last substring that encloses the returned substring
    :param searchString: A string that can be searched in the found string. If not used enter ""
    :return: A list of all substringa that are enclosed by the first and last substrings
    """
    try:
        linkText = re.findall('{}.*?{}'.format(first, last), s, re.DOTALL)
        linkText = [t[len(first):-len(last)] for t in linkText]
        if searchString != "":
            artistLinks = [p for p in linkText if searchString in p]
            return artistLinks
        else:
            return linkText
    except ValueError:
        return ""


def scrape_jjj():
    for year in range(first_year, current_year+1):
        html_request = requests.get('http://www.abc.net.au/triplej/hottest100/archive/archive.htm?year={}&alltime=0'
                                    .format(year))  #: Gathers the content from the JJJ website
        html_request.encoding = 'utf-8'  #: Sets encoding as default is unicode
        html_content = html_request.text

        start_string = '<ol>'  #: The list is the stored between the HTML tags <ol> and <\ol>
        end_string = '</ol>'

        list_data = find_between(html_content, start_string, end_string, "")
        i = 1
        for line in list_data[0].splitlines():
            InData = line[5:-5]  #: Removes the HTML tags that surround the data
            if len(line.strip()) != 0:
                SongInfo = InData.split(' - ', 1)  #: Splits up the data at the first ' - '
                if len(SongInfo) != 2:
                    print("File Error: {}".format(SongInfo))  #: Throws an error if it creates more than 2 strings
                SongInfo.insert(0, i)
                SongInfo.insert(0, year)
                songDF.loc[len(songDF)] = SongInfo
                i += 1
    return songDF

for c in ascii_lowercase:
    html_request = requests.get("https://genius.com/artists-index/{}".format(c))
    html_request.encoding = 'utf-8'
    html_content = html_request.text

    start_string = '<a '
    end_string = '</a>'
    searchPhrase = 'artist'

    links = find_between(html_content, start_string, end_string, searchPhrase)

    for i in links:
        i = i[6:]
        artistLink = i.split('">')
        nameList.append(artistLink[1])
        linkList.append(artistLink[0])

songLinkDict = dict(zip(nameList, linkList))

hottest100DF = scrape_jjj()

hotArtistList = hottest100DF['Artist'].tolist()
hottest100DF['Link'] = ""

hotLinkList = []
errorList = []
for entry in hotArtistList:
    try:
        hotLinkList.append(songLinkDict[entry])
    except:
        errorList.append(entry)

webCheckList = [name.replace(' ', '-').lower() for name in errorList]
webCheckList = list(set(webCheckList))

def writeToFile():
    print('Writing to file...')

    with open('linkDict.csv', 'w', encoding='utf-8') as linkDictFile:
        w = csv.DictWriter(linkDictFile, songLinkDict.keys())
        w.writeheader()
        w.writerow(songLinkDict)
    linkDictFile.close()

    hottest100DF.to_csv('hot100DF.csv', encoding='utf-8', index=False)

    with open('webCheck.csv', 'w', encoding='utf-8') as webCheckFile:
        wr = csv.writer(webCheckFile)
        wr.writerow(webCheckList)
    webCheckFile.close()

    print('Writing completed')

def checkExists(webString, webSuffix):
    request = requests.get(webString + webSuffix)

    if request.status_code == 200:
        return True
    else:
        return False

counter1 = 1
geniusWebName = 'https://genius.com/artists/'

for bandName in webCheckList:
    print("{}/{}".format(counter1, len(webCheckList)))
    counter1 += 1
    if checkExists(geniusWebName, bandName):
        hotLinkList.append(geniusWebName + bandName)
        print(bandName)

with open('linkList.csv', 'w', encoding='utf-8') as linkListFile:
    wr = csv.writer(linkListFile)
    wr.writerow(hotLinkList)
    linkListFile.close()
linkListFile.close()

print("After check: {}".format(len(hotLinkList)))
print("After check: {}".format(len(errorList)))
