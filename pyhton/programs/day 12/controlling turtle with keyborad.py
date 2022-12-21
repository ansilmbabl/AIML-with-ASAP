## controlling turtle with keyborad

import turtle
import random
w=turtle.Screen()
p=turtle.Turtle("turtle")

color=["red","blue","green","yellow"]

def up():
    p.setheading(90)
    p.fd(50)

def down():
    p.setheading(270)
    p.fd(50)

def right():
    p.setheading(0)
    p.fd(50)

def left():
    p.setheading(180)
    p.fd(50)

def colch():
    p.color(random.choice(color))


w.listen()
w.onkeypress(up,"Up")
w.onkeypress(down,"Down")
w.onkeypress(right,"Right")
w.onkeypress(left,"Left")
w.onkeypress(colch,"a")

turtle.mainloop()
