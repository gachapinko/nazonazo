import streamlit as st
import random
import time

# ページ設定
st.set_page_config(page_title="わくわく！なぞなぞクイズ", page_icon="💡")

# カスタムCSSでボタンを可愛く
st.markdown("""
    <style>
    /* カテゴリーボタンを大きく */
    div.stButton > button {
        width: 100%;
        height: 80px;
        font-size: 24px !important;
        font-weight: bold;
        border-radius: 20px;
    }
    /* こたえあわせボタン（赤） */
    .stElementContainer:has(#check_btn) + div button {
        background-color: #ff4d4d;
        color: white;
        border: none;
        height: 60px;
    }
    </style>
    """, unsafe_allow_html=True)

# クイズデータ（各10問）
QUIZ_DATA = {
    "たべもの 🍎": [
        {"q": "パンはパンでも、たべられないパンは？", "a": "フライパン", "c": ["メロンパン", "フライパン", "フランスパン"]},
        {"q": "上は火、下は水。これなーんだ？", "a": "おなべ", "c": ["おふろ", "おなべ", "やかん"]},
        {"q": "外は赤くて、中は白。シャリシャリたべるのは？", "a": "りんご", "c": ["りんご", "いちご", "スイカ"]},
        {"q": "むけばむくほど、なみだが出る野菜は？", "a": "たまねぎ", "c": ["キャベツ", "たまねぎ", "レタス"]},
        {"q": "おとうさんがきらいな食べ物は？", "a": "パパイヤ", "c": ["ピーマン", "パパイヤ", "セロリ"]},
        {"q": "黄色い服をぬぐと、白い体が出る果物は？", "a": "バナナ", "c": ["レモン", "バナナ", "パイナップル"]},
        {"q": "中身がないのに、名前は「中身」なのは？", "a": "ちくわ", "c": ["ドーナツ", "ちくわ", "あめ"]},
        {"q": "空を飛ぶお菓子は？", "a": "スカッシュ", "c": ["スカッシュ", "ドーナツ", "チョコ"]},
        {"q": "お弁当の真ん中によくいる酸っぱいのは？", "a": "うめぼし", "c": ["トマト", "うめぼし", "さくらんぼ"]},
        {"q": "冷たくてコーンに乗っているのは？", "a": "ソフトクリーム", "c": ["かき氷", "ソフトクリーム", "プリン"]}
    ],
    "いきもの 🐘": [
        {"q": "鼻が長くて、お耳が大きい動物は？", "a": "ゾウ", "c": ["キリン", "ゾウ", "カバ"]},
        {"q": "首がとっても長い動物は？", "a": "キリン", "c": ["キリン", "シカ", "ダチョウ"]},
        {"q": "シマシマ模様のウマは？", "a": "シマウマ", "c": ["トラ", "シマウマ", "ロバ"]},
        {"q": "お腹に袋がある動物は？", "a": "カンガルー", "c": ["カンガルー", "コアラ", "パンダ"]},
        {"q": "ひっくり返るとお菓子になる動物は？", "a": "カバ", "c": ["カバ", "トラ", "サル"]},
        {"q": "「ワン！」と鳴くのは？", "a": "イヌ", "c": ["ネコ", "イヌ", "キツネ"]},
        {"q": "夜に「ホーホー」鳴く鳥は？", "a": "フクロウ", "c": ["ハト", "カラス", "フクロウ"]},
        {"q": "白黒模様で竹を食べるのは？", "a": "パンダ", "c": ["シマウマ", "パンダ", "ペンギン"]},
        {"q": "足が速い方の動物はどっち？", "a": "ウサギ", "c": ["ウサギ", "カメ", "アリ"]},
        {"q": "百獣の王と呼ばれているのは？", "a": "ライオン", "c": ["トラ", "ライオン", "ヒョウ"]}
    ],
    "がっこう 🏫": [
        {"q": "荷物を入れる四角いカバンは？", "a": "ランドセル", "c": ["カバン", "ランドセル", "ふでばこ"]},
        {"q": "書いた字を消してくれるのは？", "a": "けしごむ", "c": ["えんぴつ", "けしごむ", "定規"]},
        {"q": "黒板に字を書くときに使うのは？", "a": "チョーク", "c": ["マジック", "チョーク", "えんぴつ"]},
        {"q": "お昼にみんなで食べるごはんは？", "a": "きゅうしょく", "c": ["おべんとう", "きゅうしょく", "おやつ"]},
        {"q": "一番速く走る運動会の競技は？", "a": "リレー", "c": ["ダンス", "リレー", "玉入れ"]},
        {"q": "長さを測る道具は？", "a": "ものさし", "c": ["のり", "ものさし", "はさみ"]},
        {"q": "紙を切る道具は？", "a": "はさみ", "c": ["カッター", "はさみ", "定規"]},
        {"q": "音楽の時間に吹く縦笛は？", "a": "リコーダー", "c": ["ピアノ", "リコーダー", "ハーモニカ"]},
        {"q": "休み時間に遊ぶ広い場所は？", "a": "こうてい", "c": ["こうてい", "きょうしつ", "体育館"]},
        {"q": "朝のあいさつ「おはよう」の次は？", "a": "こんにちは", "c": ["さようなら", "こんにちは", "おやすみ"]}
    ]
}

# セッション状態の初期化
if 'page' not in st.session_state:
    st.session_state.page = "top"
    st.session_state.score = 0
    st.session_state.q_index = 0
    st.session_state.answered = False

# --- 画面描画 ---

# TOP画面
if st.session_state.page == "top":
    st.title("💡 わくわく！なぞなぞクイズ")
    st.write("カテゴリーをえらんでね！")
    for cat in QUIZ_DATA.keys():
        if st.button(cat):
            st.session_state.category = cat
            st.session_state.page = "quiz"
            st.rerun()

# クイズ画面
elif st.session_state.page == "quiz":
    q_list = QUIZ_DATA[st.session_state.category]
    q_item = q_list[st.session_state.q_index]

    st.subheader(f"{st.session_state.category} - 第 {st.session_state.q_index + 1} 問")
    st.markdown(f"### {q_item['q']}")

    # 選択肢
    choice = st.radio("こたえをえらんでね", q_item['c'], key=f"q_{st.session_state.q_index}", index=None)

    # ボタンエリア
    if not st.session_state.answered:
        # こたえあわせボタン（赤色にするためのIDを付与）
        st.markdown('<div id="check_btn"></div>', unsafe_allow_html=True)
        if st.button("こたえあわせ"):
            if choice:
                st.session_state.answered = True
                st.rerun()
            else:
                st.warning("選択肢を選んでね！")
    else:
        # 正誤判定
        if choice == q_item['a']:
            st.success(f"✨ せいかい！ ✨ (答え: {q_item['a']})")
            st.balloons() # 紙吹雪エフェクト！
        else:
            st.error(f"ざんねん！ 答えは「{q_item['a']}」でした。")

        # つぎへボタン（こたえあわせ後に現れる）
        if st.button("つぎへ ➔"):
            if choice == q_item['a']:
                st.session_state.score += 1
            st.session_state.q_index += 1
            st.session_state.answered = False
            
            if st.session_state.q_index >= len(q_list):
                st.session_state.page = "result"
            st.rerun()

# リザルト画面
elif st.session_state.page == "result":
    st.title("🏁 おしまい！")
    st.header(f"10問中 {st.session_state.score}問 正解したよ！")
    if st.button("トップにもどる"):
        st.session_state.page = "top"
        st.session_state.score = 0
        st.session_state.q_index = 0
        st.rerun()
