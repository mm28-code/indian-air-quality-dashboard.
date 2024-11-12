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
    st.markdown("<h3 style='text-align: center;'>Welcome, " + USERNAME + "!</h3>", unsafe_allow_html=True)
    
    # **Expanded Power BI Embed (full width)**
    powerbi_url = "https://app.powerbi.com/view?r=eyJrIjoiZjdlZjg3NDUtNjcwNC00MWY3LWE5OWYtZTIxZDQ4NTY0NDliIiwidCI6ImRjNTdkYjliLWNjNTQtNDI5Yi1iOWU4LTBhZmZhMzZmMDY2NiJ9"
    st.markdown(f'<iframe width="100%" height="800" src="{powerbi_url}" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)

    # **Feedback Section (below Power BI embed, full width)**
    st.subheader("Feedback")
    cols = st.columns(5)  # Create 5 equal columns for the rating slider
    with cols[2]:  # Center the rating slider
        rating = st.slider("Rate the Dashboard:", min_value=1, max_value=5, value=3)
    st.write(f"Your Rating: {rating} stars")
    feedback = st.text_area("Please provide your feedback (below):")
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")

    # **Example Data for Download (CSV)**
    df = pd.DataFrame({
        "Location": ["Location A", "Location B", "Location C"],
        "PM2.5": [35, 42, 27],
        "PM10": [55, 60, 45]
    })
    
    # **Function to Convert DataFrame to CSV Download**
    def convert_df_to_csv(df):
        return df.to_csv(index=False).encode('utf-8')
    
    # **Download Button for CSV**
    csv = convert_df_to_csv(df)
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name="air_quality_data.csv",
        mime="text/csv"
    )
