import streamlit as st

btn = st.button("←")

st.title("概要・題名")
content = st.text_input("", max_chars=None)

# CSSスタイルの設定
style = """
<style>
    .title {font-size:20px}
    .input {font-size:16px; background-color: #FFFACD; border:none}
    .btn {background-color: #FFA500; color: white; border-radius:50%}
</style>
"""
st.markdown(style, unsafe_allow_html=True)