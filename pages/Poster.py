
# pages/Poster.py
import streamlit as st
import time

st.set_page_config(page_title="Poster · Multimedia Container", page_icon="🖼️", layout="wide")
st.title('Poster')


tab1, tab2 = st.tabs(["1", "2"])
with tab1:
    st.header("1")
    with st.container(border=True,width='stretch',height='content'):
        st.image("assets/poster1.png")
with tab2:    
    st.header("2")
    with st.container(border=True, width='stretch',height="content"):
        st.image("assets/poster2.png")
st.text("The posters are based on my own photography, capturing a dynamic moment of a New Holland honeyeater and a couple of kookaburras in motion. Designed in Figma, the poster uses its natural color palette to evoke freshness and vitality, with high visual contrast to enhance the overall impact. ")
