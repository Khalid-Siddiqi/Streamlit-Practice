import streamlit as st

st.title("Programming Language App")


if st.button("Use JavaScript"):
    st.success("You Selected JavaScript!")

use_node = st.checkbox("Use Node.JS")
if use_node:
    st.write("You also want to use Node.JS, great choice!")

frontend_types = st.radio("Select a frontend framework:", ["React", "Vue", "Angular"])
st.write(f"You selected: {frontend_types}, excellent choice!")


frontend_types = st.selectbox("Select A frontend framework:", ["React", "Vue", "Angular"])
st.write(f"You selected: {frontend_types}, excellent choice!")