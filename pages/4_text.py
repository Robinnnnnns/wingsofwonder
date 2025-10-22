import streamlit as st

st.set_page_config(page_title="Wings of Wonder", layout="centered")

st.title("Wings of Wonder")
st.header("Exploring the Beauty of Australian Birds")

tabs = st.tabs([
    "Background",
    "Motivation"])

with tabs[0]:
    st.subheader("This website")
    st.text("Australia hosts an extraordinary diversity of bird species, yet many locals and international visitors may not fully know it. These birds play vital roles in ecosystem balance, while also enriching the country’s cultural and natural heritage. This multimedia platform aims to bring birds closer to the public, transforming curiosity into care and awareness.")
    st.image("assets/poster1.png")

with tabs[1]:
    st.subheader("About author")
    st.text("As a bird photographer myself, I want to introduce to audience through vivid photography, immersive podcast and video, and 3D modeling animation, all from my original work. The website invites visitors to see, hear, and feel the wonder of native birds through my own portfolio and studio. As a bird lover, I want to share the joy of birdwatching and the beauty of birds with the audience.")
    st.image("assets/poster2.png")


