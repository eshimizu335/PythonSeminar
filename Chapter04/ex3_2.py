# 無限ループ型プログラム
# xの平方根を求める

x = 2
rnew = x
while True: # 無限ループ
    r1 = rnew
    r2 = x/r1
    rnew = (r1 + r2)/2
    print(r1, rnew, r2)
    diff = r1 -r2
    if(diff<0):
        diff = -diff
    if diff<=1.0E-6:    # 条件を満たしたらbreakでループを抜ける
        break