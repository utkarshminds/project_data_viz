
import matplotlib.pyplot as plt
import streamlit

def display_histogram(data):

    '''
    data : dataframe column
    '''
    fig, ax = plt.subplots()
    plt.hist(data, edgecolor='b', bins=4)
    streamlit.pyplot(fig)