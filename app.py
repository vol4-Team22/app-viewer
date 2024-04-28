import streamlit as st
import uuid

from pathlib import Path

image_path = Path("C:/Users/user/Documents/GitHub/mikke-viewer/canvas__4_-removebg-preview.png")


# タイトルの表示
st.markdown(
    """
    <div style="font-family: 'Arial', sans-serif; font-size: 40px; font-weight: bold;">
        日常課題をみっけしよう！
    </div>
    """,
    unsafe_allow_html=True
)

# イラストの表示
st.image(str(image_path), width=130)

import streamlit as st

button_css = f"""
<style>
  div.stButton > button:first-child  {{
    font-weight  : bold                ;/* 文字：太字                   */
    border       :  4px solid #ffcb4c     ;/* 枠線：黄色で4ピクセルの実線 */
    border-radius: 8px 8px 8px 8px ;/* 枠線：半径8ピクセルの角丸     */
    background   : #fff7ca                ;/* 背景色：薄～い黄色            */
  }}
</style>
"""
st.markdown(button_css, unsafe_allow_html=True)

posts = [
    {"title": "投稿1", "content": "投稿1の内容", "likes": 0},
    {"title": "投稿2", "content": "投稿2の内容", "likes": 0},
    {"title": "投稿3", "content": "投稿3の内容", "likes": 0},
]

for post in posts:
    st.markdown(f"<div style='background-color: #fff7ca; padding: 8px; border-radius: 6px;'><h1 style='font-size: 24px;'>{post['title']}</h1></div>", unsafe_allow_html=True)
    
    
    st.empty()  # 空のコンポーネントを追加

    # 一意のキーを生成
    button_key = str(uuid.uuid4())

    # クリックで内容を表示
    if st.button("内容を表示", key=button_key):
        st.write(post["content"])
