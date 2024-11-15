import streamlit as st
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64
import io
import time

# Set your username and password
USERNAME = "mm28"
PASSWORD = "manish@28"

# SMTP configuration
smtp_server = "smtp.office365.com"
smtp_port = 587
smtp_user = "support@aptpath.in"
smtp_password = "kjydtmsbmbqtnydk"
sender_email = "support@aptpath.in"
receiver_emails = ["mks60209@gmail.com"]

# Function to send feedback email
def send_email(subject, body, receiver_emails):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = ", ".join(receiver_emails)
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(sender_email, receiver_emails, msg.as_string())
        return True
    except Exception as e:
        st.error(f"Error sending email: {e}")
        return False

# Function to check credentials
def check_credentials():
    """Prompt for username and password, and verify credentials."""
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")

    if username == USERNAME and password == PASSWORD:
        return True
    else:
        st.warning("Incorrect Username or Password")
        return False

# **Page Configuration**
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'show_dashboard' not in st.session_state:
    st.session_state.show_dashboard = False

# **Login and Redirect Logic**
if not st.session_state.logged_in:
    # **Page 1: Login**
    st.title("Login to Access Dashboard")
    if check_credentials():
        st.session_state.logged_in = True
        st.session_state.show_dashboard = True
        st.success("Logged in successfully!")
        # Redirect to dashboard page
        with st.spinner('Loading Dashboard...'):
            time.sleep(1)
            st.empty()  # Clear the login page content
            st.session_state.show_dashboard = True
    elif st.button("Login"):
        if check_credentials():
            st.session_state.logged_in = True
            st.session_state.show_dashboard = True
else:
    if st.session_state.show_dashboard:
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
            if feedback.strip():
                feedback_body = f"User Feedback:\n\nRating: {rating} stars\n\nFeedback:\n{feedback}"
                email_sent = send_email("Dashboard Feedback", feedback_body, receiver_emails)
                if email_sent:
                    st.success("Thank you for your feedback! It has been sent successfully.")
                else:
                    st.error("Failed to send feedback. Please try again later.")
            else:
                st.warning("Please provide feedback before submitting.")

        # **Example Data for Download (CSV)**
        df = pd.DataFrame({
            "Location": ["Location A", "Location B", "Location C"],
            "PM2.5": [35, 42, 27],
            "PM10": [55, 60, 45]
        })

        # **Function to Convert DataFrame to CSV Download**
        def convert_df_to_csv(df):
            csv = df.to_csv(index=False)
            return csv

        # **Download Button for CSV**
        csv = convert_df_to_csv(df)
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name="air_quality_data.csv",
            mime="text/csv"
        )
