from turtle import *

colormode(255)        #Specifying the color mode

#yellow, red, blue, green color code
y=(255, 212, 0)        
g = (72, 255, 72)
r= (255, 51, 51)
b=(59, 204, 255)
width(2)
up()

goto(-90,-90)
down()

# Base petal

begin_fill()
left(90)
forward(280)
circle(-5,120)
forward(280)
circle(-5,120)
forward(280)
circle(-5,120)
color(y)
end_fill()

right(45)
color("black")

#Green petal
begin_fill()
forward(259)
left(105)
forward(204)
circle(5,120)
forward(280)
color(g)
end_fill()

color("black")

#Red petal
begin_fill()
left(180)
forward(280)
circle(-5,137)
forward(255)
right(102)
forward(200)
circle(-6,120)
forward(280)
color(r)
end_fill()

color("black")

# Blue petal
begin_fill()
circle(-6,137)
forward(197)
right(87)
forward(198)
circle(-6,137)
forward(283)
color(b)
end_fill()
done()



