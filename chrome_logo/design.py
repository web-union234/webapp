from turtle import *     #MODULE USED FOR GRAPHICS
from time import sleep
colormode(255)
bgcolor("black")
shape('arrow')
speed(8)

red=(223,35,35); green=(75,183,75); yellow=(252,210,9); blue=(86,146,195)
radius=120
white=(0,0,0)
seth(-150)
up()
def blue_circle():
    width(3)
    goto(-90,162)
    down()
    color("white")
    begin_fill()
    circle(112)
    color(blue)
    end_fill()
    up()
    goto(-96,30)
    
def red1():
    color("white")
    width(3)
    begin_fill()
    forward(50)
    down()
    right(90)
    circle(-radius,120)
    forward(radius*3** .5)
    left(120)
    circle(2*radius,120)
    left(60)
    color(red)
    forward(radius*3**.5)
    end_fill()

    
def green1():
    left(180)
    color("white")
    forward(radius*3**.5)
    color(green)
    begin_fill()
    color("white")
    left(120)
    circle(2*radius,120)
    left(60)
    forward(radius*3**.5)
    down()
    left(180)
    circle(-radius,120)
    color(green)
    end_fill()
    color("white")
    left(180)
    circle(radius,120)
    left(180)

    
def yellow1():
    color("white")
    begin_fill()
    forward(radius*3**.5)
    end_fill()

    color("white")
    begin_fill()
    left(120)
    circle(2*radius,120)
    left(60)
    forward(radius*3**.5)
    down()
    left(180)
    circle(-radius,120)
    color(yellow)
    end_fill()

    down()
blue_circle()
red1()
green1()
yellow1()




