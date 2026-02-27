import streamlit as st
import random

# 1. ページ設定
st.set_page_config(page_title="なぞなぞ パーティー", page_icon="🎉")

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

# 3. セッション状態の初期化
if "course" not in st.session_state:
    st.session_state.course = None
if "current_idx" not in st.session_state:
    st.session_state.current_idx = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "is_finished" not in st.session_state:
    st.session_state.is_finished = False
if "hint_visible" not in st.session_state:
    st.session_state.hint_visible = False

# --- コース選択画面 ---
if st.session_state.course is None:
    st.title("🎈 なぞなぞ パーティー 🎊")
    st.write("<p style='text-align: center; font-size: 1.5em;'>どれであそぶ？</p>", unsafe_allow_html=True)
    row1 = st.columns(3)
    row2 = st.columns(3)
    courses = list(st.session_state.quiz_data.keys())
    icons = ["🧸", "👔", "🎀", "🚀", "💥", "🎓"]
    for i, (c, icon) in enumerate(zip(courses, icons)):
        target_row = row1 if i < 3 else row2
        if target_row[i % 3].button(f"{icon} {c}"):
            st.session_state.course = c
            st.session_state.score = 0
            st.session_state.current_idx = 0
            st.session_state.is_finished = False
            st.rerun()
    st.stop()

# --- クイズ画面 or 結果画面 ---
course = st.session_state.course
quiz_list = st.session_state.quiz_data[course]
theme_styles = {
    "子供向け": {"bg": "#fff3e0", "main": "#ff8f00", "dots": "#ffcc80"},
    "大人向け": {"bg": "#fffde7", "main": "#fbc02d", "dots": "#fff59d"},
    "女の子向け": {"bg": "#fce4ec", "main": "#ec407a", "dots": "#f8bbd0"},
    "男の子向け": {"bg": "#e3f2fd", "main": "#1e88e5", "dots": "#bbdefb"},
    "ひっかけ問題": {"bg": "#f3e5f5", "main": "#8e24aa", "dots": "#e1bee7"},
    "雑学クイズ": {"bg": "#e8f5e9", "main": "#43a047", "dots": "#c8e6c9"}
}
style = theme_styles[course]

st.markdown(f"<style>.stApp {{ background-color: {style['bg']}; background-image: radial-gradient({style['dots']} 2px, transparent 2px); background-size: 40px 40px; }} .quiz-card {{ background-color: #ffffff; padding: 40px; border-radius: 40px; border: 6px solid {style['main']}; text-align: center; }} .stButton>button {{ width: 100%; border-radius: 50px; background-color: {style['main']}; color: white; border: none; height: 3.5em; font-weight: bold; }} .retire-btn > div > button {{ background-color: rgba(0,0,0,0.1) !important; color: #444 !important; }} h1 {{ text-align: center; color: {style['main']}; }}</style>", unsafe_allow_html=True)

# 🏆 結果発表画面
if st.session_state.is_finished:
    st.title("✨ パーティー・リザルト ✨")
    st.markdown(f"""
        <div class="quiz-card">
            <div style='font-size: 5em;'>🏆</div>
            <h2>お疲れ様でした！</h2>
            <p style='font-size: 1.5em;'>あなたのスコアは...</p>
            <h1 style='font-size: 4em;'>{st.session_state.score} / 10</h1>
            <p>{ "パーティーの主役級！" if st.session_state.score >= 8 else "ナイス・チャレンジ！" }</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("もういちど遊ぶ"):
        st.session_state.course = None
        st.rerun()
    st.stop()

# 📝 クイズ中画面
st.markdown('<div class="retire-btn">', unsafe_allow_html=True)
if st.button("🏃‍♂️ リタイアする"):
    st.session_state.course = None
    st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

quiz = quiz_list[st.session_state.current_idx]
st.title(f"🎉 {course}")

st.markdown(f"""
    <div class="quiz-card">
        <div style='font-size: 4em; margin-bottom: 15px;'>{quiz["icon"]}</div>
        <p style='color: {style['main']}; font-weight: bold;'>第 {st.session_state.current_idx + 1} 問 / 10</p>
        <h2 style='color: #333;'>{quiz["q"]}</h2>
    </div>
    """, unsafe_allow_html=True)

if not st.session_state.hint_visible:
    if st.button("💡 ヒントをみる"):
        st.session_state.hint_visible = True
        st.rerun()
else:
    st.warning(f"💡 ヒント： {quiz['h']}")

user_ans = st.text_input("こたえをかいてね", placeholder="なーんだ？", key=f"ans_{st.session_state.current_idx}")

if st.button("✨ こたえあわせ"):
    if user_ans.strip() == quiz["a"]:
        st.balloons()
        st.session_state.score += 1
        st.success("🎉 せいかい！")
    else:
        st.error(f"💦 ざんねん！ 答えは「{quiz['a']}」だったよ。")
    
    # 3秒待たずにボタンで次に進ませる
    if st.button("つぎへ ➡️"):
        if st.session_state.current_idx < 9:
            st.session_state.current_idx += 1
            st.session_state.hint_visible = False
            st.rerun()
        else:
            st.session_state.is_finished = True
            st.rerun()
