import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.naadyogacouncil.com/en/events/feed/"
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)

soup = BeautifulSoup(htmlContent,'html.parser')
#print(soup.prettify)

title = soup.title
#print(type(title))

popi = soup.find_all('title')
#print(popi.string)
list = []
for i in range(len(popi)):
    if(i>2):
        #print(popi[i].string)
        list.append(popi[i].string)
#print(list)

popi1 = soup.find_all('comments')
#print(popi.string)
list1 = []
for i in range(len(popi1)):
    if(i>2):
        #print(popi1[i].string[-19:-9])
        list1.append(popi1[i].string[-19:-9])
#print(list1)

popi2 = soup.find_all('content:encoded')
list2 = []
for i in range(len(popi2)):
    if(i>2):
        #print(popi2[i].string[3343:3374])
        list2.append(popi2[i].string[3343:3374])
#print(list2)

popi3 = soup.find_all('description')
list3 = []
for i in range(len(popi3)):
    if(i>3):
        #print(popi3[i].string)
        list3.append(popi3[i].string)
#print(list3)
list4 = []
for i in zip(list,list1,list2,list3):
    list4.append(i)

#print(list4)
df11 = pd.DataFrame(list4, columns = ['Title','Date','Day & Time','Description'])
df11.to_csv('event_second.csv')







