#!/usr/bin/env python
# coding: utf-8

# In[7]:


import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier


# In[8]:


st.write("""
# Simple Water Lilly Flower Prediction App
This app predicts the **Water Lilly** type!
""")


# In[9]:


st.sidebar.header('User Input Parameters')


# In[10]:


def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features


# In[11]:


df = user_input_features()

st.subheader('User Input parameters')
st.write(df)


# In[18]:


lilly = datasets.load_iris()
X = lilly.data
Y = lilly.target


# In[13]:


clf = RandomForestClassifier()
clf.fit(X, Y)


# In[19]:


prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)


# In[20]:


st.subheader('Class labels and their corresponding index number')
st.write(lilly.target_names)


# In[21]:


st.subheader('Prediction')
st.write(lilly.target_names[prediction])
#st.write(prediction)


# In[22]:


st.subheader('Prediction Probability')
st.write(prediction_proba)


# In[ ]:




