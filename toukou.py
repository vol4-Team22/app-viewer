import streamlit as st

def main():
    st.title("投稿画面")

    post_content = st.text_area("概要・題名")
    post_content = st.text_area("投稿内容を入力してください")

    if st.button("投稿する"):
        # ここで投稿の処理を行う（例えば、データベースに保存するなど）
        st.success("投稿が成功しました！")

if __name__ == "__main__":
    main()
