#concentric circle

import turtle
n=int(input("number of circles "))

w=turtle.Screen()
p=turtle.Turtle()

r=20
for i in range(n+1):
    p.circle(i*r)
    p.rt(90)
    p.penup()
    p.fd(r)
    p.lt(90)
    p.pendown()
