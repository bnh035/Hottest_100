import csv
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import calendar
from datetime import datetime
import numpy as np
import time

start = time.time()

print('Initialising...')
hot_100_df = pd.read_csv('hot100.csv')  # created from separate file
hot_lists = []
start_year = 1993
end_year = 2018
year = start_year
years = []
while year < end_year+1:
    years.append(year)
    year += 1
for i in years:
    hot_lists.append(hot_100_df[(hot_100_df['releaseyear'] == i) & (hot_100_df['alltime'] == False)].reset_index())
print('Lists prepared in: '+str(time.time() - start))


def country_breakdown(d_frame):  # pass hot_lists to work
    # TODO: Tidy this mess up
    country_df = pd.DataFrame()
    for i in range(len(d_frame)):
        test_df = d_frame[i]
        index_list = [
            "country",
            "track",
            "index",
            "alltime",
            "pollyear",
            "releaseyear",
            "artist",
            "position"
        ]
        test_df = test_df.set_index(index_list).count(level="country")
        test_df.columns = [1993+i]
        country_df = pd.concat([country_df, test_df], axis=1)
    country_df = country_df.fillna(0).astype(int)
    # country_df.plot.bar(stacked=True)
    country_df.loc[:, 'Total'] = country_df.sum(numeric_only=True, axis=1)
    summary_df = country_df.sort_values(by=['Total'], ascending=False).head(3)
    other_df = country_df.sort_values(by=['Total'], ascending=False).tail(country_df.shape[0]-3)
    other_df.plot.pie(y='Total')
    plt.show()


def get_url(artist_name, artist_song):
    artist_name_url = artist_name.replace(" ", "-")
    artist_song_url = artist_song.replace(" ", "-")
    artist_song_url = artist_song_url.replace(",", "")
    artist_song_url = artist_song_url.replace("!", "")
    artist_song_url = artist_song_url.replace("?", "")
    artist_song_url = artist_song_url.replace("'", "")
    artist_song_url = artist_song_url.replace("(", "")
    artist_song_url = artist_song_url.replace(")", "")
    base_url = "https://genius.com/"
    end_url = "-lyrics"
    genius_url = base_url+artist_name_url+"-"+artist_song_url.lower()+end_url
    page = requests.get(genius_url)
    if page.status_code == 200:
        return genius_url
    else:
        # print('Artist: '+artist_name+', Track: '+artist_song)
        return artist_name
        # retry_url = base_url+artist_name_url
        # retry_page = requests.get(retry_url)
        # if retry_page.status_code == 200:


def parse_date(date_string):
    name_to_num = {name: num for num, name in enumerate(calendar.month_name) if num}
    for month, number in name_to_num.items():
        date_string = date_string.replace(month, str(number))
    if len(date_string) < 8:
        parsed_date = datetime.strptime(date_string, "%m %Y")
        return_date = [parsed_date.year, parsed_date.month, 'X']
    else:
        parsed_date = datetime.strptime(date_string, "%m %d, %Y")
        return_date = [parsed_date.year, parsed_date.month, parsed_date.day]
    return return_date


def get_date(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        raw_date = 0
        for hit in soup.findAll('span', class_="metadata_unit-info metadata_unit-info--text_only"):
            raw_date = hit.text
        if raw_date == 0:
            # TODO: Change to an error
            return '---'
        else:
            release_date = parse_date(raw_date)
            return release_date
    except:
        return '---'

print('Starting...')
year_counter = 1993
for year in hot_lists:
    year_start = time.time()
    print('Processing year: '+str(year_counter)+'...')
    print('Searching Genius...')
    year['url'] = np.vectorize(get_url)(year['artist'], year['track'])
    print('Retrieving release dates...')
    year['release_date'] = year.apply(lambda row: get_date(row['url']), axis=1)
    print('Writing to csv...')
    year.to_csv(str(year_counter)+'.csv', index=False)
    print('Year '+str(year_counter)+" completed in: "+str(time.time() - year_start))
    year_counter += 1


print('Finished. Total time taken: '+str(time.time() - start))
# test_date = "October 1995"
# print(parse_date(test_date))
# print(test_year)
# test_name = "Allen Ginsberg"
# test_song = "Ballad Of The Skeletons"
# url1 = get_url(test_name, test_song)
# print(url1)
# print(get_date(url1))

