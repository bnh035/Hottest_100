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

# ===============================================

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


def get_url(artist_name, artist_song):
    # Creates the URL for a song by an artist.
    # This is then used to scrape the song information.
    
    # Replace special chars in data
    artist_name_url = artist_name.replace(" ", "-")
    artist_song_url = artist_song.replace(" ", "-")
    replace_list = [",", "!", "?", "'", "(", ")"]
    artist_song_url = replace_from_list_strings(artist_song_url, replace_list)
    
    # Create the genius URL
    base_url = "https://genius.com/"
    end_url = "-lyrics"
    genius_url = base_url+artist_name_url+"-"+artist_song_url.lower()+end_url

    # Request page
    page = requests.get(genius_url)

    # Error handling for the page
    if page.status_code == 200:
        return genius_url
    else:
        return artist_name


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


# ======= Data Analysis ==============
def country_breakdown(d_frame):  # pass hot_lists to work
    # TODO: Tidy this mess up
    country_df = pd.DataFrame()
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
    for i in range(len(d_frame)):
        test_df = d_frame[i]
        test_df = test_df.set_index(index_list).count(level="country")
        test_df.columns = [1993+i]
        country_df = pd.concat([country_df, test_df], axis=1)
    country_df = country_df.fillna(0).astype(int)
    country_df.loc[:, 'Total'] = country_df.sum(numeric_only=True, axis=1)
    summary_df = country_df.sort_values(by=['Total'], ascending=False).head(3)
    other_df = country_df.sort_values(by=['Total'], ascending=False).tail(country_df.shape[0]-3)
    other_df.plot.pie(y='Total')
    plt.show()


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


# ============ process_csvs.py ==============
def change_date(date_str):
    charsList = [' ', '[', ']']
    date_str = replace_from_list_strings(date_str, charsList)
    month = re.search(',(.*),', date_str)
    return month.group(1)

def process_csvs():
    start_year = 1993
    end_year = 2018
    years = list(range(start_year, end_year+1))
    months = list(range(1, 13))
    total_count = pd.DataFrame(columns=years, index=months)
    total_rank = pd.DataFrame(columns=years, index=months)
    for year in years:
        csv_str = str(year)+'.csv'
        test_df = pd.read_csv(csv_str, encoding='latin-1')
        stripped_df = pd.concat([test_df['position'], test_df['country'], test_df['release_date']], axis=1)
        stripped_df = stripped_df[stripped_df['release_date'] != '---']
        stripped_df['release_month'] = stripped_df.apply(lambda row: change_date(row['release_date']), axis=1)
        stripped_df['Points'] = stripped_df['position'].apply(lambda x: 101 - x)

        ranked_df = stripped_df.groupby('release_month')['Points'].sum()
        ranked_df.index = ranked_df.index.astype(int)
        ranked_df = ranked_df.sort_index()
        total_rank[year] = ranked_df

        count = stripped_df['release_month'].value_counts().rename_axis('Month').to_frame('Counts')
        count.index = count.index.astype(int)
        count = count.sort_index()
        total_count[year] = count['Counts']

    total_rank.loc[:, 'Total'] = total_rank.sum(numeric_only=True, axis=1)
    print(total_rank)
    total_count.plot(kind='bar', stacked=True)
    plt.show()

