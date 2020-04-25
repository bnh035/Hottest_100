#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Hottest 100 data collection

This file collects data from the JJJ Hottest 100 in 2 parts, these are:
* Collect ranking list from each of the years that it has been running in it's current form^
* Collect data from Genius.com regarding release dates and some other data^^
^ It is taken that the starting years is 1993 as that is what is available from:
    http://www.abc.net.au/triplej/hottest100/archive
^^ At the moment the current scope only includes release date, but could possibly expand to include more data
"""

import requests
import re
from string import ascii_lowercase
import pandas as pd
import csv
# from bs4 import BeautifulSoup
# import pprint

__author__ = "Brice Hilliard"
__copyright__ = ""
__credits__ = ""

__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Brice Hilliard"
__email__ = "bricehilliard035@gmail.com"
__status__ = "Production"

current_year = 2016  #: This is the last year that is archived as of 24/01/2018
first_year = 1993  #: First of lists archived
columns = ['Year', 'Position', 'Artist', 'Song']
songDF = pd.DataFrame(columns=columns)
link_list = []
name_list = []

# TODO: * Come up with an algorithm to search through Genius.com.
"""
    > Release date lies inside the HTML snippet:
        <div class="metadata_unit metadata_unit--table_row">
            <span class="metadata_unit-label">Release Date</span>
            <span class="metadata_unit-info metadata_unit-info--text_only">January 10, 1989</span>
        </div>
"""
# TODO: Potentially look into BeautifulSoup, this has already been imported, but not used
# TODO: Possibly need to search through plain text to match with the current data. Could then also store this as a dict
# that could be referred to later. The match would have to include special characters from umlaut.
# TODO: Combine the data from Genius.com with the current dataframe containing the Hottest 100 data
# TODO: Standardise camel/snake case
# TODO: Create a function that reads from the files containing the relevant data. Should speed things up


def find_between(s, first, last, search_string):
    """Find in the string 's', the substring between the 2 substrings 'first' and 'last'

    :param s: The main string that the search will be conducted through
    :param first: The initial substring that encloses the returned substring
    :param last: The last substring that encloses the returned substring
    :param search_string: A string that can be searched in the found string. If not used enter ""
    :return: A list of all substringa that are enclosed by the first and last substrings
    """
    try:
        link_text = re.findall('{}.*?{}'.format(first, last), s, re.DOTALL)
        link_text = [t[len(first):-len(last)] for t in link_text]
        if search_string != "":
            artist_links = [p for p in link_text if search_string in p]
            return artist_links
        else:
            return link_text
    except ValueError:
        return ""


def scrape_jjj():
    for year in range(first_year, current_year+1):
        #: Gathers the content from the JJJ website
        # html_request = requests.get('http://www.abc.net.au/triplej/hottest100/archive/archive.htm?year={}&alltime=0'
        #                             .format(year))
        html_request = requests.get('https://www.abc.net.au/triplej/hottest100/archive/search/?year='.format(year))
        #: Sets encoding as default is unicode
        html_request.encoding = 'utf-8'
        html_content = html_req.text
        #: The list is the stored between the HTML tags <ol> and <\ol>
        start_string = '<ol>'
        end_string = '</ol>'
        list_data = find_between(html_content, start_string, end_string, "")
        print(list_data)
        i = 1
        for line in list_data[0].splitlines():
            #: Removes the HTML tags that surround the data
            in_data = line[5:-5]
            if len(line.strip()) != 0:
                #: Splits up the data at the first ' - '
                song_info = in_data.split(' - ', 1)
                if len(song_info) != 2:
                    #: Throws an error if it creates more than 2 strings
                    print("File Error: {}".format(song_info))
                song_info.insert(0, i)
                song_info.insert(0, year)
                songDF.loc[len(songDF)] = song_info
                i += 1
    return songDF

for c in ascii_lowercase:
    html_req = requests.get("https://genius.com/artists-index/{}".format(c))
    html_req.encoding = 'utf-8'
    html_cont = html_req.text
    start_str = '<a '
    end_str = '</a>'
    search_phrase = 'artist'
    links = find_between(html_cont, start_str, end_str, search_phrase)
    for i in links:
        i = i[6:]
        artistLink = i.split('">')
        name_list.append(artistLink[1])
        link_list.append(artistLink[0])

song_link_dict = dict(zip(name_list, link_list))
hottest_100_DF = scrape_jjj()
hot_artist_list = hottest_100_DF['Artist'].tolist()
hottest_100_DF['Link'] = ""
hot_link_list = []
error_list = []

for entry in hot_artist_list:
    try:
        hot_link_list.append(song_link_dict[entry])
    except:
        error_list.append(entry)

web_check_list = [name.replace(' ', '-').lower() for name in error_list]
web_check_list = list(set(web_check_list))


def write_to_file():
    print('Writing to file...')
    with open('linkDict.csv', 'w', encoding='utf-8') as link_dict_file:
        w = csv.DictWriter(link_dict_file, song_link_dict.keys())
        w.writeheader()
        w.writerow(song_link_dict)
        link_dict_file.close()
    hottest_100_DF.to_csv('hot100DF.csv', encoding='utf-8', index=False)
    with open('webCheck.csv', 'w', encoding='utf-8') as web_check_file:
        wr = csv.writer(web_check_file)
        wr.writerow(web_check_list)
        web_check_file.close()
    print('Writing completed')


def check_exists(web_string, web_suffix):
    request = requests.get(web_string + web_suffix)
    if request.status_code == 200:
        return True
    else:
        return False

counter1 = 1
genius_web_name = 'https://genius.com/artists/'

for band_name in web_check_list:
    print("{}/{}".format(counter1, len(web_check_list)))
    counter1 += 1
    if check_exists(genius_web_name, band_name):
        hot_link_list.append(genius_web_name + band_name)
        print(band_name)

with open('linkList.csv', 'w', encoding='utf-8') as link_list_file:
    wr = csv.writer(link_list_file)
    wr.writerow(hot_link_list)
    link_list_file.close()
link_list_file.close()

print("After check: {}".format(len(hot_link_list)))
print("After check: {}".format(len(error_list)))
