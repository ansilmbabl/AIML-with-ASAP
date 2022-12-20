#circles with a common point in contact

import turtle
n=int(input("number of circles "))

w=turtle.Screen()
p=turtle.Turtle()

for i in range(n):
    p.circle(i*10)
