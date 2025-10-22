
# pages/2_Video.py
import streamlit as st
import base64

st.set_page_config(page_title="Video", page_icon="🎞️", layout="wide")


tab1, tab2 = st.tabs(["1", "2"])

with tab1:
    st.header("1")
    with st.container(width=800,border=False):
      st.video("assets/video1.mp4", loop=True,subtitles="assets/sub.vtt")
with tab2:
    st.header("2")
    with st.container(width=800,border=False):
      st.video("assets/video2.mp4", loop=True,subtitles="assets/sub.vtt")
