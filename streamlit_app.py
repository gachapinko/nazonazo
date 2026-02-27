import streamlit as st
import random

# 1. ページ設定
st.set_page_config(page_title="なぞなぞ パーティー", page_icon="🎉")

# 2. クイズデータ（ネタバレなし！）
if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = {
        "子供向け": [
            {"q": "パンはパンでも、食べられないパンは何？", "h": "動物園にいる白黒の...", "a": "パンダ", "icon": "❓"},
            {"q": "あかい色をしていて、あまくて、つぶつぶがあるくだものは？", "h": "冬から春が旬だよ", "a": "いちご", "icon": "😋"},
            {"q": "おふろにいれると、ふわふわうかんで、からだをあらうときに使うものは？", "h": "あわあわになるよ", "a": "スポンジ", "icon": "🧼"},
            {"q": "いつもおなかのポケットに赤ちゃんをいれている動物は？", "h": "ぴょんぴょんはねるよ", "a": "カンガルー", "icon": "🐾"}
        ],
        "大人向け": [
            {"q": "上に行けば行くほど、低くなるものは？", "h": "自分の「声」のことです", "a": "地声", "icon": "📢"},
            {"q": "切っても切っても、切り口がない透明なものは？", "h": "蛇口をひねると出てくるよ", "a": "水", "icon": "🔍"},
            {"q": "お父さんが嫌いな食べ物は何？", "h": "パパがいやだ（パパ・イヤ）と言うから...", "a": "パパイヤ", "icon": "🍴"},
            {"q": "使うときは投げて、使わないときは引き上げるものは？", "h": "船が止まるときに使うよ", "a": "いかり", "icon": "⚓"}
        ]
    }

# セッション状態の初期化
if "course" not in st.session_state:
    st.session_state.course = None
if "current_idx" not in st.session_state:
    st.session_state.current_idx = 0
if "hint_visible" not in st.session_state:
    st.session_state.hint_visible = False

# --- コース選択画面 ---
if st.session_state.course is None:
    st.title("🎈 なぞなぞ パーティー 🎊")
    st.write("<p style='text-align: center; font-size: 1.5em;'>どちらのコースであそぶ？</p>", unsafe_allow_html=True)
    
    col_k, col_a = st.columns(2)
    with col_k:
        if st.button("🧸 こども向け"):
            st.session_state.course = "子供向け"
            st.rerun()
    with col_a:
        if st.button("👔 おとな向け"):
            st.session_state.course = "大人向け"
            st.rerun()
    st.stop()

# --- クイズ画面 ---
course = st.session_state.course
quiz_list = st.session_state.quiz_data[course]
quiz = quiz_list[st.session_state.current_idx]

# デザイン設定（リクエスト通りの配色！）
if course == "子供向け":
    bg_base = "#fff3e0"  # 薄いオレンジ
    main_color = "#ff8f00" # 濃いオレンジ
    bg_dots = "#ffcc80"   # ドットの色
else:
    bg_base = "#fffde7"  # 薄いイエロー
    main_color = "#fbc02d" # 濃いイエロー
    bg_dots = "#fff59d"   # ドットの色

st.markdown(f"""
    <style>
    .stApp {{
        background-color: {bg_base};
        background-image: radial-gradient({bg_dots} 2px, transparent 2px);
        background-size: 40px 40px;
    }}
    .quiz-card {{
        background-color: #ffffff;
        padding: 40px;
        border-radius: 40px;
        border: 6px solid {main_color};
        margin-bottom: 25px;
        text-align: center;
        box-shadow: 0 15px 35px rgba(0,0,0,0.05);
    }}
    .stButton>button {{
        width: 100%;
        border-radius: 50px;
        background-color: {main_color};
        color: white;
        border: none;
        height: 3.5em;
        font-weight: bold;
    }}
    /* リタイアボタン */
    .retire-btn > div > button {{
        background-color: rgba(0,0,0,0.1) !important;
        color: #444 !important;
        height: 2.5em !important;
        font-size: 0.9em !important;
    }}
    h1 {{
        text-align: center;
        color: {main_color};
        font-family: 'Hiragino Maru Gothic Pro', sans-serif;
    }}
    </style>
    """, unsafe_allow_html=True)

# リタイアボタン
st.markdown('<div class="retire-btn">', unsafe_allow_html=True)
if st.button("🏃‍♂️ リタイアする"):
    st.session_state.course = None
    st.session_state.current_idx = 0
    st.session_state.hint_visible = False
    st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

st.title(f"🎉 {course}コース")

# 問題表示
st.markdown(f"""
    <div class="quiz-card">
        <div style='font-size: 4.5em; margin-bottom: 15px;'>{quiz["icon"]}</div>
        <p style='font-size: 1.1em; color: {main_color}; font-weight: bold;'>だい {st.session_state.current_idx + 1} もん</p>
        <h2 style='color: #333; font-size: 2.2em;'>{quiz["q"]}</h2>
    </div>
    """, unsafe_allow_html=True)

# ヒント
if st.session_state.hint_visible:
    st.warning(f"💡 ヒント： {quiz['h']}")
else:
    if st.button("💡 ヒントをみる"):
        st.session_state.hint_visible = True
        st.rerun()

# 回答入力
user_ans = st.text_input("こたえをかいてね", placeholder="なーんだ？", key=f"ans_{course}_{st.session_state.current_idx}")

col1, col2 = st.columns(2)
with col1:
    if st.button("✨ こたえあわせ"):
        if user_ans.strip() == quiz["a"]:
            st.balloons()
            st.success("🎉 せいかい！ おめでとう！")
        else:
            st.error("💦 ざんねん！ もういちど 考えてみてね。")
with col2:
    if st.button("➡️ つぎへ"):
        st.session_state.current_idx = (st.session_state.current_idx + 1) % len(quiz_list)
        st.session_state.hint_visible = False
        st.rerun()
