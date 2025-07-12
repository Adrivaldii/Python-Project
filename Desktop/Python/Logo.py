import turtle

screen = turtle.Screen()
pen = turtle.Turtle()

# huruf A
def draw_A():
    pen.penup()
    pen.goto(-100, 0)
    pen.pendown()
    pen.left(75)
    pen.forward(100)
    pen.right(150)
    pen.forward(100)
    pen.backward(50)
    pen.right(105)
    pen.forward(26)

# huruf D
def draw_D():
    pen.penup()
    pen.goto(-50, 0)
    pen.pendown()
    pen.setheading(90)
    pen.forward(100)
    pen.right(90)
    pen.circle(-50, 180)

# huruf E
def draw_E():
    pen.penup()
    pen.goto(50, 0)
    pen.pendown()
    pen.setheading(0)
    pen.forward(60)
    pen.penup()
    pen.goto(50, 50)
    pen.pendown()
    pen.forward(50)
    pen.penup()
    pen.goto(50, 100)
    pen.pendown()
    pen.forward(60)

draw_A()
draw_D()
draw_E()

pen.hideturtle()
screen.mainloop()