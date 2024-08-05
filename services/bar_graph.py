import matplotlib.pyplot as plt
import streamlit

def display_bar_graph(data):
    '''
    data : dataframe column
    '''
    fig, ax = plt.subplots()
    data.value_counts().plot(kind='bar')
    streamlit.pyplot(fig)
