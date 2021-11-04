#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Hottest 100 data collection

This file collects data from the JJJ Hottest 100 in 2 parts, these are:
* Collect ranking list from each of the years that it has been running in it"s current form^
* Collect data from Genius.com regarding release dates and some other data^^
^ It is taken that the starting years is 1993 as that is what is available from:
    http://www.abc.net.au/triplej/hottest100/archive
^^ At the moment the current scope only includes release date, but could possibly expand to include more data
# TODO: * Come up with an algorithm to search through Genius.com.

    > Release date lies inside the HTML snippet:
        <div class="metadata_unit metadata_unit--table_row">
            <span class="metadata_unit-label">Release Date</span>
            <span class="metadata_unit-info metadata_unit-info--text_only">January 10, 1989</span>
        </div>

TODO: Potentially look into BeautifulSoup, this has already been imported, but not used
TODO: Possibly need to search through plain text to match with the current data. Could then also store this as a dict
      that could be referred to later. The match would have to include special characters from umlaut.
TODO: Combine the data from Genius.com with the current dataframe containing the Hottest 100 data
TODO: Standardise camel/snake case
TODO: Create a function that reads from the files containing the relevant data. Should speed things up

26/10/21 Update
===============
Update format of program:

- wrap in a main function
    - Check data
        + Use current date to check and download data
    - Create functions for separate processes
    - Repair data
        + Download/scrape missing data
    - Process data
    - Plot data
    - Analyse data

