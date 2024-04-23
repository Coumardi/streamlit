import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image

# Title
st.title('Streamlit Demo')

# Header
st.header('This is a header')

# Subheader
st.subheader('This is a subheader')

# Text
st.write('This is some text.')

# Markdown
st.markdown('## This is a Markdown title')

# Dataframes
df=pd.read_csv('museum_data.csv')
columns_to_drop= ['Museum ID', 'Alternate Name',
                  'County Code (FIPS)','State Code (FIPS)','Region Code (AAM)',
                  'Tax Period','Legal Name','Institution Name','Institution Name',
                  'Locale Code (NCES)']
df.drop(columns=columns_to_drop, inplace=True)

st.write('Data Table:')
st.write(df)



#compute the average
data = pd.read_csv('museum_data.csv')


# Step 3: Data Summarization and Statistics
# Total number of museums
total_museums = len(data)

# Different types of museums
museum_types = data['Museum Type'].value_counts()

# Average income and revenue
average_income = data['Income'].mean()
average_revenue = data['Revenue'].mean()

st.write("Total number of museums:", total_museums)
st.write("Different types of museums:")
st.write(museum_types)
st.write("Average income:", average_income)
st.write("Average revenue:", average_revenue)



fig, ax = plt.subplots(figsize=(10, 6))
museum_types.plot(kind='bar', ax=ax)

# Set title and labels
plt.title('Distribution of Museums by Type')
plt.xlabel('Museum Type')
plt.ylabel('Count')

# Display the plot using Streamlit
st.pyplot(fig)

# Pie chart to show proportion of museums in each state
fig, ax = plt.subplots(figsize=(50, 20))  # Adjust the figure size as needed
state_counts = data['State (Administrative Location)'].value_counts()
state_counts.plot(kind='pie', autopct='%1.1f%%', ax=ax)
plt.title('Proportion of Museums in Each State')
plt.ylabel('')  # Remove the y-label

# Display the plot using Streamlit
st.pyplot(fig)







# Create a DataFrame with the latitude and longitude columns


#map
st.write('Map:')
map_data = pd.DataFrame(
   
    columns=['Latitude', 'Longitude']
)
st.write(map_data)
st.map(map_data)














