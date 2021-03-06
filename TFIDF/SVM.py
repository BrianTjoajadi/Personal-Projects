from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pandas
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import roc_auc_score
from datetime import date

# read data
data = pandas.read_csv("covid_articles.csv")

#drop null values
data = data.dropna(axis=0)
#check for null
data.isnull().values.any()

# concatenate all news into one
data["combined_body_text"] = data.filter(regex=("body_text")).apply(lambda x: ''.join(str(x.values)), axis=1)

# convert to feature vector
feature_extraction = TfidfVectorizer()
X = feature_extraction.fit_transform(data["body_text"].values)

# TODO: EDIT FROM HERE
# split into training- and test set
train_df, test_df = train_test_split(df, test_size = 0.2, random_state = 42)

TRAINING_END = date(2014,12,31)
num_training = len(data[pandas.to_datetime(data["Date"]) <= TRAINING_END])
X_train = X[:num_training]
X_test = X[num_training:]
y_train = data["Label"].values[:num_training]
y_test = data["Label"].values[num_training:]

# train classifier
clf = SVC(probability=True, kernel='rbf')
clf.fit(X_train, y_train)

# predict and evaluate predictions
predictions = clf.predict_proba(X_test)
print('ROC-AUC yields ' + str(roc_auc_score(y_test, predictions[:,1])))