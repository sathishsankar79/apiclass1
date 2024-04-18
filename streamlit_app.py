import streamlit as st
from datetime import datetime
import gspread
 
# Load the Google Sheets credentials from secrets
credentials_info = st.secrets["gcp_service_account"]
 
# Authenticate using the credentials
gc = gspread.service_account_from_dict(credentials_info)
 
# Open the Google Sheet by ID extracted from the secrets
spreadsheet_id = "10scZE22D48M19dMc8BhHzWIhs33haUjmCkMAeKQG34E"
sheet = gc.open_by_key(spreadsheet_id).sheet1
 
st.title("Green Boot Camp")
st.subheader("Attendance Tracker")
 
# Input from the users
date=st.date_input("Date")
 
people_options=["Marie", "Sathish", "Zahra", "Aycan","Andreas", "Jacky","Lukas", "Philipp", "Moritz", "Nikolay"]
people=st.selectbox("Select the person", people_options)
 
Attendance_options=["Present", "Absent"]
attendance=st.selectbox("Attendance", Attendance_options)
 
if st.button("Submit"):
 
    dataToAppend= [date.strftime("%Y-%m-%d"), people, attendance]
 
    next_row=len(sheet.get_all_values())+1
    sheet.insert_row(dataToAppend, next_row, value_input_option='USER_ENTERED')
 
    st.success("Attendance has been recorded successfully")