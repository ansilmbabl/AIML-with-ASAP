#Star

import turtle

w=turtle.Screen()
p=turtle.Turtle()

#5 limbs
for i in range(5):
    p.fd(100)
    p.rt(144)

#6 limbs
p.circle(100,360,3)
p.penup()
p.goto(0,200)
p.pendown()
p.circle(-100,360,3)
