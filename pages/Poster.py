
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

