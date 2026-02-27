import streamlit as st

st.title("Juice Taste Poll")
st.subheader("Brewed with Streamlit")

col1,col2 = st.columns(2)
with col1:
    st.header("Apple Juice")
    #st.image("https://images.unsplash.com/photo-1567306226416-28f0efdc88ce", width=200)
    vote1 = st.button("Vote for Apple Juice")

with col2:
    st.header("Orange Juice")
    #st.image("https://images.unsplash.com/photo-1574226516831-e1dff420e37d", width=200)
    vote2 = st.button("Vote for Orange Juice")

if vote1:
    st.success("You voted for Apple Juice!")
elif vote2:
    st.success("You voted for Orange Juice!")

name = st.sidebar.text_input("Enter your name:")
juice = st.sidebar.selectbox("Select your juice:", ["Apple Juice", "Orange Juice", "Grape Juice", "Pineapple Juice"])
if st.sidebar.button("Submit"):
    st.sidebar.write(f"{name}! Your {juice} is being prepared.")

with st.expander("See the juice preparation process"):
    st.write("1. Select fresh fruits.")
    st.write("2. Wash and cut the fruits.")
    st.write("3. Use a juicer to extract the juice.")
    st.write("4. Serve chilled and enjoy!")