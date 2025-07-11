'''

@author Sam Mukherjee
Basics of ML with pandas
'''

import pandas as pd
df = pd.read_csv('reviews.csv')
'''
print('The number of reviews: ', len(df))
print(df[['title', 'rating']].head(3))


#Step 1 : Cleansing the Data pip install google_trans_new
from deep_translator import GoogleTranslator
translated = GoogleTranslator(source='auto', target='en').translate("guten Tag")
print(translated)
'''

#Step 2 : Splitting and Transforming the Data
#Chapter 11: Gaining Insights from Data
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

reviews = df['title'].values
ratings = df['rating'].values
reviews_train, reviews_test, y_train, y_test = train_test_split(reviews, ratings, test_size=0.2, random_state=1000)
vectorizer = CountVectorizer()
vectorizer.fit(reviews_train)
x_train = vectorizer.transform(reviews_train)
x_test = vectorizer.transform(reviews_test)
#print(x_train.toarray())
#print(len(x_train.toarray()[0]))
#print(len(x_test.toarray()[0]))

#Senitiment analysis
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(x_train, y_train)
#Evaluating the Model
import numpy as np
predicted = classifier.predict(x_test)
accuracy = np.mean(predicted == y_test)
print("Accuracy:", round(accuracy,2))

#make predictions fo rnew data
new_reviews = ['useless book', 'Very good effort, but not five stars', 'Clear and concise but HORRIBLE']
X_new = vectorizer.transform(new_reviews)
print(classifier.predict(X_new))

#stock
import matplotlib.pyplot as plt
import yfinance as yf
tkr = yf.Ticker('AAPL')
hist = tkr.history(period="1y")
print('===')
print(hist.dtypes)

#Get the S&P as a reference
import pandas_datareader.data as pdr
from datetime import date, timedelta
end = date.today()
start = end - timedelta(days=365)
index_data = pdr.get_data_stooq('^SPX', start, end)
print(index_data.dtypes)


index_data_no_tz = index_data.copy().tz_localize('EST')
df = index_data_no_tz[['Close','Volume']]
print(df)

df = hist[['Close','Volume']]
print(df)

hist_no_tz= hist[['Close']]
#index_data_n0_tz.index.tz = None

#Joining Sand P and APPL
index_data_no_tz_no_vol = index_data_no_tz.copy()[['Close']]
index_data_no_tz_no_vol['Close'] = index_data_no_tz_no_vol['Close'].astype(str)
df = hist_no_tz.join(index_data_no_tz_no_vol, rsuffix='__')
#df = df[['Close','Volume','Close_idx','Volume_idx']]
print(df)







