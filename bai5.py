import turtle

screen = turtle.Screen()

pen = turtle.Turtle()

pen.speed(1)

pen.pendown()

for i in range(1, 4):
    pen.forward(100)
    pen.left(120)
    pen.forward(100)

turtle.done()
