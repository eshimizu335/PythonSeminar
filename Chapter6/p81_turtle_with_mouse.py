# マウスクリックに応答するプログラム
from turtle import *

def come(x,y):  # 引数はマウスクリックしたときのカーソルの位置
    (xx,yy) = pos()
    newxy = ((xx+x)/2,(yy+y)/2)
    print(x,y)
    goto(newxy)
onscreenclick(come) # 関数が引数になっている
done()
