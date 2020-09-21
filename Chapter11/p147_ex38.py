# 矩形波の三角関数の和での近似
import tkinter as tk
import tkinter.filedialog
import math

# tikinterのfiledialogだけを利用する例
# rootウィンドウはwithdrow()メソッドを読んで隠す
root = tk.Tk()  # tkinterのメインウインドウを作成
root.withdraw() # メインウインドウは使わないので見えなくする
#
# 書き出しようのfiledialogを読んでファイル名を得る
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
# 正弦波の重ね合わせで矩形波を近似する
#
# w = sin(t) + sin(3t)/3 + sin(5t)/5 + sin(7t)/7 ...
#
# 2周期分、全体は1000ステップで高調波は5番目まで
#
cycles = 2
steps = 1000
harmonics = 5   # 全部で5項
# ファイルが開けない時のエラー対応
try:
    # ファイルを開く
    with open(filename,'w')as file:
        for i in range(steps):
            angle_in_degree = 360*cycles*i/steps    # 角度を文字列に
            angle = math.radians(angle_in_degree)
            s = str(angle_in_degree)    # 角度
            w = 0
            for i in range(1,harmonics*2+1,2):  # 第一項、第二項までの和、第三項までの和、第四項までの和、第五項までの和を計算
                w += math.sin(angle*(i))/i
                s = s+", "+str(w)   # 角度と和で一行を作る。csv形式にするため和wを文字列に変換してsに加える。
            print(s)    # Python Shellで結果を確認する。不要であればコメントアウト。
            file.write(s+"\n")  # 改行を加えて書き出し
        print("Writing to file " + filename + "is finished")
except IOError:
    print("Unable to open file")
