import streamlit as st
import pandas as pd
import base64
import io

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
    
    # Embed Power BI report inside an iframe (adjusted width and height)
    st.markdown(f'<iframe width="100%" height="75%" src="{powerbi_url}" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)
    
    # Feedback Section with Rating
    st.subheader("Feedback")
    rating = st.slider("Rate the Dashboard:", 1, 5, 3)
    st.write(f"Your Rating: {rating} stars")
    
    feedback = st.text_area("Please provide your feedback:")
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")

    # Example data for download (in CSV format for this case)
    df = pd.DataFrame({
        "Location": ["Location A", "Location B", "Location C"],
        "PM2.5": [35, 42, 27],
        "PM10": [55, 60, 45]
    })

    # Function to convert dataframe to a download link for CSV
    def convert_df_to_csv(df):
        # Converting DataFrame to CSV
        csv = df.to_csv(index=False)
        return csv

    # Download button for CSV
    csv = convert_df_to_csv(df)
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name="air_quality_data.csv",  # Changed to CSV
        mime="text/csv"
    )
else:
    st.warning("Please log in to access the dashboard.")
