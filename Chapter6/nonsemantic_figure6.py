# turtleで無意味図形を作る
from turtle import *
import random

t = Turtle()   # タートルオブジェクトをコンストラクタTurtle()で生成
t.begin_fill()
for i in range(10):
    for h in range(5):
        t.forward(50)
        t.right(random.randint(10, 90))    # 30度から180度の範囲でランダムにタートルの向きを変える
        p = t.pos()
    #t.setpos(p)
t.setpos(0,0)
t.end_fill()
done()

