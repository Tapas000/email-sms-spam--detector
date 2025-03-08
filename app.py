import streamlit as st

import pickle
import string
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.corpus import  stopwords
from nltk.stem.porter import PorterStemmer

import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
cv = CountVectorizer()
tfidf = TfidfTransformer()

ps = PorterStemmer()

def transform_text(text):
  text = text.lower()
  text = nltk.word_tokenize(text)
  y = []
  for i in text:
    if i.isalnum():    # a-z and 0-9
      y.append(i)

  text = y[:] # cloning
  y.clear()
  for i in text:
    if i not in stopwords.words('english') and i not in string.punctuation:
      y.append(i)

  text = y[:]
  y.clear()
  for i in text:
    y.append(ps.stem(i))

  return " ".join(y)


model = pickle.load(open('model.pkl','rb'))

st.title('Email/sms  Spam Classifier')

input_sms = st.text_input("Enter the message")
if st.button('Predict'):
  #Preprocessing

  transform_sms = transform_text(input_sms)

  #vectorization
  vector_input = cv.transform([transform_sms])

  #Prediction
  result = model.predict(vector_input)[0]

  #output
  if result  == 1:
      st.header("Spam")

  else:
      st.header("Not Spam")
