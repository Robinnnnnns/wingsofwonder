import streamlit as st
st.set_page_config(page_title="3D Models", page_icon="🎞️", layout="wide")
st.title("3D Animation")


col1, col2, col3 = st.columns(3, border=True, gap='small')


images = [
    ("assets/3D1.png", "Rainbow Lorikeet"),
    ("assets/3D2.png", "Kookaburra"),
    ("assets/3D3.png", "Mascot")
]

for col, (img_path, caption) in zip([col1, col2, col3], images):
    with col:
        # 设置相同的显示宽度让三张图等大
        st.image(img_path, use_container_width=True)
        st.caption(caption)

tab1, tab2 ,tab3= st.tabs(["1", "2","3"])

with tab1:
    st.header("Rainbow Lorikeet")
    with st.container(width=800,border=False):
      st.video("assets/3D5.mkv", loop=True)
with tab2:
    st.header("Kookaburra")
    with st.container(width=800,border=False):
      st.video("assets/3D6.mkv", loop=True)
with tab3:
    st.header("Mascot")
    with st.container(width=800,border=False):
      st.video("assets/3D7.webm", loop=True,)

st.header("Flying Movement")
with st.container(width=800,border=False):
    st.video("assets/3D4.mkv", loop=True)