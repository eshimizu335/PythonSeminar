# 2つの関数を利用して繰り返し平方根を求めるプログラム
# 端末から正の数値の入力を得る関数
def get_positive_numeral():
    v = input("平方根を求めたい数を入力 ")
    while True:
        try:
            v = float(v)
        except ValueError:  # ValueErrorへの対応
            print(v, "は数値に変換できません")
            v = input("もう一度平方根を求めたい数を入力してください ")
            continue
        except: # その他のエラーへの対応
            print("予期していないエラーです")
            exit()
        if (v<=0):  # 正の値であることの検査
            print(v,"は正の数値ではありません")
            v = input("もう一度平方根を求めたい数を入力してください ")
            continue
        # 正しい入力が得られたときの処理
        return v

# 平方根を求める関数
def square_root(x):
    rnew = x
    diff = rnew - x / rnew  # 2つの近似値(xとx/x)の差をとる
    diff = abs(diff)  # 近似値の差の絶対値を求める
    while (diff > 1.0E-6):  # 絶対精度で差が10のマイナス6乗より大きければ繰り返す
        r1 = rnew
        r2 = x / r1
        rnew = (r1 + r2) / 2
        print(r1, rnew, r2)
        diff = r1 - r2
        diff = abs(diff)
    return rnew

# ここからメインプログラム
a = get_positive_numeral()
b = square_root(a)
print("結果は ", b)