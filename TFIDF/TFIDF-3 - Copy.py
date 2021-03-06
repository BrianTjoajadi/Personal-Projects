from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import linear_kernel
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

import string
import re
import os
import nltk
import pandas as pd
import numpy as np
import numpy.linalg as LA
import glob

#Please edit: change it to read excel files, each article as a list item
path = "c:\\Users\\btjoa\\OneDrive\\Desktop\\Babson\\Grad\\Programming in Python\\Personal Projects\\stories"

dataset = []
for filename in glob.glob(os.path.join(path, '*.txt')):
   with open(os.path.join(os.getcwd(), filename), 'r', encoding="cp1250", errors="ignore") as f:
       dataset.append(f.read().strip())


#No need for changes
#Preprocessing

#turn everything to lower case
dataset = [data.lower() for data in dataset]
# print(dataset)

#strip punctuation
# This uses str.translate to map all punctuation to the empty string
table = str.maketrans('', '', string.punctuation)
dataset = [data.translate(table) for data in dataset]

# Convert all numbers in the article to the word 'num' using regular expressions
dataset = [re.sub(r'\d+', 'num', data) for data in dataset]

#stopwords
stopwords = set(stopwords.words('english'))
dataset = [[word for word in data.split() if word not in stopwords] for data in dataset]

#stemming (A better option would be to lemmatize, but it takes forever)
stemmer = PorterStemmer()
dataset = [" ".join([stemmer.stem(word) for word in data]) for data in dataset]

#Vectorizing dataset
vectorizer = TfidfVectorizer(tokenizer = word_tokenize, analyzer = "word", ngram_range=(1, 2))
tfidf = vectorizer.fit_transform(np.array(dataset))

# #for viewing data in a table
# feature_names = vectorizer.get_feature_names()
# dense = tfidf.todense()
# denselist = dense.tolist()
# df = pd.DataFrame(denselist, columns=feature_names)
# print(df)

# def cosine_sim(a, b):
#     cos_sim = np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))
#     return cos_sim


#Query Searches

from sklearn.metrics.pairwise import cosine_similarity


def cosine_similarities(q, k = 10):
    """
    Takes a query, and returns the most 'similar' documents based on their cosine similarity scores between the query and each document

    q : represents the query
    k : number of similar documents we're looking for. (Default set at 10)

    Possible changes: change q to *q to enable taking multiple queries
    """

    query = []
    query.append(q)
    query = [word.lower() for word in query]
    table = str.maketrans('', '', string.punctuation)
    query = [word.translate(table) for word in query]
    query = [re.sub(r'\d+', 'num', word) for word in query]
    query = [[word for word in data.split() if word not in stopwords] for data in query]
    query = [" ".join([stemmer.stem(word) for word in data]) for data in query]
    queryVectorizer = vectorizer.transform(query).toarray()

    #cosine similarity formula below, not needed because importing cosine_similarity from sklearn
    #cx = lambda a,b : np.inner(a, b)/(np.linalg.norm(a)*np.linalg.norm(b)) 
    
    cosine_similarities = cosine_similarity(queryVectorizer[:], tfidf)
    related_docs_indices = cosine_similarities.flatten().argsort()[-k][::-1]
    return (related_docs_indices)

#prints the 
print(cosine_similarities("Without the drive of Rebeccah's insistence, Kate lost her momentum. She stood next a slatted oak bench, canisters still clutched, surveying"))






##Original Code from stackoverflow lol
# from sklearn.datasets import fetch_20newsgroups

# twenty = fetch_20newsgroups()
# print(twenty)

# query = ["Without the drive of Rebeccah's insistence, Kate lost her momentum. She stood next a slatted oak bench, canisters still clutched, surveying"]

# tfidf1 = TfidfVectorizer().fit_transform(query)
# print(tfidf1)

# tfidf = TfidfVectorizer().fit_transform(twenty.data)
# print(tfidf[0:1])
# cosine_similarities = linear_kernel(tfidf[0:1], tfidf).flatten()
# related_docs_indices = cosine_similarities.argsort()[:-5:-1]
# print(related_docs_indices)