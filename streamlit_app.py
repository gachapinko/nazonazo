import streamlit as st
import random

# 1. ページ設定
st.set_page_config(page_title="なぞなぞ パーティー", page_icon="🎉", layout="centered")

# 2. クイズデータ（各10問）
if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = {
        "子供向け": [
            {"q": "パンはパンでも、食べられないパンは何？", "h": "動物園にいる白黒の...", "a": "パンダ", "icon": "❓"},
            {"q": "あかい色をしていて、あまくて、つぶつぶがあるくだものは？", "h": "冬から春が旬だよ", "a": "いちご", "icon": "😋"},
            {"q": "おふろにいれると、ふわふわうかんで、からだをあらうときに使うものは？", "h": "あわあわになるよ", "a": "スポンジ", "icon": "🧼"},
            {"q": "いつもおなかのポケットに赤ちゃんをいれている動物は？", "h": "ぴょんぴょんはねるよ", "a": "カンガルー", "icon": "🐾"},
            {"q": "あお、きいろ、あか、の3つの色があって、みちで光っているものは？", "h": "「とまれ」や「すすめ」を教えてくれるよ", "a": "しんごう", "icon": "🚦"},
            {"q": "よるにそらでピカピカ光っている、おほしさまの形をしたものは？", "h": "バナナみたいな形のときもあるよ", "a": "つき", "icon": "🌙"},
            {"q": "しまうまの体にある、白と黒のもようは何ていう？", "h": "お洋服の柄でも人気だよ", "a": "しましま", "icon": "🦓"},
            {"q": "ゾウさんの体の中で、一番長いところはどこ？", "h": "そこでお水を飲んだりもするよ", "a": "はな", "icon": "🐘"},
            {"q": "お口を大きくあけて「ガオー」となく、百獣の王は？", "h": "かっこいい、たてがみがあるよ", "a": "ライオン", "icon": "🦁"},
            {"q": "雨がやんだあと、空にかかる7色の橋はなーんだ？", "h": "お空の虹（にじ）のことだよ", "a": "にじ", "icon": "🌈"}
        ],
        "大人向け": [
            {"q": "上に行けば行くほど、低くなるものは？", "h": "自分の「声」のことです", "a": "地声", "icon": "📢"},
            {"q": "切っても切っても、切り口がない透明なものは？", "h": "蛇口をひねると出てくるよ", "a": "水", "icon": "🔍"},
            {"q": "お父さんが嫌いな食べ物は何？", "h": "パパがいやだ（パパ・イヤ）と言うから...", "a": "パパイヤ", "icon": "🍴"},
            {"q": "使うときは投げて、使わないときは引き上げるものは？", "h": "船が止まるときに使うよ", "a": "いかり", "icon": "⚓"},
            {"q": "世界中にいるのに、一人もいない国はどこ？", "h": "国名に注目してみて", "a": "韓国", "icon": "🇰🇷"},
            {"q": "あるときは2つ、ないときは0、これなーんだ？", "h": "漢字の「二」をイメージしてみて", "a": "穴", "icon": "🕳️"},
            {"q": "火を通すと、名前が「あ」から「い」に変わる貝は？", "h": "焼くと「焼き〇〇」になるよね", "a": "あさり", "icon": "🐚"},
            {"q": "春、夏、秋、冬、一番長いのはいつ？", "h": "文字数を数えてみて！", "a": "お正月", "icon": "🎍"},
            {"q": "とっても大きなカメがいるけど、絶対に動かないカメは？", "h": "写真や動画を撮るのに使うよ", "a": "カメラ", "icon": "📸"},
            {"q": "一軒家、マンション、アパート。一番おしゃべりなのはどれ？", "h": "「〇〇〇〇」がよく聞こえるよ", "a": "マンション", "icon": "🏢"}
        ],
        "女の子向け": [{"q": "ひらがな3文字。鏡の中の私に挨拶して？", "h": "こたえは「わたし」だよ", "a": "わたし", "icon": "✨"}] * 10,
        "男の子向け": [{"q": "エンジンがついていて速く走る乗り物は？", "h": "ブーン！車だよ", "a": "くるま", "icon": "🏎️"}] * 10,
        "ひっかけ問題": [{"q": "10円玉2枚、合計はいくら？", "h": "シンプルに考えて！", "a": "20円", "icon": "💰"}] * 10,
        "雑学クイズ": [{"q": "シマウマの地肌の色は？", "h": "白か黒か...", "a": "黒", "icon": "🦓"}] * 10
    }

# 3. セッション管理
if "course" not in st.session_state: st.session_state.course = None
if "current_idx" not in st.session_state: st.session_state.current_idx = 0
if "score" not in st.session_state: st.session_state.score = 0
if "is_finished" not in st.session_state: st.session_state.is_finished = False
if "hint_visible" not in st.session_state: st.session_state.hint_visible = False
if "answered" not in st.session_state: st.session_state.answered = False

