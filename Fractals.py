import turtle


def circle():
    turtle.Screen().setup(400, 300)
    for x in list(range(50, 1, -10)):
        for i in list(range(4)):
            turtle.circle(x)
            turtle.left(90)


turtle.speed(0)
turtle.clear()
circle()


def linear():
    turtle.hideturtle()
    turtle.Screen().setup(800, 600)
    for x in list(range(20, 1, -2)):
        for i in list(range(4)):
            for i in list(range(4)):
                turtle.forward(x)
                turtle.left(90)
            turtle.left(270)


turtle.speed(0)
turtle.clear()
linear()


def linear():
    turtle.hideturtle()
    turtle.speed(200)
    turtle.Screen().setup(800, 800)
    turtle.goto(0, 0)
    for x in list(range(80, 1, -2)):
        for i in list(range(4)):
            turtle.forward(x)
            turtle.right(45)
            turtle.forward(x)
            turtle.left(135)
            turtle.forward(x)
            turtle.right(45)


turtle.speed(0)
turtle.clear()
linear()


def linear(count):
    for x in list(range(count)):
        turtle.hideturtle()
        turtle.Screen().setup(800, 800)
        for x in list(range(80, 1, -2)):
            for i in list(range(4)):
                turtle.forward(x)
                turtle.right(45)
                turtle.forward(x)
                turtle.right(-90)
                turtle.forward(x)
                turtle.right(45)
                turtle.forward(x)
                turtle.right(120)
        turtle.goto([-120, 100])
        turtle.right(-60)


count = 6
turtle.speed(0)
turtle.goto([-120, 100])
turtle.clear()
linear(count)