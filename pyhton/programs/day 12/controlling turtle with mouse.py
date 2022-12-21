#controlling turtle with mouse

import turtle
import random

w=turtle.Screen()
p=turtle.Turtle()
color=["red","green","blue","yellow"]

def chclr(x,y):
    p.pencolor(random.choice(color))
    p.rt(90)
    p.fd(50)

def printscr(x,y):
    p.penup()
    p.goto(x,y)
    p.pendown()
    p.write("**")

def dragging(x,y):
    p.ondrag(None)
    p.setheading(p.towards(x,y))
    p.goto(x,y)
    p.ondrag(dragging)

w.listen()    
p.onclick(chclr,3)
turtle.onscreenclick(printscr)
p.ondrag(dragging)
turtle.mainloop()