# テーマ設定
theme_styles = {
    "子供向け": {"bg": "#fff3e0", "main": "#ff8f00", "dots": "#ffcc80"},
    "大人向け": {"bg": "#fffde7", "main": "#fbc02d", "dots": "#fff59d"},
    "女の子向け": {"bg": "#fce4ec", "main": "#ec407a", "dots": "#f8bbd0"},
    "男の子向け": {"bg": "#e3f2fd", "main": "#1e88e5", "dots": "#bbdefb"},
    "ひっかけ問題": {"bg": "#f3e5f5", "main": "#8e24aa", "dots": "#e1bee7"},
    "雑学クイズ": {"bg": "#e8f5e9", "main": "#43a047", "dots": "#c8e6c9"},
    "None": {"bg": "#ffffff", "main": "#ff8f00", "dots": "#eeeeee"}
}
current_style = theme_styles[str(st.session_state.course)]

# スタイル適用
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {current_style['bg']};
        background-image: radial-gradient({current_style['dots']} 2px, transparent 2px);
        background-size: 40px 40px;
    }}
    .quiz-card {{
        background-color: #ffffff;
        padding: 30px;
        border-radius: 30px;
        border: 5px solid {current_style['main']};
        text-align: center;
        margin-bottom: 20px;
    }}
    /* ボタンの共通設定 */
    .stButton>button {{
        width: 100%;
        border-radius: 50px;
        font-weight: bold;
        transition: 0.3s;
        border: none;
    }}
    /* ヒント（小さめ・黄色） */
    div[data-testid="stVerticalBlock"] > div:nth-child(3) .stButton>button {{
        height: 2.2em;
        background-color: #fff9c4;
        color: #fbc02d;
        font-size: 0.8em;
    }}
    /* 答え合わせ（赤系） */
    div[data-testid="column"]:nth-child(1) .stButton>button {{
        background-color: #ef5350;
        color: white;
        height: 3.5em;
    }}
    /* 次へ（テーマカラー） */
    div[data-testid="column"]:nth-child(2) .stButton>button {{
        background-color: {current_style['main']};
        color: white;
        height: 3.5em;
    }}
    .retire-btn button {{
        background-color: #f5f5f5 !important;
        color: #999 !important;
        height: 2.5em !important;
    }}
    h1 {{ text-align: center; font-family: 'Hiragino Maru Gothic Pro'; }}
    /* スマホ用調整 */
    @media (max-width: 640px) {{
        .quiz-card {{ padding: 20px; }}
        h1 {{ font-size: 1.8em; }}
    }}
    </style>
    """, unsafe_allow_html=True)

# --- トップ画面 ---
if st.session_state.course is None:
    st.title("🎈 なぞなぞ パーティー 🎊")
    st.write("<p style='text-align: center;'>どれであそぶ？</p>", unsafe_allow_html=True)
    
    # スマホでも崩れないように、1つずつのボタンにするか2列にする
    for c, icon in zip(st.session_state.quiz_data.keys(), ["🧸", "👔", "🎀", "🚀", "💥", "🎓"]):
        if st.button(f"{icon} {c}"):
            st.session_state.course = c
            st.session_state.score, st.session_state.current_idx = 0, 0
            st.session_state.is_finished, st.session_state.answered = False, False
            st.rerun()
    st.stop()

# --- クイズ終了画面 ---
if st.session_state.is_finished:
    st.title("🏆 結果発表")
    st.markdown(f"""<div class="quiz-card"><h1>{st.session_state.score} / 10</h1><p>正解したよ！</p></div>""", unsafe_allow_html=True)
    if st.button("トップにもどる"):
        st.session_state.course = None
        st.rerun()
    st.stop()

# --- プレイ中画面 ---
col_ret, _ = st.columns([1, 2])
with col_ret:
    st.markdown('<div class="retire-btn">', unsafe_allow_html=True)
    if st.button("リタイア"):
        st.session_state.course = None
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

quiz = st.session_state.quiz_data[st.session_state.course][st.session_state.current_idx]
st.title(f"🎉 {st.session_state.course}")

st.markdown(f"""
    <div class="quiz-card">
        <div style='font-size: 3.5em;'>{quiz["icon"]}</div>
        <p style='color: {current_style['main']}; font-weight: bold;'>第 {st.session_state.current_idx + 1} 問</p>
        <h2 style='font-size: 1.5em;'>{quiz["q"]}</h2>
    </div>
    """, unsafe_allow_html=True)

# ヒントセクション（重なり防止）
st.write("") # スペース確保
if not st.session_state.hint_visible:
    if st.button("💡 ヒント"):
        st.session_state.hint_visible = True
        st.rerun()
else:
    st.info(f"💡 {quiz['h']}")

# 回答入力
user_ans = st.text_input("こたえをかいてね", placeholder="なーんだ？", key=f"q_{st.session_state.current_idx}")

# アクションボタン
col1, col2 = st.columns(2)
with col1:
    if st.button("✨ 判定"):
        st.session_state.answered = True
        if user_ans.strip() == quiz["a"]:
            st.balloons()
            st.session_state.score += 1
            st.success("正解！")
        else:
            st.error(f"残念！答え：{quiz['a']}")

with col2:
    # 状態を確実に進めるためにキーを工夫
    if st.button("つぎへ ➡️"):
        if st.session_state.current_idx < 9:
            st.session_state.current_idx += 1
            st.session_state.hint_visible = False
            st.session_state.answered = False
            st.rerun()
        else:
            st.session_state.is_finished = True
            st.rerun()
