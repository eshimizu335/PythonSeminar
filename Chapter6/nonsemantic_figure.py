# turtleで無意味図形を作る
from turtle import *
import random

t1 = Turtle()   # タートル１号オブジェクトをコンストラクタTurtle()で生成
t2 = Turtle()   # タートル２号オブジェクトをコンストラクタTurtle()で生成
t3 = Turtle()   # タートル３号オブジェクトをコンストラクタTurtle()で生成

t1.color('red')
t2.color('blue')
t3.color('green')

x = random.randint(-150,150)
y = random.randint(-100, 100)
z = random.randint(-50,50)
c = random.randint(7,15) # turtleを何回動かすか指定

for i in range(c):
    t1.right(random.randint(1,180))    # 1度から180度の範囲でランダムに１号の向きを変える
    t2.right(random.randint(1,180))    # 1度から180度の範囲でランダムに２号の向きを変える
    t3.right(random.randint(1,180))    # 1度から180度の範囲でランダムに３号の向きを変える
    t1.forward(x)
    t2.forward(y)
    t3.forward(z)
    # タートルの位置が原点から一定の距離を超えれば戻る
    if(t1.position()[0]**2+position()[1]**2>50**2):
        t1.forward(-10)
    if (t2.position()[0] ** 2 + position()[1] ** 2 > 200 ** 2):
        t2.forward(-10)
    if (t3.position()[0] ** 2 + position()[1] ** 2 > 200 ** 2):
        t3.forward(-10)
done()