"""

from bs4 import BeautifulSoup
from datetime import datetime
from googlesearch import search
from googleapiclient.discovery import build
from string import ascii_lowercase

import ast
import calendar
import csv
import json
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import pprint
import requests
import re
import time

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
columns = ["Year", "Position", "Artist", "Song"]
songDF = pd.DataFrame(columns=columns)
link_list = []
name_list = []

# Setup pretty printer
pp = pprint.PrettyPrinter(indent=4)

# =========== Useful Functions ==================
# Move to a utils file

def find_between(s, first, last, search_string):
    """Find in the string "s", the substring between the 2 substrings "first" and "last"

    :param s: The main string that the search will be conducted through
    :param first: The initial substring that encloses the returned substring
    :param last: The last substring that encloses the returned substring
    :param search_string: A string that can be searched in the found string. If not used enter ""
    :return: A list of all substringa that are enclosed by the first and last substrings
    """
    try:
        link_text = re.findall("{}.*?{}".format(first, last), s, re.DOTALL)
        link_text = [t[len(first):-len(last)] for t in link_text]
        if search_string != "":
            artist_links = [p for p in link_text if search_string in p]
            return artist_links
        else:
            return link_text
    except ValueError:
        return ""


def replace_from_list_strings(stringToReplace, listOfChars, replace_char):
    for i in listOfChars:
        stringToReplace = stringToReplace.replace(i, replace_char)
    return(stringToReplace)


# =========== Data Cleaning Functions ===========
# Move to a data preprocessing file


# =========== Scraping Functions ================
# Move to a scraping file
def scrape_jjj():
    """
    Scrapes data from the JJJ website and returns a list of dictionaries of track data
    """
    out_text = ""
    base_url = "https://www.abc.net.au/triplej/hottest100/archive/search/?year="
    html_request = requests.get(base_url + str(2018))
    
    #: Sets encoding as default is unicode
    html_request.encoding = "utf-8"
    html_content = html_request.text

    start_string = "<script>"
    end_string = "</script>"
    list_data = find_between(html_content, start_string, end_string, "")
    
    # remove extraneous characters
    for i in list_data:
        replace_from_list_strings(i, ["\r", "\n"], ")
        out_text+=i+"\n"
    
    # Split string at ] to get track data. Album data can be accessed by using the second element in the split output.
    out_text = out_text.replace("var tracks = ", ").replace("window.h100site = {path: "/triplej/hottest100/archive" }", ")
    tracks = json.loads(out_text.split("var albums = [")[0])
    
    #pp.pprint(tracks)
    return pd.DataFrame(tracks)


def check_url(test_url):
    # Request page
    page = requests.get(test_url)

    # Error handling for the page
    if page.status_code == 200:
        valid = True
    else:
        valid = False
    return valid


def prep_url(artist_name, artist_song):
    # Create the genius URL
    base_url = "https://genius.com/"
    end_url = "-lyrics"
    mid_url = artist_name+"-"+artist_song

    # Replace special chars in data
    mid_url = mid_url.replace(" ", "-")
    replace_list = ["/", ".", "{", "}", ",", ".", "!", "?", "'", "(", ")"]
    mid_url = replace_from_list_strings(mid_url, replace_list, "")
    mid_url = mid_url.replace("&", "and")

    # Construct the full
    genius_url = base_url+mid_url+end_url
    genius_url = genius_url.replace("--", "-")
    return genius_url


def add_song_url(name, song):
    # Prepare and check a url based on artist name and song
    url = prep_url(name, song)
    if check_url(url):
        out_url = "XX-"
    else:
        out_url = url
    return out_url


def add_missing_col(check_str):
    # Add a column that checks if the url contains "XX-"
    search_str = "XX-"
    if search_str in check_str:
        return True
    else:
        return False


def google_search(search_term, api_key, cse_id, **kwargs):
    # Currently limited to 100 queries a day
    # Figure a more efficient way of searching google
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    resJSON = res["items"][0]
    url = resJSON["link"]
    return url


def search_for_links(name, song):
    # Enter google API and CSE IDs
    API_KEY = "YY"
    CSE_ID = "XX"

    # Create the search term
    my_query = f"{name} {song} genius"

    # Looking for this term in the search result to confirm website
    genius_head = "https://genius.com/"

    # This is the default link for when the search is unsuccessful
    link = "XX-"

    # Search Google
    my_url = google_search(my_query, API_KEY, CSE_ID)

    # Check if the first result is from Genius.com
    if genius_head in my_url:
        link = my_url
    
    # Create a dictionary to be added to the link cache file
    temp_dict = {
    "artist": name,
    "track": song,
    "song_url": link
    }
    print([name, song, link])

    # Add the dictionary to the end of the cache file (csv)
    if os.path.isfile("link_cache.csv"):
        cache_df = pd.read_csv("data/link_cache.csv", index_col=0)
    else:
        cache_df = pd.DataFrame()
    cache_df = cache_df.append(temp_dict, ignore_index=True)

    # Resave the link cache file
    cache_df.to_csv("data/link_cache.csv")
    return link


def update_df(name, song, url, update_df):
    # Update the song urls for rows with the matching artist and song title
    if (name in update_df["artist"].unique()) and (song in update_df["track"].unique()):
        try:
            # Not sure why this is causing an error. Need to investigate further
            return update_df[(update_df["artist"]==name)&(update_df["track"]==song)]["song_url"].unique()[0]
        except:
            return "XX-"
    else:
        return url


# ======== Main Function ============

def main(search_google):
    # Start the timer
    start = datetime.now()
    print(f"start time: {start}")
    
    # Check if cache exists and load from it if it does.
    if os.path.isfile("data/cache.csv"):
        print("reading from cache...")
        hottest_100_DF = pd.read_csv("cache.csv", index_col=0)
    else:
        print("scraping...")
        hottest_100_DF = scrape_jjj()
        hottest_100_DF["song_url"] = hottest_100_DF.apply(lambda x: add_song_url(x.artist, x.track), axis=1)
        hottest_100_DF.to_csv("data/cache.csv")    
    
    # Create a DF of links that do not work or are missing
    # Detect when this needs to be done
    print("collecting missing urls...")
    hottest_100_DF["val_link"] = hottest_100_DF.apply(lambda x: add_missing_col(x.song_url), axis=1)
    missing_df = hottest_100_DF[hottest_100_DF["val_link"]]
    
    print("fixing missing links...") 
    # Do this by searching google. 
    # This is limited to 100 queries per day, set search_google to true when using this functionality
    if search_google:
        for start_row in range(0, missing_df.shape[0], 10):
            end_row  = min(start_row + 10, missing_df.shape[0])
            curr_df = missing_df.iloc[start_row:end_row, :]
            curr_df["song_url"] = curr_df.apply(lambda x: search_for_links(x.artist, x.track), axis=1)
    
    # Load the link cache file
    link_df = pd.read_csv("data/link_cache.csv", index_col=0)

    # Update the main DF with the link DF
    hottest_100_DF["song_url"] = hottest_100_DF.apply(lambda x: update_df(x.artist, x.track, x.song_url, link_df), axis=1)

    # Update the val_link column after updating the links
    hottest_100_DF["val_link"] = hottest_100_DF.apply(lambda x: add_missing_col(x.song_url), axis=1)

    # Save the main DF as cache.csv
    hottest_100_DF.to_csv("data/cache.csv")

    # Print the time that it took to complete
    print(f"time to complete: {datetime.now() - start}")
    return hottest_100_DF


def plot_countries(data_df):
    print(data_df["country"].value_counts())


data = main(False)
# plot_countries(data)
