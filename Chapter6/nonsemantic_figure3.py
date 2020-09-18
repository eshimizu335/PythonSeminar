# turtleで無意味図形を作る
from turtle import *
import random

t = Turtle()   # タートルオブジェクトをコンストラクタTurtle()で生成
c = random.randint(30,70)   # タートルを何回動かすか

for i in range(c):
    t.forward(random.randint(10, 50))
    t.right(random.randint(30, 180))  # 30度から180度の範囲でランダムにタートルの向きを変える

t.setpos(0,0)

done()

