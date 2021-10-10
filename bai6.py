import turtle

screen = turtle.Screen()
pen = turtle.Turtle()

pen.speed(2)
pen.pendown()

for i in range(0, 4):
    pen.forward(100)
    pen.left(90)
    pen.forward(100)

pen.penup()

pen.goto(0, -20)
pen.pendown()
pen.pensize(5)
for i in range(0, 4):
    pen.forward(120)
    pen.left(90)
    pen.forward(120)
pen.penup()

turtle.done()
