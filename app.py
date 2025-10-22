
# app.py
# -*- coding: utf-8 -*-
#Create an entry point script that defines and connects your pages
import streamlit as st

st.set_page_config(
    page_title="WINGS OF WONDER", #title on  the tab
    page_icon="🐦", 
    layout="wide")

with st.sidebar:
    st.image('assets/logo.png')

pages = {
    "Home": [
        st.Page("pages/4_text.py", title="Home"),
    ],
    "Birds": [
        st.Page("pages/Cols.py", title="Birds"),
       
    ],
    "Images": [
        st.Page("pages/Poster.py", title="Poster"),
        st.Page("pages/Story.py", title="Storyboard"),
        st.Page("pages/Gallery.py", title="Gallery"),
        st.Page("pages/banner.py", title="Sketch"),

    ],
    "Podcast": [
        st.Page("pages/Podcast.py", title="Podcast"),
    ],
    "Videos": [
        st.Page("pages/Video.py", title="Video"),
        st.Page("pages/Animation.py", title="Animation"),

    ],
    
}

with st.container(width='stretch',height="content"):
    st.image('assets/banner.png')
po=st.sidebar.selectbox("Navigation Bar", ["top", "sidebar", "hidden"], key="NP")

pg = st.navigation(pages,position=po)
pg.run()







