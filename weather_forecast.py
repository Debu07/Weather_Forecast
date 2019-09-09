import requests , pandas as pd
from bs4 import BeautifulSoup
pages=requests.get('https://forecast.weather.gov/MapClick.php?lat=34.099420000000066&lon=-118.33108999999996')
soup = BeautifulSoup(pages.content,'html.parser')
week=soup.find(id='seven-day-forecast-body')
items=week.find_all(class_='tombstone-container')
#print(items[0])
#print(items[0].find(class_='period-name').get_text())
#print(items[0].find(class_='short-desc').get_text())
#print(items[0].find(class_='temp').get_text())

period_names=[item.find(class_='period-name').get_text() for item in items]
print(period_names)
short_desc=[item.find(class_='short-desc').get_text() for item in items]
print(short_desc)
temp=[item.find(class_='temp').get_text() for item in items]
print(temp)

weather_stuff=pd.DataFrame(
    {'period':period_names,
     'short_desc':short_desc,
     'temperature':temp
     })
print(weather_stuff)
weather_stuff.to_csv('weather report.csv')

