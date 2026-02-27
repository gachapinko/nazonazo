import streamlit as st
import random

# 1. ページ設定
st.set_page_config(page_title="暇な時にやろう なぞなぞ パーティー", page_icon="🎉", layout="centered")

# 2. クイズデータ（全カテゴリーをオリジナルの10問ずつに差し替え）
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
        "女の子向け": [
            {"q": "ガラスの靴を忘れていったお姫様はだれ？", "h": "カボチャの馬車に乗るよ", "a": "シンデレラ", "icon": "👠"},
            {"q": "赤くて丸くて、唇にぬる化粧品はなーんだ？", "h": "リップともいうよ", "a": "口紅", "icon": "💄"},
            {"q": "鏡の中の私にひらがな3文字で挨拶して？", "h": "鏡にうつっているのは...", "a": "わたし", "icon": "✨"},
            {"q": "ピンク色の耳が長くて、ぴょんぴょん跳ねる動物は？", "h": "にんじんが大好き", "a": "うさぎ", "icon": "🐰"},
            {"q": "ピアノを弾くときに見る、音符が書いてある本は？", "h": "「が」から始まるよ", "a": "楽譜", "icon": "🎹"},
            {"q": "キラキラ光って、指につけるアクセサリーは？", "h": "「ゆ」から始まるよ", "a": "指輪", "icon": "💍"},
            {"q": "お花の蜜を集めて、針がある小さな虫は？", "h": "黄色と黒のしましまだよ", "a": "ミツバチ", "icon": "🐝"},
            {"q": "とっても甘くて、イチゴが乗っているお祝いの食べ物は？", "h": "誕生日に食べるよ", "a": "ケーキ", "icon": "🎂"},
            {"q": "頭につける、リボンやお花がついた飾りは？", "h": "髪をまとめるよ", "a": "髪飾り", "icon": "🎀"},
            {"q": "雨の日にさす、おしゃれな道具はなーんだ？", "h": "「か」から始まるよ", "a": "傘", "icon": "☂️"}
        ],
        "男の子向け": [
            {"q": "大きな角があって、森の王様と呼ばれる虫は？", "h": "茶色くて力持ちだよ", "a": "カブトムシ", "icon": "🪲"},
            {"q": "土を掘る大きな腕がついた、工事現場の車は？", "h": "黄色い車が多いよ", "a": "ショベルカー", "icon": "🏗️"},
            {"q": "エンジンがついていて、サーキットを速く走る車は？", "h": "ブーンと鳴るよ", "a": "レーシングカー", "icon": "🏎️"},
            {"q": "海賊が探している、お宝が入った箱は？", "h": "「た」から始まるよ", "a": "宝箱", "icon": "🏴‍☠️"},
            {"q": "宇宙へ飛んでいく、火を吹く大きな乗り物は？", "h": "「ろ」から始まるよ", "a": "ロケット", "icon": "🚀"},
            {"q": "火を吹いて空を飛ぶ、伝説の大きなトカゲみたいな生き物は？", "h": "「ど」から始まるよ", "a": "ドラゴン", "icon": "🐉"},
            {"q": "11人で丸いボールを蹴って遊ぶスポーツは？", "h": "ゴールを狙うよ", "a": "サッカー", "icon": "⚽"},
            {"q": "海の中を潜って進む、窓のない船はなーんだ？", "h": "「せ」から始まるよ", "a": "潜水艦", "icon": "⚓"},
            {"q": "警察官が乗っている、白と黒の車は？", "h": "サイレンが鳴るよ", "a": "パトカー", "icon": "🚓"},
            {"q": "新幹線よりも速く、空を飛ぶ乗り物は？", "h": "翼があるよ", "a": "飛行機", "icon": "✈️"}
        ],
        "ひっかけ問題": [
            {"q": "10円玉2枚。合計はいくら？", "h": "ひっかけだよ、算数じゃないかも", "a": "20円", "icon": "💰"},
            {"q": "「シカ」と10回言って。サンタが乗るのは？", "h": "シカじゃないよ", "a": "トナカイ", "icon": "🦌"},
            {"q": "1年中、休まず動いているのに一歩も進まないのは？", "h": "チクタク鳴るよ", "a": "時計", "icon": "⏰"},
            {"q": "お父さんとお母さんの間には何がいる？", "h": "文字に注目してみて", "a": "と", "icon": "👪"},
            {"q": "「シャンデリア」と10回言って。毒リンゴを食べたのは？", "h": "シンデレラじゃないよ", "a": "白雪姫", "icon": "🍎"},
            {"q": "日本で一番高い山は富士山。では二番目は？", "h": "エベレストは日本じゃないよ", "a": "北岳", "icon": "⛰️"},
            {"q": "カメとウサギが競走しました。勝ったのはどっち？", "h": "お話の通りだよ", "a": "カメ", "icon": "🐢"},
            {"q": "右手に1つ、左手に2つ持っている体のパーツは？", "h": "「ひじ」を数えてみて", "a": "ひじ", "icon": "💪"},
            {"q": "パンはパンでも、フライパンを焼くと何になる？", "h": "食べ物じゃないよ", "a": "火傷", "icon": "🔥"},
            {"q": "100個のリンゴから10個食べました。残りは？", "h": "「残り」の数だよ", "a": "90個", "icon": "🍎"}
        ],
        "雑学クイズ": [
            {"q": "シマウマの地肌（毛を剃った色）は何色？", "h": "白か黒か...", "a": "黒", "icon": "🦓"},
            {"q": "コアラの指紋は人間とそっくり。本当か嘘か？", "h": "驚きの事実だよ", "a": "本当", "icon": "🐨"},
            {"q": "バナナは「木」になる？それとも「草」になる？", "h": "背は高いけど茎なんだよ", "a": "草", "icon": "🍌"},
            {"q": "かき氷のシロップは、実は全部同じ味。本当か嘘か？", "h": "香りが違うだけなんだよ", "a": "本当", "icon": "🍧"},
            {"q": "世界で一番読まれている本はなーんだ？", "h": "ギネス記録にもなってるよ", "a": "聖書", "icon": "📖"},
            {"q": "ショートケーキの「ショート」の本当の意味は？", "h": "短い、ではないよ", "a": "サクサクした", "icon": "🍰"},
            {"q": "トランプの数字を全部足すと、何日になる？", "h": "ジョーカー1枚を1として足すと...", "a": "365", "icon": "🃏"},
            {"q": "太陽の光が地球に届くまで、何分かかる？", "h": "8分ちょっとだよ", "a": "8分", "icon": "☀️"},
            {"q": "キリンの舌の色は何色？", "h": "日焼けしないように濃い色だよ", "a": "青紫色", "icon": "🦒"},
            {"q": "宇宙で唯一、肉眼で見える人工建造物は？", "h": "中国にあるよ", "a": "万里の長城", "icon": "🇨🇳"}
        ]
    }

