#!/usr/bin/env python
# coding: utf-8
#dip07.raz@gmail.com
# In[1]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# In[2]:


st.set_page_config(layout='wide', initial_sidebar_state='expanded')


# In[3]:


# In[4]:


st.sidebar.header('Dashboard `version 1`')


# In[6]:


st.sidebar.subheader('Heat map parameter')
time_hist_color = st.sidebar.selectbox('Color by', ('temp_min', 'temp_max')) 


# In[7]:


st.sidebar.subheader('Donut chart parameter')
donut_theta = st.sidebar.selectbox('Select data', ('a2', 'a3'))


# In[8]:


st.sidebar.subheader('Line chart parameters')
plot_data = st.sidebar.multiselect('Select data', ['temp_min', 'temp_max'], ['temp_min', 'temp_max'])
plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)


# In[9]:

st.sidebar.markdown('''
---
Created by [Dipraj_Howlader](https://www.facebook.com/dipraz07/).
''')


# In[10]:


# Row A
st.markdown('### Metrics')
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")


# In[11]:


# Row B
seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')


# In[12]:


# Assuming 'seattle_weather' is a DataFrame with temperature data
# Check the column names in the DataFrame
print(seattle_weather.columns)

# Update the column names for temperature data
seattle_weather['temp_max'] = pd.to_numeric(seattle_weather['temp_max'], errors='coerce')
seattle_weather['temp_min'] = pd.to_numeric(seattle_weather['temp_min'], errors='coerce')

# In[13]:


c1, c2 = st.columns((7, 3))
seattle_weather['date'] = pd.to_datetime(seattle_weather['date'])
seattle_weather.set_index('date', inplace=True)

weekly_weather = seattle_weather.resample('W').mean()
with c1:
    st.markdown('### Heatmap')
    fig, ax = plt.subplots(figsize=(10, 4))
    sns.histplot(data=weekly_weather, y='temp_min', bins='auto', cbar=True, cbar_kws={'shrink': 0.5}, ax=ax)
    ax.set_xlabel('Date')
    ax.set_ylabel('Day')
    ax.set_title('Time Histogram')
    st.pyplot(fig)


with c2:
    # Create the donut chart using Matplotlib
    fig, ax = plt.subplots(figsize=(10, 13))
    donut_data = stocks['company'].value_counts()
    colors = sns.color_palette('Set3', len(donut_data))
    ax.pie(donut_data, labels=donut_data.index, colors=colors, startangle=90, counterclock=False, wedgeprops={'edgecolor': 'white'})
    ax.add_artist(plt.Circle((0, 0), 0.6, color='white'))

    # Customize the plot
    ax.set_title('Donut Chart')
    ax.axis('equal')

    # Show the donut chart using st.pyplot()
    st.pyplot(fig)

    # Disable the PyplotGlobalUseWarning
    st.set_option('deprecation.showPyplotGlobalUse', False)


# Row C
st.markdown('### Line chart')
st.line_chart(seattle_weather, x = 'date', y = plot_data, height = plot_height)





