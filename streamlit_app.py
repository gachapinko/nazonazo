import streamlit as st

# ページ設定
st.set_page_config(page_title="わくわく！なぞなぞクイズ", page_icon="💡")

# --- カスタムCSS（UIを可愛く、ボタンを大きく、赤く！） ---
st.markdown("""
    <style>
    /* 全体の背景色 */
    .stApp { background-color: #fffaf0; }
    
    /* コンテナを中央寄せ＆カード風に */
    [data-testid="stVerticalBlock"] > div:has(.quiz-card) {
        background: white;
        padding: 30px;
        border-radius: 30px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
    }

    /* カテゴリーボタン（大きく可愛く） */
    div.stButton > button {
        width: 100%;
        height: 70px;
        font-size: 20px !important;
        font-weight: bold;
        border-radius: 20px;
        border: 3px solid #ffdeeb !important;
        background-color: white !important;
        color: #555 !important;
        margin-bottom: 10px;
    }

    /* こたえあわせボタン（赤くて目立つ） */
    div.stButton > button[kind="primary"] {
        background-color: #ff4d4d !important;
        color: white !important;
        border: none !important;
        height: 60px;
        font-size: 22px !important;
        box-shadow: 0 5px 0 #c0392b;
    }
    
    /* つぎへボタン（緑） */
    div.stButton > button[kind="secondaryFormSubmit"] {
        background-color: #4CAF50 !important;
        color: white !important;
        border: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- クイズデータ（6カテゴリー × 10問） ---
if 'quiz_data' not in st.session_state:
    st.session_state.quiz_data = {
        "たべもの 🍎": [
            {"q": "パンはパンでも、たべられないパンは？", "a": "フライパン", "c": ["メロンパン", "フライパン", "フランスパン"]},
            {"q": "上は火、下は水。これなーんだ？", "a": "おなべ", "c": ["おふろ", "おなべ", "やかん"]},
            {"q": "外は赤くて中は白。シャリシャリなのは？", "a": "りんご", "c": ["りんご", "いちご", "スイカ"]},
            {"q": "むけばむくほど涙が出る野菜は？", "a": "たまねぎ", "c": ["たまねぎ", "ネギ", "レタス"]},
            {"q": "お父さんが嫌いな食べ物は？", "a": "パパイヤ", "c": ["ピーマン", "パパイヤ", "セロリ"]},
            {"q": "黄色い服を脱ぐと白い体が出るのは？", "a": "バナナ", "c": ["レモン", "バナナ", "パイナツ"]},
            {"q": "中身がないのに名前は「中身」なのは？", "a": "ちくわ", "c": ["ドーナツ", "ちくわ", "あめ"]},
            {"q": "空を飛ぶお菓子は？", "a": "スカッシュ", "c": ["スカッシュ", "チョコ", "グミ"]},
            {"q": "お弁当の真ん中の酸っぱいのは？", "a": "うめぼし", "c": ["トマト", "うめぼし", "さくらんぼ"]},
            {"q": "冷たくてコーンに乗っているのは？", "a": "ソフトクリーム", "c": ["ソフトクリーム", "プリン", "かき氷"]}
        ],
        "いきもの 🐘": [
            {"q": "鼻が長くて耳が大きいのは？", "a": "ゾウ", "c": ["キリン", "ゾウ", "カバ"]},
            {"q": "首がとっても長いのは？", "a": "キリン", "c": ["キリン", "シカ", "ヘビ"]},
            {"q": "シマシマ模様のウマは？", "a": "シマウマ", "c": ["シマウマ", "トラ", "ロバ"]},
            {"q": "お腹に袋があるのは？", "a": "カンガルー", "c": ["カンガルー", "パンダ", "コアラ"]},
            {"q": "ひっくり返るとお菓子になるのは？", "a": "カバ", "c": ["カバ", "トラ", "サル"]},
            {"q": "「ワン！」と鳴くのは？", "a": "イヌ", "c": ["ネコ", "イヌ", "タヌキ"]},
            {"q": "夜に「ホーホー」鳴くのは？", "a": "フクロウ", "c": ["ハト", "カラス", "フクロウ"]},
            {"q": "竹を食べる白黒のクマは？", "a": "パンダ", "c": ["パンダ", "シロクマ", "レッサーパンダ"]},
            {"q": "足が速い方の動物は？", "a": "ウサギ", "c": ["ウサギ", "カメ", "アリ"]},
            {"q": "百獣の王は？", "a": "ライオン", "c": ["トラ", "ライオン", "ヒョウ"]}
        ],
        "がっこう 🏫": [
            {"q": "荷物を入れる四角いカバンは？", "a": "ランドセル", "c": ["カバン", "ランドセル", "ふでばこ"]},
            {"q": "字を消してくれるのは？", "a": "けしごむ", "c": ["えんぴつ", "けしごむ", "定規"]},
            {"q": "黒板に字を書くのは？", "a": "チョーク", "c": ["マジック", "チョーク", "えんぴつ"]},
            {"q": "みんなで食べるお昼ごはんは？", "a": "きゅうしょく", "c": ["おべんとう", "きゅうしょく", "おやつ"]},
            {"q": "運動会で一番速く走る競技は？", "a": "リレー", "c": ["リレー", "玉入れ", "綱引き"]},
            {"q": "長さを測る道具は？", "a": "ものさし", "c": ["のり", "ものさし", "はさみ"]},
            {"q": "紙を切る道具は？", "a": "はさみ", "c": ["カッター", "はさみ", "定規"]},
            {"q": "音楽で吹く縦笛は？", "a": "リコーダー", "c": ["リコーダー", "ピアノ", "太鼓"]},
            {"q": "休み時間に遊ぶ広い場所は？", "a": "こうてい", "c": ["こうてい", "きょうしつ", "音楽室"]},
            {"q": "朝のあいさつは？", "a": "おはよう", "c": ["おはよう", "こんにちは", "こんばんは"]}
        ],
        "のりもの 🚗": [
            {"q": "線路の上を走る長い乗り物は？", "a": "でんしゃ", "c": ["バス", "でんしゃ", "ひこうき"]},
            {"q": "空を飛ぶ大きな乗り物は？", "a": "ひこうき", "c": ["ふね", "ひこうき", "ヘリコプター"]},
            {"q": "サイレンを鳴らして火事を消しに行くのは？", "a": "しょうぼうしゃ", "c": ["パトカー", "きゅうきゅうしゃ", "しょうぼうしゃ"]},
            {"q": "海の上をぷかぷか進むのは？", "a": "ふね", "c": ["バス", "ふね", "サメ"]},
            {"q": "病気の人を運ぶ白い車は？", "a": "きゅうきゅうしゃ", "c": ["パトカー", "きゅうきゅうしゃ", "トラック"]},
            {"q": "足でこいで進む2輪車は？", "a": "じてんしゃ", "c": ["じてんしゃ", "バイク", "三輪車"]},
            {"q": "土を掘る大きな腕がついた車は？", "a": "ショベルカー", "c": ["トラック", "ショベルカー", "クレーン車"]},
            {"q": "宇宙まで行く乗り物は？", "a": "ロケット", "c": ["ひこうき", "ロケット", "UFO"]},
            {"q": "たくさんの人を乗せて道路を走るのは？", "a": "バス", "c": ["タクシー", "バス", "でんしゃ"]},
            {"q": "泥棒を追いかける白黒の車は？", "a": "パトカー", "c": ["パトカー", "トラック", "救急車"]}
        ],
        "からだ 💪": [
            {"q": "においをかぐところは？", "a": "はな", "c": ["くち", "はな", "みみ"]},
            {"q": "音をきくところは？", "a": "みみ", "c": ["め", "みみ", "はな"]},
            {"q": "物を見るところは？", "a": "め", "c": ["め", "くち", "まゆげ"]},
            {"q": "ごはんを食べるところは？", "a": "くち", "c": ["くち", "はな", "のど"]},
            {"q": "考えるときに使うところは？", "a": "あたま", "c": ["あたま", "おなか", "せなか"]},
            {"q": "歩くときに使うのは？", "a": "あし", "c": ["て", "あし", "かた"]},
            {"q": "お辞儀をするときに曲げるのは？", "a": "こし", "c": ["ひざ", "こし", "ひじ"]},
            {"q": "手の一番長い指はどれ？", "a": "なかゆび", "c": ["おやゆび", "なかゆび", "こゆび"]},
            {"q": "食べたものが入る袋は？", "a": "おなか", "c": ["あたま", "おなか", "むね"]},
            {"q": "笑うときに動くのは？", "a": "かお", "c": ["かお", "あし", "おしり"]}
        ],
        "うちゅう 🚀": [
            {"q": "夜に光る、一番近い天体は？", "a": "つき", "c": ["たいよう", "つき", "火星"]},
            {"q": "昼間にギラギラ光る大きな星は？", "a": "たいよう", "c": ["たいよう", "つき", "土星"]},
            {"q": "輪っかがあることで有名な惑星は？", "a": "どせい", "c": ["木星", "土星", "火星"]},
            {"q": "私たちが住んでいる星は？", "a": "ちきゅう", "c": ["ちきゅう", "月", "金星"]},
            {"q": "宇宙にいる人のことを何という？", "a": "うちゅうひこうし", "c": ["パイロット", "うちゅうひこうし", "探検家"]},
            {"q": "夜空にキラキラ光る小さな光は？", "a": "ほし", "c": ["ほし", "月", "たいよう"]},
            {"q": "赤くて「火」の名前がついた星は？", "a": "かせい", "c": ["火星", "水星", "木星"]},
            {"q": "宇宙の乗り物が発射される場所は？", "a": "ロケットセンター", "c": ["空港", "港", "ロケットセンター"]},
            {"q": "宇宙にある、重力がとっても強い穴は？", "a": "ブラックホール", "c": ["ブラックホール", "ワームホール", "クレーター"]},
            {"q": "星をみるための大きな道具は？", "a": "てんもんぼうえんきょう", "c": ["顕微鏡", "てんもんぼうえんきょう", "虫眼鏡"]}
        ]
    }

# セッション初期化
if 'page' not in st.session_state:
    st.session_state.page = "top"
    st.session_state.score = 0
    st.session_state.q_index = 0
    st.session_state.answered = False

# --- 描画ロジック ---
with st.container():
    st.markdown('<div class="quiz-card">', unsafe_allow_html=True)
    
    # TOP画面
    if st.session_state.page == "top":
        st.title("💡 なぞなぞクイズ")
        st.write("カテゴリーをえらんでね！")
        # 2列でボタンを配置
        cols = st.columns(2)
        cats = list(st.session_state.quiz_data.keys())
        for i, cat in enumerate(cats):
            if cols[i % 2].button(cat):
                st.session_state.category = cat
                st.session_state.page = "quiz"
                st.rerun()

    # クイズ画面
    elif st.session_state.page == "quiz":
        q_list = st.session_state.quiz_data[st.session_state.category]
        q_item = q_list[st.session_state.q_index]

        st.caption(f"{st.session_state.category} - 第 {st.session_state.q_index + 1} 問")
        st.markdown(f"## {q_item['q']}")

        # 選択肢をラジオボタンで表示
        choice = st.radio("こたえを えらんでね", q_item['c'], key=f"q_{st.session_state.q_index}", index=None)

        st.divider()

        if not st.session_state.answered:
            # 「こたえあわせ」ボタン（赤色：type="primary"）
            if st.button("こたえあわせ", type="primary", use_container_width=True):
                if choice:
                    st.session_state.answered = True
                    st.rerun()
                else:
                    st.warning("どれか選んでね！")
        else:
            # 正誤判定表示
            if choice == q_item['a']:
                st.success(f"✨ せいかい！ ✨")
                st.balloons()
            else:
                st.error(f"ざんねん！ こたえは「{q_item['a']}」でした。")

            # 「つぎへ」ボタン（こたえあわせ後に現れる）
            if st.button("つぎへ ➔", use_container_width=True):
                if choice == q_item['a']:
                    st.session_state.score += 1
                st.session_state.q_index += 1
                st.session_state.answered = False
                if st.session_state.q_index >= 10:
                    st.session_state.page = "result"
                st.rerun()

    # リザルト画面
    elif st.session_state.page == "result":
        st.title("🏁 おしまい！")
        st.header(f"10問中 {st.session_state.score}問 正解！")
        if st.button("トップにもどる", use_container_width=True):
            st.session_state.page = "top"
            st.session_state.score = 0
            st.session_state.q_index = 0
            st.rerun()
            
    st.markdown('</div>', unsafe_allow_html=True)
