# range()関数を使ってxの平方根を求める
x = 2
rnew = x
for i in range(10000000): # iを0から9まで変えながら以下の処理を繰り返す
    r1 = rnew
    r2 = x/r1
    rnew = (r1 + r2)/2
print(r1, rnew, r2)