import pandas as pd
from bs4 import BeautifulSoup
import requests
import string
import sys
import concurrent.futures
import time
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("TestingSetv1_summ.csv", engine="python")
df = df[["Index", "Title", "body_text"]]

print(df.head())

# df = df.drop(["Summary"])

df = df.assign(Index=df['Index'].apply(pd.to_numeric, errors='coerce'))

# df = df.to_frame()
print(type(df))

df = df.dropna()

df.to_csv('covid_articles_3.csv', index = False)