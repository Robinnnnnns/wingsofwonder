import streamlit as st

st.set_page_config(page_title="Podcast", page_icon="🎙", layout="wide")


st.title("Podcast")


with st.container(width=800):
    st.audio('assets/Birdwatching Tour_Robin Shi.wav',
             loop=True)
    
st.image("assets/walkthrough.png")
##add chapter
