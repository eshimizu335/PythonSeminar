import tkinter as tk

class Dentaku():
    def __init__(self): # 初期化メソッド
        self.current_number = 0
        self.first_term = 0
        self.second_term = 0
        self.result = 0
        self_operation ="+"

    def do_operation(self): # 計算を実行するメソッド
        if self.operation == "+":
            self.result = self.first_term + self.second_term
        elif self.operation == "-":
            self.result = self.first_term - self.second_term
        elif self.operation == "×":
            self.result = self.first_term*self.second_term
        elif self.operation == "÷":
            if self.second_term == 0:
                self.result = '割る数を0にしないでね'
            else:
                self.result = self.first_term//self.second_term

# ここからメインプログラム
dentaku = Dentaku() # オブジェクトの生成
while True:
    f = int(input("First term"))
    dentaku.first_term = f
    o = input("Operation")
    dentaku.operation=o
    s = int(input("Second term"))
    dentaku.second_term = s
    dentaku.do_operation()
    r = dentaku.result
    print("Result", r)


