import turtle

wn = turtle.Screen()
wn.title("Animasi Kuntul")
wn.bgcolor("skyblue")

burung = turtle.Turtle()
burung.shape("triangle")
burung.color("red")
burung.penup()
burung.speed(1)

def fly_up():
    y = burung.ycor()
    y += 20
    burung.sety(y)

def fly_down():
    y = burung.ycor()
    y -= 20
    burung.sety(y)

wn.listen()
wn.onkey(fly_up, "Up")
wn.onkey(fly_down, "Down")

while True:
    burung.forward(2)
    if burung.xcor() > 400:
        burung.goto(-400, burung.ycor())

wn.mainloop()