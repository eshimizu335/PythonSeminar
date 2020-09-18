class Dentaku():
    def __init__(self): # 初期化メソッド
        self.first_term = 0
        self.second_term = 0
        self.result = 0
        self_operation ="+"

    def do_operation(self): # 計算を実行するメソッド
        if self.operation == "+":
            self.result = self.first_term + self.second_term
        elif self.operation == "-":
            self.result = self.first_term - self.second_term

# ここからメインプログラム
dentaku1 = Dentaku() # 複数のオブジェクトを生成
dentaku2 = Dentaku()
while True:
    f1 = int(input("dentaku1_first term"))
    dentaku1.first_term = f1
    o1 = input("Operation")
    dentaku1.operation=o1
    s1 = int(input("dentaku1_second term"))
    dentaku1.second_term = s1
    dentaku1.do_operation()
    r1 = dentaku1.result
    print("dentaku1_result", r1)
    f2 = int(input("dentaku2_first term"))
    dentaku2.first_term = f2
    o2 = input("Operation")
    dentaku2.operation = o2
    s2 = int(input("dentaku2_second term"))
    dentaku2.second_term = s2
    dentaku2.do_operation()
    r2 = dentaku2.result
    print("dentaku2_result", r2)


