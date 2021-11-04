#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Hottest 100 data collection
Scrapes the TripleJ website to collect the yearly rankings and then attempting to find trends and 
patterns that correlate to the positions of various songs.

TODO List
=========
TODO: Scrape data from genius links. Look into BeautifulSoup to see if it may be useful.
TODO: Find other sources for information on these songs.
    * Is it possible to analyse the actual song?
    * Get artist details
TODO: Combine the data from Genius.com with the current dataframe containing the Hottest 100 data
TODO: Collect functions into separate files that represent functionality
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


# =========== Useful Functions ==================
# Move to a utils file
def find_between(s, first, last, search_string):
    """Find in the string "s", the substring between the 2 substrings "first" and "last"

    :param s: The main string that the search will be conducted through
    :param first: The initial substring that encloses the returned substring
    :param last: The last substring that encloses the returned substring
    :param search_string: A string that can be searched in the found string. If not used enter ""
    :return: A list of all substrings that are enclosed by the first and last substrings
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


def replace_from_list_strings(string_replace, list_chars, replace_char):
    """ Replace a list of chars in a string
    
    :param string_replace: string that contains characters that need to be replaced
    :param list_chars: list of characters to be replaces
    :param replace_char: character that replaces the other
    :return: string with characters replaced
    """
    for i in list_chars:
        string_replace = string_replace.replace(i, replace_char)
    return(string_replace)


# =========== Data Cleaning Functions ===========
# Move to a data preprocessing file


# =========== Scraping Functions ================
# Move to a scraping file
def scrape_jjj():
    """Scrapes data from the JJJ website and returns a list of dictionaries of track data
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
        replace_from_list_strings(i, ["\r", "\n"], "")
        out_text+=i+"\n"
    
    # Split string at ] to get track data. Album data can be accessed by using the second element in the split output.
    out_text = out_text.replace("var tracks = ", ").replace("window.h100site = {path: "/triplej/hottest100/archive" }", ")
    tracks = json.loads(out_text.split("var albums = [")[0])
    
    #pp.pprint(tracks)
    return pd.DataFrame(tracks)


def check_url(test_url):
    """ Check URL exists
    
    :param test_url: URL to be checked
    :return: True if URL exists, False otherwise
    """
    # Request page
    page = requests.get(test_url)

    # Error handling for the page
    if page.status_code == 200:
        valid = True
    else:
        valid = False
    return valid


def prep_url(name, song):
    """ prepare the url based on name and song
    
    :param name: artist name
    :param song: song name
    :return: a url to be tested
    """
    # Create the genius URL
    base_url = "https://genius.com/"
    end_url = "-lyrics"
    mid_url = name+"-"+song

    # Replace special chars in the URL
    mid_url = mid_url.replace(" ", "-")
    replace_list = ["/", ".", "{", "}", ",", ".", "!", "?", "'", "(", ")"]
    mid_url = replace_from_list_strings(mid_url, replace_list, "")
    mid_url = mid_url.replace("&", "and")

    # Construct the full URL
    genius_url = base_url+mid_url+end_url
    genius_url = genius_url.replace("--", "-")
    return genius_url


def add_song_url(name, song):
    """ Applied to a DF to add a column with a URL based on the artist name and song

    :param name: artist name
    :param song: song name
    :return: A string constructed from name and song or placeholder if URL not found
    """
    url = prep_url(name, song)
    if check_url(url):
        out_url = "XX-"
    else:
        out_url = url
    return out_url


def add_missing_col(check_str):
    """ Applied to a DF based on if a URL contains XX-
    
    :param check_str: the string that will be searched in
    :return: Boolean if check_str contains XX-
    """
    # Add a column that checks if the url contains "XX-"
    search_str = "XX-"
    if search_str in check_str:
        return True
    else:
        return False


def google_search(search_term, api_key, cse_id, **kwargs):
        """Find in the string "s", the substring between the 2 substrings "first" and "last"

    :param s: The main string that the search will be conducted through
    :param first: The initial substring that encloses the returned substring
    :param last: The last substring that encloses the returned substring
    :param search_string: A string that can be searched in the found string. If not used enter ""
    :return: A list of all substringa that are enclosed by the first and last substrings
    """
    # Currently limited to 100 queries a day
    # Figure a more efficient way of searching google
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    resJSON = res["items"][0]
    url = resJSON["link"]
    return url


def search_for_url(name, song):
    """Find in the string "s", the substring between the 2 substrings "first" and "last"
    
    :param name: artist name
    :param song: song name
    :return: url that has been searched for
    """
    # Enter google API and CSE IDs
    API_KEY = "YY"
    CSE_ID = "XX"

    my_query = f"{name} {song} genius"  # Create the search term
    genius_head = "https://genius.com/" # Looking for this term in the search result to confirm website
    link = "XX-" # This is the default link for when the search is unsuccessful

    # Search Google
    my_url = google_search(my_query, API_KEY, CSE_ID)

    if genius_head in my_url: # Check if the first result is from Genius.com
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
    """ Applied to a DF to update the url column

    :param name: artist name
    :param song: song name
    :param url: initial url
    :param update_df: DF that the basis for the update
    :return: the updated url
    """
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
    """Find in the string "s", the substring between the 2 substrings "first" and "last"

    :param search_google: Boolean (True if google search is required)
    :return: DF containing the results of the scraping
    """
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
            curr_df["song_url"] = curr_df.apply(lambda x: search_for_url(x.artist, x.track), axis=1)
    
    # Load the link cache file
    link_df = pd.read_csv("data/link_cache.csv", index_col=0)
    hottest_100_DF["song_url"] = hottest_100_DF.apply(lambda x: update_df(x.artist, x.track, x.song_url, link_df), axis=1)
    hottest_100_DF["val_link"] = hottest_100_DF.apply(lambda x: add_missing_col(x.song_url), axis=1)
    hottest_100_DF.to_csv("data/cache.csv")

    print(f"time to complete: {datetime.now() - start}")
    return hottest_100_DF


def plot_countries(data_df):
    print(data_df["country"].value_counts())


data = main(False)
# plot_countries(data)
