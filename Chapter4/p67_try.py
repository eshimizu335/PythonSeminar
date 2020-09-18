# 平方根を求めるプログラム
# 平方根を求める数xを端末から入力
while True:
    x = input("平方根を求めたい数を入力 ")
    if x == "end":  # endと入力されたら終了する
        break
    try:
        x = float(x)
    except ValueError:  # ValueErrorへの対応
        print(x, "は数値に変換できません")
        continue
    except: # その他のエラーへの対応
        print("予期していないエラーです")
        exit()
    if (x<=0):  # 正の値であることの検査
        print(x,"は正の数値ではありません")
        continue
# 正しい入力が得られたときの処理
    rnew = x
    diff = rnew - x / rnew  # 2つの近似値(xとx/x)の差をとる
    diff = abs(diff)    # 近似値の差の絶対値を求める
    while (diff/x > 1.0E-6):  # 相対精度で差が10のマイナス6乗より大きければ繰り返す
        r1 = rnew
        r2 = x / r1
        rnew = (r1 + r2) / 2
        print(r1, rnew, r2)
        diff = r1 - r2
        diff = abs(diff)
    break
