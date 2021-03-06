"""CODE BY STUART TODA"""

import pandas as pd
from bs4 import BeautifulSoup
import requests
import string
import sys
import concurrent.futures
import time
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

#read the csv
df = pd.read_csv("TrainingSetv1.csv", engine="python")
#head
df.head()

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

t1 = time.perf_counter()
final = {}

#Downloading Text
def download_text(url):
    try:
        global info
        info = {}
        r = requests.get(url, headers = headers)
        time.sleep(10)
        html_doc= r.text
        soup = BeautifulSoup(html_doc, 'lxml')
        #print(soup.prettify())
        if soup.find_all('p'):
            y =""
            for x in soup.find_all('p'):
                y += x.get_text()
            info[url] = y      #changed soup.title.text with url
        elif soup.find_all('section'):
            y = ""
            for x in soup.find_all('section'): #section class = 'articlebody'
                y += x.get_text()
            info[url] = y     #changed soup.title.text with url
    except:
        e = sys.exc_info()[0]
        print(e)
        print(url)
    
    final.update(info)
  
  
for chunk in pd.read_csv("TrainingSetv1.csv", engine="python", chunksize=50):   #INPUT CSV FILE HERE 
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_text, chunk.iloc[:,2]) #change 4 to the column number of URL
        
    
t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')

#confirmation that we have all/most the articles
i = pd.read_csv('TrainingSetv1.csv', engine='python')
print('The length of the original dataset is' ,len(i))
print("\n")
print('The number of articles we succesfully grabbed body text from is',len(final))

#dictionary to dataframe
body_text = pd.DataFrame(list(final.items()),columns = ['url','body_text']) 

#Adding body text to csv
for x in range(len(df)):
    for y in range(len(body_text)):
        if df.iloc[x,2] == body_text.iloc[y,0]:
            df.loc[x,'body_text' ] = body_text.loc[y,'body_text']

#look for columns
for x in df.columns:
    print(x)

#look for na in rows
for x in range(len(df.columns)):
    print(df.iloc[:,x].isnull().sum())

#export to df
df.to_csv('covid_articles_2.csv', index = False)
            