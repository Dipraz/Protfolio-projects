#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")


import pandas as pd
import streamlit as st

def get_data_from_csv():
    df = pd.read_csv(r"C:\Users\dip07\Downloads\superstore (1).csv\superstore (1).csv", usecols=list("B:R"), nrows=1000)
    df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    return df

# Call the function to retrieve the data
df = get_data_from_csv()

# Calculate average quantity
average_quantity = df["Quantity"].mean()

# Check for NaN values
if pd.isnull(average_quantity):
    average_quantity = 0

# Display the average quantity
st.write("Average Quantity:", average_quantity)

# Display a star rating based on the average quantity
quantity = ":star:" * int(round(average_quantity, 0))

# Display the star rating
st.write("Quantity Rating:", quantity)



# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")
city = st.sidebar.multiselect(
    "Select the City:",
    options=df["City"].unique(),
    default=df["City"].unique()
)


# In[17]:


segment_type = st.sidebar.multiselect(
    "Select the Customer Type:",
    options=df["Segment"].unique(),
    default=df["Segment"].unique(),
)


# In[18]:


sales = st.sidebar.multiselect(
    "Select the Gender:",
    options=df["Sales"].unique(),
    default=df["Sales"].unique()
)


# In[21]:


df_selection = df.query(
    "City == @city & Segment ==@segment_type & Sales == @sales"
)


# In[22]:


# ---- MAINPAGE ----
st.title(":bar_chart: Sales Dashboard")
st.markdown("##")


# In[26]:


# TOP KPI's
total_profit = int(df_selection["Profit"].sum())
average_quantity = round(df_selection["Quantity"].mean(), 1)
quantity = ":star:" * int(round(average_quantity, 0))
average_sale_by_transaction = round(df_selection["Profit"].mean(), 2)


# In[27]:


left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Profit:")
    st.subheader(f"US $ {total_profit:,}")
with middle_column:
    st.subheader("Average Rating:")
    st.subheader(f"{average_quantity} {quantity}")
with right_column:
    st.subheader("Average Sales Per Transaction:")
    st.subheader(f"US $ {average_sale_by_transaction}")


# In[28]:


st.markdown("""---""")


# In[34]:


# SALES BY HOUR [BAR CHART]
sales_by_month = df_selection.groupby(by=["order month"]).sum()[["Sales"]]
fig_monthly_sales = px.bar(
    sales_by_month,
    x=sales_by_month.index,
    y="Sales",
    title="<b>Sales by month</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_month),
    template="plotly_white",
)
fig_monthly_sales.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)


# In[36]:


left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_monthly_sales, use_container_width=True)


# In[37]:


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


# In[ ]:




