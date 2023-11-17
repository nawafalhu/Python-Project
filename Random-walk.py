from turtle import Turtle
import random as r

tim = Turtle()

colors = ["Red", "Blue", "Yellow", "Green", "Pink"]
dir = [0, 90, 180, 270]

tim.pensize(15)
tim.speed("fastest")
for _ in range(100) :
    tim.color(r.choice(colors))
    tim.forward(30)
    tim.setheading(r.choice(dir))
