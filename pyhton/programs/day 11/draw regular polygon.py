#WAP to draw to take the number of sides from the user and draw regular polygon according to it


import turtle
n=int(input("number of sides of triangle: "))

w=turtle.Screen()
p=turtle.Turtle()

for i in range(n):
    p.fd(100)
    p.lt(360/n)
