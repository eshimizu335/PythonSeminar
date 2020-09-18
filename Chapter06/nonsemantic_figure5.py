# turtleで無意味図形を作る
from turtle import *
import random

t = Turtle()   # タートルオブジェクトをコンストラクタTurtle()で生成
for i in range(20):
    for h in range(5):
        t.forward(100)
        t.right(random.randint(-90, 180))    # 30度から180度の範囲でランダムにタートルの向きを変える
        p = t.pos()
    t.setpos(p)
t.setpos(0,0)
done()

