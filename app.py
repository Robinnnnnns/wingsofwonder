# app.py
# -*- coding: utf-8 -*-
import streamlit as st

st.set_page_config(
    page_title="WINGS OF WONDER",
    page_icon="🐦",
    layout="wide"
)

st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background: linear-gradient(180deg, #E0F7FA 0%, #C8E6C9 100%);
}


[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #E0F7FA 0%, #A5D6A7 100%);
    border-right: 3px solid #81C784; /* 草绿色描边 */
    box-shadow: 2px 0 10px rgba(0, 0, 0, 0.1);
}


[data-testid="stSidebar"] h1, 
[data-testid="stSidebar"] h2, 
[data-testid="stSidebar"] h3, 
[data-testid="stSidebar"] p, 
[data-testid="stSidebar"] span {
    color: #2E7D32 !important;
    font-weight: 500;
}


[data-testid="stHorizontalBlock"] img {
    border-radius: 12px;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
}


div[data-baseweb="select"] > div {
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.image('assets/logo.png', use_container_width=True)
   

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
        st.Page("pages/Animation.py", title="3D Animation"),
    ],
}

with st.container():
    st.image('assets/banner.png', use_container_width=True)

po = "sidebar"
pg = st.navigation(pages, position=po)
pg.run()
