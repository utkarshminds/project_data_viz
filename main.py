import pandas
import streamlit as st

#pandas - data storage/manipulation
#streamlit - web front end and gui

import matplotlib.pyplot as plt #graphs or data viz
import numpy#- data storage/manipulation

from services.bar_graph import display_bar_graph
from services.histogram import display_histogram 


import hmac



def check_password():
    """Returns `True` if the user had a correct password."""

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["username"] in st.secrets[
            "passwords"
        ] and hmac.compare_digest(
            st.session_state["password"],
            st.secrets.passwords[st.session_state["username"]],
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the username or password.
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show inputs for username + password.
    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False


if not check_password():
    st.stop()

# Main Streamlit app starts here


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