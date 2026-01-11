import turtle

t = turtle.Turtle()
t.speed(5)
t.color("blue")
t.pensize(3)

for i in range(4):
    t.forward(150)
    t.right(90)

turtle.done()