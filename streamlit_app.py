import streamlit as st
import pandas as pd

# Set your username and password
USERNAME = "mm28"
PASSWORD = "manish@28"

def check_credentials():
    """Prompt for username and password, and verify credentials."""
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")
    
    if username == USERNAME and password == PASSWORD:
        return True
    else:
        st.warning("Incorrect Username or Password")
        return False

# Authenticate user
if check_credentials():
    # Display your dashboard after successful login
    st.title("Indian Air Quality Dashboard")

    # Power BI embed URL (replace with your actual Power BI link)
    powerbi_url = "https://app.powerbi.com/view?r=eyJrIjoiZjdlZjg3NDUtNjcwNC00MWY3LWE5OWYtZTIxZDQ4NTY0NDliIiwidCI6ImRjNTdkYjliLWNjNTQtNDI5Yi1iOWU4LTBhZmZhMzZmMDY2NiJ9"
    
    # Zoom functionality
    zoom_level = st.slider("Zoom Level", min_value=50, max_value=200, value=100)
    iframe_width = f"{zoom_level}%"
    iframe_height = f"{zoom_level * 0.6}%"  # Adjust height proportionally

    # Embed Power BI report inside an iframe
    st.markdown(f'<iframe width="{iframe_width}" height="{iframe_height}" src="{powerbi_url}" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)
    
    # Example data for download
    df = pd.DataFrame({
        "Location": ["Location A", "Location B", "Location C"],
        "PM2.5": [35, 42, 27],
        "PM10": [55, 60, 45]
    })

    # Download button for CSV file
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name="air_quality_data.csv",
        mime="text/csv"
    )
