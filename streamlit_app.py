import streamlit as st

powerbi_url = "https://app.powerbi.com/reportEmbed?reportId=YOUR_REPORT_ID&groupId=YOUR_GROUP_ID"

st.markdown(f'<iframe width="100%" height="600" src="{powerbi_url}" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)
