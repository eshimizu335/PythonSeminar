# 繰り返し平方根を求める関数の実装
def square_root(x):
    '引数xの平方根を求める'
    while True:
        if x == "end":  # endと入力されたら終了する
            break
        try:
            x = float(x)
        except ValueError:  # ValueErrorへの対応
            print(x, "は数値に変換できません")
            x = input("もう一度平方根を求めたい数を入力してください ")
            continue
        except: # その他のエラーへの対応
            print("予期していないエラーです")
            exit()
        if (x<=0):  # 正の値であることの検査
            print(x,"は正の数値ではありません")
            x = input("もう一度平方根を求めたい数を入力してください ")
            continue
    # 正しい入力が得られたときの処理
        rnew = x
        diff = rnew - x / rnew  # 2つの近似値(xとx/x)の差をとる
        diff = abs(diff)    # 近似値の差の絶対値を求める
        while (diff > 1.0E-6):  # 絶対精度で差が10のマイナス6乗より大きければ繰り返す
            r1 = rnew
            r2 = x / r1
            rnew = (r1 + r2) / 2
            print(r1, rnew, r2)
            diff = r1 - r2
            diff = abs(diff)
        break
    return rnew

# ここからメインプログラム
v = input("平方根を求めたい数を入力 ")
r= square_root(v)
print("結果は ", r)

