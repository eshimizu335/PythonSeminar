# turtleで星形を描く
from turtle import *
n = 5
for i in range(n):
    x = 360/n
    forward(100)
    left(x)
done()