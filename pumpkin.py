import turtle
t = turtle.Turtle()
t.speed(5)

def drawcircle(x):
    t.color("orange")
    t.penup()
    t.goto(x,-50)
    t.pendown()
    t.begin_fill()
    t.circle(70)
    t.end_fill()

drawcircle(20)
drawcircle(-20)

def drawtriangle(x,y):
    t.color("yellow")
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    for i in range(3):
        t.forward(36)
        t.left(360/3)
    t.end_fill()

drawtriangle(20,25)
drawtriangle(-55,25)
drawtriangle(-18, 0)
#Programmed By Wazz
#18.03.22

