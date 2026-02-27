import tkinter as tk
from tkinter import messagebox
import random

class NazoNazoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("わくわく！なぞなぞクイズ")
        self.root.geometry("500x700")
        self.root.configure(bg="#fffaf0")

        self.score = 0
        self.q_index = 0
        self.current_cat = []
        
        # なぞなぞデータ（各10問）
        self.quiz_data = {
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

        self.main_frame = tk.Frame(root, bg="#fffaf0")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.show_top()

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_top(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="なぞなぞクイズ！", font=("MS Gothic", 24, "bold"), bg="#fffaf0", fg="#ff6f61").pack(pady=20)
        tk.Label(self.main_frame, text="カテゴリーをえらんでね", font=("MS Gothic", 12), bg="#fffaf0").pack(pady=10)

        # カテゴリーボタンを大きく可愛く
        for cat in self.quiz_data.keys():
            btn = tk.Button(self.main_frame, text=cat, font=("MS Gothic", 16, "bold"),
                            bg="white", fg="#555", bd=5, relief="raised",
                            padx=20, pady=20, cursor="hand2",
                            command=lambda c=cat: self.start_game(c))
            btn.pack(fill="x", pady=10)

    def start_game(self, cat_name):
        self.current_cat = self.quiz_data[cat_name]
        self.q_index = 0
        self.score = 0
        self.show_quiz()

    def show_quiz(self):
        self.clear_frame()
        q_item = self.current_cat[self.q_index]

        tk.Label(self.main_frame, text=f"だい {self.q_index + 1} もん", font=("MS Gothic", 14), bg="#fffaf0").pack()
        
        self.q_label = tk.Label(self.main_frame, text=q_item["q"], font=("MS Gothic", 16, "bold"), 
                                wraplength=400, bg="#fffaf0", pady=20)
        self.q_label.pack()

        self.var = tk.StringVar()
        for choice in q_item["c"]:
            rb = tk.Radiobutton(self.main_frame, text=choice, variable=self.var, value=choice,
                                font=("MS Gothic", 14), bg="#fffaf0", indicatoron=False, 
                                selectcolor="#fff3cd", width=20, pady=10, bd=2, relief="groove")
            rb.pack(pady=5)

        # こたえあわせボタン（赤くて目立つ！）
        self.check_btn = tk.Button(self.main_frame, text="こたえあわせ", font=("MS Gothic", 18, "bold"),
                                   bg="#ff4d4d", fg="white", activebackground="#c0392b",
                                   padx=40, pady=10, bd=4, relief="raised",
                                   command=self.check_answer)
        self.check_btn.pack(pady=30)

        # つぎへボタン（最初は隠す代わりに作成しない、または非表示にする）
        self.next_btn = tk.Button(self.main_frame, text="つぎへ ➔", font=("MS Gothic", 14),
                                  bg="#4CAF50", fg="white", padx=30, pady=10,
                                  command=self.next_question)

    def check_answer(self):
        answer = self.var.get()
        if not answer:
            messagebox.showwarning("おっと！", "こたえをえらんでね！")
            return

        correct_a = self.current_cat[self.q_index]["a"]
        self.check_btn.pack_forget() # こたえあわせボタンを消す

        if answer == correct_a:
            self.score += 1
            self.q_label.config(text="✨ せいかい！ ✨", fg="#ff4d4d")
        else:
            self.q_label.config(text=f"ざんねん！\nこたえは「{correct_a}」", fg="#2196F3")

        self.next_btn.pack(pady=10) # つぎへボタンを出す

    def next_question(self):
        self.q_index += 1
        if self.q_index < len(self.current_cat):
            self.show_quiz()
        else:
            self.show_result()

    def show_result(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="おしまい！", font=("MS Gothic", 24, "bold"), bg="#fffaf0").pack(pady=30)
        tk.Label(self.main_frame, text=f"10もんちゅう {self.score}もん せいかい！", 
                 font=("MS Gothic", 18), bg="#fffaf0").pack(pady=20)
        
        tk.Button(self.main_frame, text="トップにもどる", command=self.show_top,
                  font=("MS Gothic", 14), bg="white", bd=3).pack(pady=30)

if __name__ == "__main__":
    root = tk.Tk()
    app = NazoNazoApp(root)
    root.mainloop()
