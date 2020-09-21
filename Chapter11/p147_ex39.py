# のこぎり波の三角関数の和での近似
import tkinter as tk
import tkinter.filedialog
import math

# tikinterのfiledialogだけを利用する例
# rootウィンドウはwithdrow()メソッドを読んで隠す
root = tk.Tk()  # tkinterのメインウインドウを作成
root.withdraw() # メインウインドウは使わないので見えなくする
#
# 書き出し用のfiledialogを読んでファイル名を得る
#
filename = tkinter.filedialog.asksaveasfilename()   # asksaveasfilename()メソッドで名前を付けて保存
#
# ファイル名がもらえなければ終了(名前を付けて保存でキャンセルしたときなど)
#
if filename:
    pass
else:
    print("No file specified")
    exit()
#
# 正弦波の重ね合わせで鋸波を近似する
#
# w = sin(t) + sin(2t)/2 + sin(3t)/3 + sin(4t)/4 ...
#
# 2周期分、全体は1000ステップで高調波は5番目まで
#
cycles = 2
steps = 1000
harmonics = 5   # 全部で5項
# ファイルが開けない時のエラー対応

lista = list()
listb = list()
for i in range(steps):
    angle_in_degree = 360 * cycles * i / steps  # 角度を文字列に
    angle = math.radians(angle_in_degree)
    s = str(angle_in_degree)  # 角度
    w = 0
    for i in range(1, harmonics + 1):  # 第一項、第二項までの和、第三項までの和、第四項までの和、第五項までの和を計算
        w += math.sin(angle * (i)) / i
        s = s + ", "+str(w)  # 角度と和で一行を作る。csv形式にするため和wを文字列に変換してsに加える。
    lista.append(s)
    # print(lista)  # Python Shellで結果を確認する。不要であればコメントアウト。

try:
    # ファイルを開く
    with open(filename,'w')as file:
        for i in range(steps):
            file.write(str(lista[i]))  # 書き出し
            file.write("\n")    # 改行
        print("Writing to file " + filename + "is finished")
except IOError:
    print("Unable to open file")