#concentric circle with coloring
import random
import turtle
n=int(input("number of circles "))

w=turtle.Screen()
p=turtle.Turtle()


colors=["green","blue","yellow","black","red"]
r=200
for i in range(len(colors)):
    p.fillcolor(random.choice(colors))
    p.begin_fill()
    p.circle(r)
    p.end_fill()
    p.penup()
    p.goto(p.xcor(),p.ycor()+25)
    r-=25
    p.pendown()
