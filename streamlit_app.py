import streamlit as st
import pandas as pd
import time

# Set your username and password
USERNAME = "mm28"
PASSWORD = "manish@28"

# **Page Configuration**
st.set_page_config(page_title="Indian Air Quality Dashboard")

# **Initialize session states for login and display control**
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# **Function to check credentials**
def check_credentials(username, password):
    """Verify username and password."""
    return username == USERNAME and password == PASSWORD

# **Login Logic**
if not st.session_state.logged_in:
    # **Page 1: Login**
    st.title("Login to Access Dashboard")
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")
    
    # Button to trigger login check
    if st.button("Login"):
        if check_credentials(username, password):
            st.session_state.logged_in = True
            st.success("Logged in successfully!")
            # Redirect to dashboard after delay
            with st.spinner('Loading Dashboard...'):
                time.sleep(1)
            st.experimental_rerun()  # Refresh the page to show dashboard
        else:
            st.warning("Incorrect Username or Password")
else:
    # **Page 2: Dashboard (only accessible after login)**
    st.title("Indian Air Quality Dashboard")
    st.markdown("<h3 style='text-align: center;'>Welcome, " + USERNAME + "!</h3>", unsafe
