import pandas
import streamlit as st

#pandas - data storage/manipulation
#streamlit - web front end and gui

import matplotlib.pyplot as plt #graphs or data viz
import numpy#- data storage/manipulation

from services.bar_graph import display_bar_graph
from services.histogram import display_histogram 

st.title('My first webpage')

st.header('Data visualization in python')

upload_file = st.file_uploader('Upload csv file', type=['csv'])

if upload_file is not None:

    data = pandas.read_csv(upload_file)

    st.write(data)

    col_names = data.columns.tolist()

    selected_col = st.selectbox('Select a column', col_names)

    if pandas.api.types.is_numeric_dtype(data[selected_col]):

        display_histogram(data[selected_col])

    else:

        display_bar_graph(data[selected_col])