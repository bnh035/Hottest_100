from bs4 import BeautifulSoup
import requests
import calendar
from datetime import datetime

url1 = "https://genius.com/Bush-swallowed-lyrics"


def get_url(artist_name, artist_song):
    artist_name = artist_name.replace(" ", "-")
    artist_song = artist_song.replace(" ", "-")
    base_url = "https://genius.com/"
    end_url = "-lyrics"
    genius_url = base_url+artist_name+"-"+artist_song.lower()+end_url
    page = requests.get(genius_url)
    if page.status_code == 200:
        return genius_url
    else:
        return FileNotFoundError


def parse_date(date_string):
    name_to_num = {name: num for num, name in enumerate(calendar.month_name) if num}
    for month, number in name_to_num.items():
        date_string = date_string.replace(month, str(number))
    parsed_date = datetime.strptime(date_string, "%m %d, %Y")
    return [parsed_date.year, parsed_date.month, parsed_date.day]


def get_date(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    raw_date = 0
    for hit in soup.findAll('span', class_="metadata_unit-info metadata_unit-info--text_only"):
        raw_date = hit.text
    if raw_date == 0:
        # TODO: Change to an error
        return 0
    else:
        release_date = parse_date(raw_date)
        return release_date

test_name = "Allen Ginsberg"
test_song = "Ballad Of The Skeletons"
url1 = get_url(test_name, test_song)
print(url1)
# print(get_date(url1))
