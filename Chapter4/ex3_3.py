# 精度を指定して平方根を求める
# 端末から平方根を求める数値を入力する
x = int(input("平方根を求めたい数を入力 "))
rnew = x
diff = rnew - x/rnew    # 2つの近似値(xとx/x)の差をとる
if (diff<0):    # 絶対値を求めるので負の場合は符号を反転させる
    diff = -diff
while (diff>1.0E-6):    # 差が10のマイナス6乗より大きければ繰り返す
    r1 = rnew
    r2 = x/r1
    rnew = (r1 + r2)/2
    print(r1, rnew, r2)
    diff = r1 - r2
    if (diff<0):
        diff = -diff