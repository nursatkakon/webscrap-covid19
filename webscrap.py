from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.worldometers.info/coronavirus/'
req = requests.get(url)
soup = BeautifulSoup(req.content, 'lxml')

labels = []
world = soup.find('table', {'id': 'main_table_countries_today'})
trs = world.find_all('tr')
ths = [v.text.replace('\n', '') for v in trs[0].find_all('th')]
#print(len(thElements))
#print(thElements)
df = pd.DataFrame(columns=ths)

for i in range(1, len(trs)):
    tds = trs[i].find_all('td')
    if len(tds) == 19:
        values = [tds[0].text, tds[1].text.replace('\n', ''), tds[2].text, tds[3].text, tds[4].text, tds[5].text, tds[6].text, tds[7].text, tds[8].text, tds[9].text, tds[10].text, tds[11].text, tds[12].text, tds[13].text, tds[14].text, tds[15].text, tds[16].text, tds[17].text, tds[18].text]
    else:
        values = [td.text for td in tds]
    #print(values)
    #break
    df = df.append(pd.Series(values, index=ths), ignore_index=True)
    df.to_csv(r'/Users/nursatkakon/Desktop/git/covid_visualizer/' + 'coviddata.csv', index=False)


'''     
***IT'S WORKING***
world = soup.find('table', {'id': 'main_table_countries_today'})
countries = world.tbody
for rows in countries.find_all('tr', {'style': ''}):
    #if (countries_row != countries.tr({'class': 'total_row_world row_continent'}) or countries_row != ({'class': 'row_continent total_row'})):
    #rows = countries.find_all('tr')  # each country info
    cols = rows
    for col in cols.find_all('td'):
        print(col.text)
'''