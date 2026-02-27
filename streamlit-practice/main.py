import streamlit as st

st.title("Programming Language App")
st.subheader("Brewed with Streamlit")
st.text("Welcome to your interactive app!")
select =st.selectbox("Select an option:", ["Python", "C++", "Java", "JavaScript", "Go", "Rust"])
st.write(f"You selected: {select}, excellent choice!")

st.success("Your Programming Language of choice has been recorded.")
