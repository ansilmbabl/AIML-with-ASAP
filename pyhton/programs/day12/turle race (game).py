#turle race (game)

import turtle
import random

w=turtle.Screen()
w.bgcolor("light green")

##finishing line
p=turtle.Turtle()
p.penup()
p.goto(300,200)
p.pendown()
p.rt(90)
#or
#p.setheading(270)
p.pensize(5)
for i in range(20):
    p.pencolor("black")
    p.fd(10)
    p.pencolor("white")
    p.fd(10)
p.hideturtle()

##participants
#player 1
tim=turtle.Turtle("turtle")
tim.color("red")
tim.shapesize(2)
tim.penup()
tim.goto(-300,120)

#player 2
tom=turtle.Turtle("turtle")
tom.color("blue")
tom.shapesize(2)
tom.penup()
tom.goto(-300,0)

#player 3
tem=turtle.Turtle("turtle")
tem.color("violet")
tem.shapesize(2)
tem.penup()
tem.goto(-300,-120)

    
##racing
while(True):
    if tim.xcor()>=p.xcor():
        tim.write("tim has won",font=("Arial",30))
        break
    elif tom.xcor()>=p.xcor():
        tom.write("tom has won",font=("Arial",30))
        break
    elif tem.xcor()>=p.xcor():
        tem.write("tem has won",font=("Arial",30))
        break
    else:
        tim.fd(random.randint(1,5))
        tom.fd(random.randint(1,5))
        tem.fd(random.randint(1,5))
