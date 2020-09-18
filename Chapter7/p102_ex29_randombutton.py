# 起動するたびに数字ボタンの配置が変わる、使いづらい電卓を作ってみる
import tkinter as tk
import random
# 計算機能のための変数とイベント用の関数定義

# 2項演算のモデル
current_number = 0  # 入力中の数字
first_term = 0  # 第一項
second_term = 0 # 第二項
result = 0  # 結果

calc = 'none'   # 加減乗除の指定

def do_plus():
    "+キーが押されたときの計算動作、第一項の設定と入力中の数字のクリア"
    global current_number
    global first_term
    global calc

    first_term = current_number
    current_number = 0
    calc = 'plus'

def do_minus():
    "-キーが押されたときの計算動作、第一項の設定と入力中の数字のクリア"
    global current_number
    global first_term
    global calc

    first_term = current_number
    current_number = 0
    calc = 'minus'

def do_cross():
    "×キーが押されたときの計算動作、代以降の設定と入力中の数字のクリア"
    global current_number
    global first_term
    global calc

    first_term = current_number
    current_number = 0
    calc = 'cross'

def do_division():
    "÷キーが押されたときの計算動作、第一項の設定と入力中の数字のクリア"
    global current_number
    global first_term
    global calc

    first_term = current_number
    current_number = 0
    calc = 'division'

def do_eq():
    "=キーが押されたときの計算動作、第二項の設定、加算の実施、入力中の数字のクリア"
    global second_term
    global result
    global current_number
    global calc
    second_term = current_number
    # 変数calcに従って四則演算を行う
    if calc == 'plus':
        result = first_term + second_term
    elif calc == 'minus':
        result = first_term - second_term
    elif calc == 'cross':
        result = first_term * second_term
    elif calc == 'division':
        if second_term == 0:
            result = '割る数を0にしないでね'
        else:
            result = first_term // second_term
    current_number = 0

# 数字キーを一括処理する関数
def key(n):
    global current_number
    current_number = current_number * 10 + n
    show_number(current_number)

def clear():    # クリアキーの処理
    global current_number
    current_number = 0
    show_number(current_number)

def plus(): # +キーの処理
    do_plus()
    show_number(current_number)

def minus():    # -キーの処理
    do_minus()
    show_number(current_number)

def cross():    # ×キーの処理
    do_cross()
    show_number(current_number)

def division(): # ÷キーの処理
    do_division()
    show_number(current_number)

def eq():   # =キーの処理
    do_eq()
    show_number(result)

def show_number(num):   # 数値をエントリーに表示する関数
    e.delete(0,tk.END)
    e.insert(0,str(num))

# tkinterでの画面の構成

root = tk.Tk()  # Tk()でウインドウ作成
f = tk.Frame(root,bg ='#ffffc0')  # Frameコンテナ作成
f.grid()    # Frameを割り付け

# ウィジェットの作成
b1 = tk.Button(f,text='1',command=lambda:key(1),bg ='#ffffff',width=2,font=('Helvetica',14))
b2 = tk.Button(f,text='2',command=lambda:key(2),bg ='#ffffff',width=2,font=('Helvetica',14))
b3 = tk.Button(f,text='3',command=lambda:key(3),bg ='#ffffff',width=2,font=('Helvetica',14))
b4 = tk.Button(f,text='4',command=lambda:key(4),bg ='#ffffff',width=2,font=('Helvetica',14))
b5 = tk.Button(f,text='5',command=lambda:key(5),bg ='#ffffff',width=2,font=('Helvetica',14))
b6 = tk.Button(f,text='6',command=lambda:key(6),bg ='#ffffff',width=2,font=('Helvetica',14))
b7 = tk.Button(f,text='7',command=lambda:key(7),bg ='#ffffff',width=2,font=('Helvetica',14))
b8 = tk.Button(f,text='8',command=lambda:key(8),bg ='#ffffff',width=2,font=('Helvetica',14))
b9 = tk.Button(f,text='9',command=lambda:key(9),bg ='#ffffff',width=2,font=('Helvetica',14))
b0 = tk.Button(f,text='0',command=lambda:key(0),bg ='#ffffff',width=2,font=('Helvetica',14))
bc = tk.Button(f,text='C', command=clear,bg ='#ff0000',width=2,font=('Helvetica',14))
bp = tk.Button(f,text='+', command=plus,bg ='#00ff00',width=2,font=('Helvetica',14))
bm = tk.Button(f,text='-', command=minus,bg ='#00ff00',width=2,font=('Helvetica',14))
bcr = tk.Button(f,text='×', command=cross,bg ='#00ff00',width=2,font=('Helvetica',14))
bd = tk.Button(f,text='÷', command=division,bg ='#00ff00',width=2,font=('Helvetica',14))
be = tk.Button(f,text='=', command=eq,bg ='#00ff00',width=2,font=('Helvetica',14))

# ランダム表示のために数字ボタンオブジェクトをリストにする
list = [b1, b2, b3, b4, b5, b6,b7,b8,b9,b0]
randlist = random.sample(list, 10)
# Grid型ジオメトリマネージャによるウィジェットの割り付け
# Grid位置を指定してボタンをFrameに割り付け
randlist[0].grid(row=3, column=0)
randlist[1].grid(row=3, column=1)
randlist[2].grid(row=3, column=2)
randlist[3].grid(row=2, column=0)
randlist[4].grid(row=2, column=1)
randlist[5].grid(row=2, column=2)
randlist[6].grid(row=1, column=0)
randlist[7].grid(row=1, column=1)
randlist[8].grid(row=1, column=2)
randlist[9].grid(row=4, column=1)
bc.grid(row=1, column=3)
be.grid(row=4, column=3)
bp.grid(row=4, column=0)
bm.grid(row=4, column=2)
bcr.grid(row=2, column=3)
bd.grid(row=3, column=3)

# 文字入力用のEntryウィジェットを数値表示用に生成、横長に割り付け
# 数値を表示するウィジェット
e = tk.Entry(f,font=('Helvetica',14))
e.grid(row=0,column=0,columnspan=4)
clear()

# ここからGUIがスタート
root.mainloop() # mainloopメソッドでGUIの処理に移る
