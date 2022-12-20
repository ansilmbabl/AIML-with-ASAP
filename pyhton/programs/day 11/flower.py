##flower shapes

import turtle
import random

w=turtle.Screen()
p=turtle.Turtle()
p.speed(500)

colors=["violet","indigo","green","blue","yellow","orange","red"]

##simple flower
for i in range(4):
    p.fillcolor("yellow")
    p.begin_fill()
    p.circle(100)
    p.end_fill()
    p.lt(45)
    p.fillcolor("light yellow")
    p.begin_fill()
    p.circle(100)
    p.end_fill()
    p.lt(45)
    

p.goto(p.xcor(),p.ycor()-10)
p.fillcolor("violet")
p.begin_fill()
p.circle(20)
p.end_fill()

## spiral flower
for i in range(500):
    p.pencolor(random.choice(colors))
    p.fd(i+2)
    p.lt(91)
