from turtle import *
import random

stop_flag = False   # 実行を停止するためのフラグ

def clicked(x,y):
    global stop_flag
    stop_flag = True

onscreenclick(clicked)

speed(0)
while(not stop_flag):
    left(random.randint(-90,90))    # -90度から90度の範囲でランダムに向きを変える
    forward(10)
    # タートルの位置が原点から一定の距離を超えれば戻る
    if(position()[0]**2+position()[1]**2>200**2):
        forward(-10)
