import streamlit as st
st.title("Podcast")


with st.container(width=800):
    st.audio('assets/Birdwatching Tour_Robin Shi.wav',
             loop=True)
    
st.image("assets/walkthrough.png")
##add chapter
