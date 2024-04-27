import streamlit as st

btn = st.button("←")
st.title("概要・題名")
content = st.text_input("", max_chars=None)

# style.cssファイルからスタイルを読み込む
with open(r"C:\Users\user\Documents\GitHub\mikke-viewer\app\style.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)