
# pages/2_Video.py
import streamlit as st
import base64

st.set_page_config(page_title="Video", page_icon="🎞️", layout="wide")

# app.py
import streamlit as st


VIDEO_PATH = "assets/video.mp4"
SUB = "assets/sub.vtt"

CHAPTERS = {
    "Intro": 0,
    "Rainbow Lorikeet": 8,
    "Noisy Miner": 30,
    "Kookaburra": 52,
}

st.title("🎬 Birdwatching Tour")

st.session_state.setdefault("chapter_time", 0)

with st.container():
    cols = st.columns(len(CHAPTERS), gap="medium")
    for i, (label, t) in enumerate(CHAPTERS.items()):
        with cols[i]:
            if st.button(label):
                st.session_state["chapter_time"] = t

    st.video(VIDEO_PATH, start_time=st.session_state["chapter_time"],subtitles="assets/sub.vtt")
   




