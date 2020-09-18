import tkinter as tk
class Dentaku():
    def __init__(self): # 初期化メソッド
        self.first_term = 0
        self.second_term = 0
        self.result = 0
        self.calc = "none"

    def do_plus(self):
        "+キーが押されたときの計算動作、第一項の設定と入力中の数字のクリア"
        self.first_term = self.current_number
        self.current_number = 0
        self.calc = 'plus'

    def do_minus(self):
        "-キーが押されたときの計算動作、第一項の設定と入力中の数字のクリア"
        self.first_term = self.current_number
        self.current_number = 0
        self.calc = 'minus'

    def do_cross(self):
        "×キーが押されたときの計算動作、代以降の設定と入力中の数字のクリア"
        self.first_term = self.current_number
        self.current_number = 0
        self.calc = 'cross'

    def do_division(self):
        "÷キーが押されたときの計算動作、第一項の設定と入力中の数字のクリア"
        self.first_term = self.current_number
        self.current_number = 0
        self.calc = 'division'

    def do_eq(self):
        "=キーが押されたときの計算動作、第二項の設定、加算の実施、入力中の数字のクリア"
        self.second_term = self.current_number
        # 変数calcに従って四則演算を行う
        if self.calc == 'plus':
            self.result = self.first_term + self.second_term
        elif self.calc == 'minus':
            self.result = self.first_term - self.second_term
        elif self.calc == 'cross':
            self.result = self.first_term * self.second_term
        elif self.calc == 'division':
            if self.second_term == 0:
                self.result = '割る数を0にしないでね'
            else:
                self.result = self.first_term // self.second_term
        self.current_number = 0

    # 数字キーを一括処理する関数
    def key(self,n):
        self.current_number = self.current_number * 10 + n
        self.show_number(self.current_number)

    def clear(self):  # クリアキーの処理
        self.current_number = 0
        self.show_number(self.current_number)

    def plus(self):  # +キーの処理
        self.do_plus()
        self.show_number(self.current_number)

    def minus(self):  # -キーの処理
        self.do_minus()
        self.show_number(self.current_number)

    def cross(self):  # ×キーの処理
        self.do_cross()
        self.show_number(self.current_number)

    def division(self):  # ÷キーの処理
        self.do_division()
        self.show_number(self.current_number)

    def eq(self):  # =キーの処理
        self.do_eq()
        self.show_number(self.result)

    def show_number(self,num):  # 数値をエントリーに表示する関数
        self.e.delete(0, tk.END)
        self.e.insert(0, str(num))

    def gui(self):
        # tkinterでの画面の構成

        self.root = tk.Tk()  # Tk()でウインドウ作成
        self.f = tk.Frame(self.root, bg='#ffffc0')  # Frameコンテナ作成
        self.f.grid()  # Frameを割り付け

        # ウィジェットの作成
        self.b1 = tk.Button(self.f, text='1', command=lambda: self.key(1), bg='#ffffff', width=2, font=('Helvetica', 14))
        self.b2 = tk.Button(self.f, text='2', command=lambda: self.key(2), bg='#ffffff', width=2, font=('Helvetica', 14))
        self.b3 = tk.Button(self.f, text='3', command=lambda: self.key(3), bg='#ffffff', width=2, font=('Helvetica', 14))
        self.b4 = tk.Button(self.f, text='4', command=lambda: self.key(4), bg='#ffffff', width=2, font=('Helvetica', 14))
        self.b5 = tk.Button(self.f, text='5', command=lambda: self.key(5), bg='#ffffff', width=2, font=('Helvetica', 14))
        self.b6 = tk.Button(self.f, text='6', command=lambda: self.key(6), bg='#ffffff', width=2, font=('Helvetica', 14))
        self.b7 = tk.Button(self.f, text='7', command=lambda: self.key(7), bg='#ffffff', width=2, font=('Helvetica', 14))
        self.b8 = tk.Button(self.f, text='8', command=lambda: self.key(8), bg='#ffffff', width=2, font=('Helvetica', 14))
        self.b9 = tk.Button(self.f, text='9', command=lambda: self.key(9), bg='#ffffff', width=2, font=('Helvetica', 14))
        self.b0 = tk.Button(self.f, text='0', command=lambda: self.key(0), bg='#ffffff', width=2, font=('Helvetica', 14))
        self.bc = tk.Button(self.f, text='C', command=self.clear, bg='#ff0000', width=2, font=('Helvetica', 14))
        self.bp = tk.Button(self.f, text='+', command=self.plus, bg='#00ff00', width=2, font=('Helvetica', 14))
        self.bm = tk.Button(self.f, text='-', command=self.minus, bg='#00ff00', width=2, font=('Helvetica', 14))
        self.bcr = tk.Button(self.f, text='×', command=self.cross, bg='#00ff00', width=2, font=('Helvetica', 14))
        self.bd = tk.Button(self.f, text='÷', command=self.division, bg='#00ff00', width=2, font=('Helvetica', 14))
        self.be = tk.Button(self.f, text='=', command=self.eq, bg='#00ff00', width=2, font=('Helvetica', 14))

        # Grid型ジオメトリマネージャによるウィジェットの割り付け
        # Grid位置を指定してボタンをFrameに割り付け
        self.b1.grid(row=3, column=0)
        self.b2.grid(row=3, column=1)
        self.b3.grid(row=3, column=2)
        self.b4.grid(row=2, column=0)
        self.b5.grid(row=2, column=1)
        self.b6.grid(row=2, column=2)
        self.b7.grid(row=1, column=0)
        self.b8.grid(row=1, column=1)
        self.b9.grid(row=1, column=2)
        self.b0.grid(row=4, column=1)
        self.bc.grid(row=1, column=3)
        self.be.grid(row=4, column=3)
        self.bp.grid(row=4, column=0)
        self.bm.grid(row=4, column=2)
        self.bcr.grid(row=2, column=3)
        self.bd.grid(row=3, column=3)

        # 文字入力用のEntryウィジェットを数値表示用に生成、横長に割り付け
        # 数値を表示するウィジェット
        self.e = tk.Entry(self.f, font=('Helvetica', 14))
        self.e.grid(row=0, column=0, columnspan=4)
        self.clear()

        self.root.mainloop()


# ここからメインプログラム
dentaku = Dentaku() # オブジェクトの生成
dentaku.gui()


