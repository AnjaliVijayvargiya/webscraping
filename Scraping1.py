import requests
from bs4 import BeautifulSoup
import pandas as pd
from glob import glob

data = pd.read_csv('url_int.csv')
datac = pd.read_csv('ATG.csv')

url_list = data['Interesting URLs']
#url_list = ['https://insider.in/all-digital-events-in-online','https://insider.in/all-digital-events-in-online?priceFilter=free','https://insider.in/all-digital-events-in-online-today']

for m in range(len(url_list)):
    url = url_list[m]
    r = requests.get(url)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent,'html.parser')

    popi = soup.find_all('div',class_='event-card-details')

    list = []

    for i in range(len(popi)):
        for e in popi[i].children:
            for f in e.children:
                #print(f.text)
                list.append(f.text)
    #print(list)
    list1 = [list[x:x+5] for x in range(0, len(list),5)]
    if len(list1) == 0:
        print('Event data is not found.')
        continue
    print(list1)
    df11 = pd.DataFrame(list1, columns = ['Title','Date & Time','Mode','Price','Etc'])
    del df11['Etc']
    list = datac['Interested_Group']
    #print(list)
    listn = []
    ik = 0
    for i in df11['Title']:
        ik +=1
        for j in list:
            if j in i:
                print(i,j,ik)
                listn.append((i,j,ik,url))
                
    #print(listn)
    df15 = pd.DataFrame(listn, columns = ['Title','Matching Word','Position','url'])
    df15.to_csv('classify.csv')
    
    df11['Processed URL'] = url
    df11.to_csv('event_'+str(m)+'.csv')




