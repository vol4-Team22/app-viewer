import streamlit as st
import requests
import json
import uuid


# GETリクエストを送信する関数
def get_request(url):
    try:
        response = requests.get(url)
        # レスポンスが成功したかどうかを確認
        if response.status_code == 200:
            return response.text
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Error: {e}"


# Using "with" notation
with st.sidebar:
    add_radio = st.sidebar.selectbox("メニュー", ("投稿する", "全ての投稿を見る", "詳細"))


if add_radio == "投稿する":
    # POSTリクエストを送信する関数
    def post_user_input(url, payload):
        try:
            headers = {"Content-Type": "application/json"}
            response = requests.post(url, data=json.dumps(payload), headers=headers)
            # レスポンスが成功したかどうかを確認
            if response.status_code == 200:
                return response.text
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return f"Error: {e}"

    st.title("投稿画面")

    post_title = st.text_area("概要・題名")
    post_comment = st.text_area("投稿内容を入力してください")

    if st.button("投稿する"):
        # ここで投稿の処理を行う（例えば、データベースに保存するなど）
        # POSTリクエストに含めるデータ
        payload = {"title": post_title, "comment": post_comment,}
        # ユーザーが入力したURL
        url = "http://localhost:18000/post"
        result = post_user_input(url, payload)
        st.text("レスポンス:")
        st.write(result)

        st.success("投稿が成功しました！")

    post_id = st.number_input("投稿ID", min_value=0, max_value=100, step=1)
    if st.button("リプライ"):
        # ここで投稿の処理を行う（例えば、データベースに保存するなど）
        # POSTリクエストに含めるデータ
        payload = {"title": post_title, "comment": post_comment, "post_id": post_id,}
        # ユーザーが入力したURL
        url = "http://localhost:18000/reply"
        result = post_user_input(url, payload)
        st.text("レスポンス:")
        st.write(result)

        st.success("投稿が成功しました！")


if add_radio == "全ての投稿を見る":

    # タイトルの表示
    st.markdown(
        """
        <div style="font-family: 'Arial', sans-serif; font-size: 40px; font-weight: bold;">
            日常課題をみっけしよう！
        </div>
        """,
        unsafe_allow_html=True,
    )
    # セッションステートの初期化
    if "data_json" not in st.session_state:
        st.session_state["data_json"] = []
    if "data_detail" not in st.session_state:
        st.session_state["data_detail"] = []

    # 全ての投稿を取得
    url = "http://localhost:18000/list"
    result = get_request(url)
    posts = json.loads(result)

    # 投稿のリストをループして、各投稿のタイトルをボタンとして表示
    for post in posts:
        if st.button(post["title"], key=post["post_id"]):
            # ボタンがクリックされたら、その投稿の詳細を取得
            detail_url = f"http://localhost:18000/post/{post['post_id']}"
            detail_result = get_request(detail_url)
            detail = json.loads(detail_result)

            # 取得した詳細を表示
            st.write(f"Title: {detail['title']}")
            st.write(f"Comment: {detail['comment']}")
            st.write(f"Created: {detail['created']}")
            st.write(f"Modified: {detail['modified']}")
    # イラストの表示
    # st.image("image\src\canvas__4_-removebg-preview.webp", width=130)

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
    # CSSを適用するためのmarkdown
    st.markdown(button_css, unsafe_allow_html=True)

    posts = st.session_state["data_detail"]

    for post in posts:
        st.markdown(
            f"<div style='background-color: #fff7ca; padding: 8px; border-radius: 6px;'><h1 style='font-size: 24px;'>{post['title']}</h1></div>",
            unsafe_allow_html=True,
        )
        st.empty()  # 空のコンポーネントを追加
        st.write(post["comment"])
        # 一意のキーを生成
        button_key = str(uuid.uuid4())

        reply_url = f"http://localhost:18000/reply/list/{post['post_id']}"
        reply_result = get_request(reply_url)
        reply_result = json.loads(reply_result)

        for i in range(len(reply_result)):
            st.divider()
            st.write(f"返信{i+1}")
            st.write(reply_result[i]["title"])
            st.write(reply_result[i]["comment"])


        st.divider()
        # クリックで内容を表示
        # if st.button("内容を表示", key=button_key):
        #     st.write(post["comment"])


if add_radio == "詳細":
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

    user_input_id = st.number_input("投稿ID", min_value=0, max_value=100, step=1)
    if st.button("キーの詳細テスト"):
        detail_url = f"http://localhost:18000/post/{user_input_id}"
        detail_result = get_request(detail_url)
        detail_result = json.loads(detail_result)

        st.markdown(
            f"<div style='background-color: #fff7ca; padding: 8px; border-radius: 6px;'><h1 style='font-size: 24px;'>{detail_result['title']}</h1></div>",
            unsafe_allow_html=True,
        )
        st.write(detail_result["comment"])

        reply_url = f"http://localhost:18000/reply/list/{user_input_id}"
        reply_result = get_request(reply_url)
        reply_result = json.loads(reply_result)

        for i in range(len(reply_result)):
            st.write(f"返信{i+1}")
            st.write(reply_result[i]["title"])
            st.write(reply_result[i]["comment"])
            st.divider()