# 3. セッション管理
if "course" not in st.session_state: st.session_state.course = None
if "current_idx" not in st.session_state: st.session_state.current_idx = 0
if "score" not in st.session_state: st.session_state.score = 0
if "is_finished" not in st.session_state: st.session_state.is_finished = False
if "hint_visible" not in st.session_state: st.session_state.hint_visible = False
if "answered" not in st.session_state: st.session_state.answered = False
if "wrong_list" not in st.session_state: st.session_state.wrong_list = []

# テーマカラー設定
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

# CSS適用
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
    .stButton>button {{
        width: 100%;
        border-radius: 50px;
        font-weight: bold;
        transition: 0.3s;
        border: none;
    }}
    .ans-btn button {{
        background-color: #ef5350 !important;
        color: white !important;
        height: 3.5em !important;
        box-shadow: 0 4px 0 #c62828;
    }}
    .next-btn button {{
        background-color: {current_style['main']} !important;
        color: white !important;
        height: 3.5em !important;
        box-shadow: 0 4px 0 {current_style['dots']};
    }}
    .retire-btn button {{
        background-color: #f5f5f5 !important;
        color: #999 !important;
        height: 2.5em !important;
    }}
    .wrong-card {{
        background-color: #fff1f0;
        border-left: 5px solid #ff4d4f;
        padding: 10px 20px;
        margin-bottom: 10px;
        border-radius: 10px;
        text-align: left;
    }}
    h1 {{ text-align: center; font-family: 'Hiragino Maru Gothic Pro'; }}
    </style>
    """, unsafe_allow_html=True)

# --- 画面制御 ---

if st.session_state.course is None:
    st.title("🎈 暇な時にやろう なぞなぞ パーティー 🎊")
    st.write("<p style='text-align: center;'>どれであそぶ？</p>", unsafe_allow_html=True)
    for c, icon in zip(st.session_state.quiz_data.keys(), ["🧸", "👔", "🎀", "🚀", "💥", "🎓"]):
        if st.button(f"{icon} {c}"):
            st.session_state.course = c
            st.session_state.score, st.session_state.current_idx = 0, 0
            st.session_state.is_finished, st.session_state.answered = False, False
            st.session_state.wrong_list = []
            st.rerun()
    st.stop()

if st.session_state.is_finished:
    st.title("🏆 結果発表")
    st.markdown(f"""<div class="quiz-card"><h1>{st.session_state.score} / 10</h1><p>正解したよ！</p></div>""", unsafe_allow_html=True)
    if st.session_state.wrong_list:
        st.subheader("📝 間違えた問題のおさらい")
        for item in st.session_state.wrong_list:
            st.markdown(f"""<div class="wrong-card"><b>問：{item['q']}</b><br><span style='color: #ff4d4f;'>あなたの答え：{item['user']}</span><br><span style='color: #52c41a; font-weight: bold;'>正解：{item['correct']}</span></div>""", unsafe_allow_html=True)
    else:
        st.balloons()
        st.success("全問正解！すごすぎる！")
    if st.button("トップにもどる"):
        st.session_state.course = None
        st.rerun()
    st.stop()

# プレイ画面
col_ret, _ = st.columns([1, 2])
with col_ret:
    st.markdown('<div class="retire-btn">', unsafe_allow_html=True)
    if st.button("リタイア"):
        st.session_state.course = None
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

quiz = st.session_state.quiz_data[st.session_state.course][st.session_state.current_idx]
st.title(f"🎉 {st.session_state.course}")
st.markdown(f"""<div class="quiz-card"><div style='font-size: 3.5em;'>{quiz["icon"]}</div><p style='color: {current_style['main']}; font-weight: bold;'>第 {st.session_state.current_idx + 1} 問</p><h2 style='font-size: 1.5em;'>{quiz["q"]}</h2></div>""", unsafe_allow_html=True)

if not st.session_state.hint_visible:
    if st.button("💡 ヒント"):
        st.session_state.hint_visible = True
        st.rerun()
else:
    st.info(f"💡 {quiz['h']}")

user_ans = st.text_input("こたえをかいてね", placeholder="なーんだ？", key=f"q_{st.session_state.current_idx}")

st.write("") 
if not st.session_state.answered:
    st.markdown('<div class="ans-btn">', unsafe_allow_html=True)
    if st.button("✨ こたえあわせ"):
        if user_ans.strip():
            st.session_state.answered = True
            is_correct = user_ans.strip() == quiz["a"]
            if is_correct:
                st.session_state.is_correct = True
                st.session_state.score += 1
            else:
                st.session_state.is_correct = False
                st.session_state.wrong_list.append({"q": quiz["q"], "user": user_ans.strip(), "correct": quiz["a"]})
            st.rerun()
        else:
            st.warning("なにか書いてね！")
    st.markdown('</div>', unsafe_allow_html=True)
else:
    if st.session_state.is_correct:
        st.success("せいかい！ ✨")
    else:
        st.error("ざんねん！最後におさらいしよう！")
    st.markdown('<div class="next-btn">', unsafe_allow_html=True)
    if st.button("つぎへ ➡️"):
        if st.session_state.current_idx < 9:
            st.session_state.current_idx += 1
            st.session_state.hint_visible = False
            st.session_state.answered = False
            st.rerun()
        else:
            st.session_state.is_finished = True
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
