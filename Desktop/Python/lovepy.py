import turtle

window = turtle.Screen()
window.bgcolor("black")

pen = turtle.Turtle()
pen.color("red")
pen.speed(1)

pen.penup()
pen.goto(-100, 0)
pen.pendown()
pen.write("I love Python ()", font=("Arial", 50, "italic"), align="center")

pen.hideturtle()

window.exitonclick()
