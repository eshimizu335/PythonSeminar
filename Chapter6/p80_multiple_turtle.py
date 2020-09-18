# 複数のturtleを動かす
from turtle import *
t1 = Turtle()   # タートル１号オブジェクトをコンストラクタTurtle()で生成
t2 = Turtle()   # タートル２号オブジェクトをコンストラクタTurtle()で生成
# タートルに色をつける
t1.color('red') # colorメソッドでt1オブジェクトを赤にする
t2.color('blue')
for i in range(180):
    t1.forward(5)   # t1は5ステップ前進
    t2.forward(3)   # t2は3ステップ前進
    t1.left(2)  # それぞれ2度回転
    t2.left(2)
done()