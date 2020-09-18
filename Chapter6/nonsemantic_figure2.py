# turtleで無意味図形を作る
from turtle import *
import random

t = Turtle()   # タートルオブジェクトをコンストラクタTurtle()で生成


for i in range(50):
    t.forward(random.randint(10, 50))
    t.right(random.randint(1, 180))  # 1度から180度の範囲でランダムにタートルの向きを変える
    t.setpos(0,0)

done()

