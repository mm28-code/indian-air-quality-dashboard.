import streamlit as st
import pandas as pd

# Set your username and password
USERNAME = "mm28"
PASSWORD = "manish@28"

# Function to check credentials
def check_credentials():
    """Prompt for username and password, and verify credentials."""
    with st.form("login_form"):
        username = st.text_input("Username:")
        password = st.text_input("Password:", type="password")
        submit = st.form_submit_button("Login")
        
        if submit:
            if username == USERNAME and password == PASSWORD:
                return True
            else:
                st.warning("Incorrect Username or Password")
                return False
    return False

# Authenticate user
if check_credentials():
    # Hide the login form after successful login
    st.empty()  # This will remove the login form

    # Display your dashboard after successful login
    st.title("Indian Air Quality Dashboard")

    # Power BI embed URL (replace with your actual Power BI link)
    powerbi_url = "https://app.powerbi.com/view?r=eyJrIjoiZjdlZjg3NDUtNjcwNC00MWY3LWE5OWYtZTIxZDQ4NTY0NDliIiwidCI6ImRjNTdkYjliLWNjNTQtNDI5Yi1iOWU4LTBhZmZhMzZmMDY2NiJ9"
    
    # Zoom functionality (adjusted to fit screen)
    zoom_level = st.slider("Zoom Level", min_value=50, max_value=150, value=100)
    iframe_width = "100%"  # Full screen width
    iframe_height = f"{zoom_level * 0.6}vh"  # Adjust height proportionally to viewport height

    # Embed Power BI report inside an iframe
    st.markdown(f'<iframe width="{iframe_width}" height="{iframe_height}" src="{powerbi_url}" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)

    # Example data for download (modified to PBIX format is not possible directly, 
    # as PBIX is a proprietary format and requires Power BI Desktop to generate. 
    # However, you can provide a link to download the report from Power BI Service)
    st.warning("Note: Downloading as PBIX is not supported here. You can download from Power BI Service instead.")
    st.markdown("### Alternative: Download as CSV")
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

    # Feedback feature
    st.header("Provide Feedback")
    with st.form("feedback_form"):
        feedback = st.text_area("Your Feedback:")
        submit_feedback = st.form_submit_button("Submit Feedback")
        
        if submit_feedback:
            # You can store the feedback in a database or a file
            with open("feedback.txt", "a") as f:
                f.write(feedback + "\n")
            st.success("Thank you for your feedback!")
