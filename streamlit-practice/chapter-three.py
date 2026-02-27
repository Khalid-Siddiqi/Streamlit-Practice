from datetime import date
import streamlit as st


min_date_allowed = date(1900, 1, 1)
st.title("Age Calculator App")
name = st.text_input("Enter your name:")
dob = st.date_input("Select your date of birth:", min_value=min_date_allowed, max_value=date.today(), value=date(2000, 1, 1))
if st.button("Calculate Age"):
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    st.write(f"Hello, {name}! You are {age} years old.")