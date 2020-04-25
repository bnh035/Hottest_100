import pandas as pd
import re
import matplotlib.pyplot as plt

start_year = 1993
end_year = 2018
years = list(range(start_year, end_year+1))
months = list(range(1, 13))


def change_date(date_str):
    date_str = date_str.replace(' ', '')
    date_str = date_str.replace('[', '')
    date_str = date_str.replace(']', '')
    month = re.search(',(.*),', date_str)
    return month.group(1)

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
    #print(ranked_df)
    # print(type(ranked_df))
    total_rank[year] = ranked_df

    count = stripped_df['release_month'].value_counts().rename_axis('Month').to_frame('Counts')
    count.index = count.index.astype(int)
    count = count.sort_index()
    total_count[year] = count['Counts']

total_rank.loc[:, 'Total'] = total_rank.sum(numeric_only=True, axis=1)
print(total_rank)
total_count.plot(kind='bar', stacked=True)
plt.show()
