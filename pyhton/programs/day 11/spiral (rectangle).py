#spiral rectangle

import turtle

w=turtle.Screen()
p=turtle.Turtle()

k=5
for i in range(15):
    p.fd(i*k)
    p.lt(90)
    k+=2
