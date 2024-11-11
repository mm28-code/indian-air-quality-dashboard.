import streamlit as st
import pandas as pd
import base64
import io
import qrcode

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
    
    # Embed Power BI report inside an iframe (ensuring it's visible and fits the screen)
    st.markdown(f'<iframe width="80%" height="600" src="{powerbi_url}" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)
    
    # Feedback Form with Rating and Text Area for Feedback
    st.subheader("Feedback")
    
    rating = st.slider("Rating", 1, 5, 3)  # Rating from 1 to 5
    feedback = st.text_area("Please provide your feedback:")

    if st.button("Submit Feedback"):
        st.success(f"Thank you for your feedback! You rated this {rating} stars.")

    # Example data for download (in CSV format for this case, as .pbix download isn't supported)
    df = pd.DataFrame({
        "Location": ["Location A", "Location B", "Location C"],
        "PM2.5": [35, 42, 27],
        "PM10": [55, 60, 45]
    })

    # Function to convert dataframe to CSV for download
    def convert_df_to_csv(df):
        # Converting DataFrame to CSV
        csv = df.to_csv(index=False)
        return csv

    # Download button for CSV
    csv = convert_df_to_csv(df)
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name="air_quality_data.csv",
        mime="text/csv"
    )
    
    # Generate QR Code for downloading the CSV file
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    download_url = f"data:text/csv;base64,{base64.b64encode(csv.encode()).decode()}"
    qr.add_data(download_url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill="black", back_color="white")
    
    # Display the QR Code
    st.image(qr_img, caption="Scan to download the data")
    
else:
    st.warning("Please log in to access the dashboard.")
