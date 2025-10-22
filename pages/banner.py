import streamlit as st

st.set_page_config(page_title="Sketch", page_icon="🖼️", layout="wide")



st.title("Sketch")
st.header(" ")
st.header("Logo")
with st.container(width='stretch',height="content"):
    st.image('assets/logo.png')
st.text("Inspired by the pink robin, a fascinating and iconic Australian bird, the logo incorporates its geometric shapes and vibrant color. It was hand-drawn by me in Procreate to create a friendly impression of the website.")
st.header("Banner")
with st.container(width='stretch',height="content"):
    st.image('assets/banner.png')
st.text("Drawing inspiration from the birds kookaburra and the Australian magpie, I illustrated their everyday scenes in Procreate based on my photographs. The collage-style hand-drawn technique brings out a warm and engaging character. ")