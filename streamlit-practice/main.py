import streamlit as st

st.title("WaveTec App")
st.subheader("Brewed with Streamlit")
st.text("Welcome to your interactive app!")
st.write("Chose your options below:")


st.selectbox("Select an option:", ["Kiosk Inspection", "ATM Inspection", "Human Mobility"])