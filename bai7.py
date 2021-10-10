import turtle
import math

screen = turtle.Screen()
pen = turtle.Turtle()

pen.pendown()

for i in range(4):
    pen.forward(100)
    pen.left(90)
    pen.forward(100)

pen.penup()

diagonal = math.sqrt(200**2 + 200**2)
distance = (diagonal - 200) / 2
pen.goto(0, -distance)
pen.pendown()
pen.left(45)
for i in range(4):
    pen.forward(200)
    pen.left(90)

pen.penup()

turtle.done()
