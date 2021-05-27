import requests
from bs4 import BeautifulSoup

url = "https://www.naadyogacouncil.com/en/"
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)

soup = BeautifulSoup(htmlContent,'html.parser')
#print(soup.prettify)

title = soup.title
#print(type(title))

anchors = soup.find_all('a')
all_links = set()
for link in anchors:
    if(link != "#"):
        if(link.get('href').startswith('https')):
            all_links.add(link.get('href'))
        else:
            all_links.add("https://www.naadyogacouncil.com/en"+link.get('href'))
#print(all_links)
all_links = sorted(all_links)


import numpy as np
import pandas as pd
import os
import openpyxl

df = pd.DataFrame(all_links, columns = ['URL Links']) 

tags = []
interesting_url = []
non_interesting_url = []

for i in df['URL Links']:
    if("event" in i):
        tags.append('True')
        interesting_url.append(i)
    else:
        tags.append('False')
        non_interesting_url.append(i)
#print(tags)

df['Tags'] = tags
df.to_csv('urls.csv')
#print(non_interesting_url)
interesting_url = sorted(interesting_url)
if(url == "https://www.naadyogacouncil.com/en/"):
    interesting_url.append("https://www.naadyogacouncil.com/en/events/list/?tribe_event_display=list&tribe_paged=1")
    interesting_url.append("https://www.naadyogacouncil.com/en/events/list/?tribe_event_display=list&tribe_paged=2")
    interesting_url.append("https://www.naadyogacouncil.com/en/events/list/?tribe_event_display=list&tribe_paged=3")
    interesting_url.append("https://www.naadyogacouncil.com/en/events/list/?tribe_event_display=list&tribe_paged=4")

non_interesting_url = sorted(non_interesting_url)

df1 = pd.DataFrame(interesting_url, columns = ['Interesting URLs']) 
df2 = pd.DataFrame(non_interesting_url, columns = ['Non Interesting URLs']) 

df1.to_csv('url_int.csv')
df2.to_csv('url_non_int.csv')

data = pd.read_csv('url_int.csv')
url_list = data['Interesting URLs']
