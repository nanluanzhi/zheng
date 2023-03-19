import turtle

# 设置画笔
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# 画心形


def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)


t.color('red', 'pink')
t.begin_fill()
t.left(140)
t.forward(111.65)
curve()

t.left(120)
curve()
t.forward(111.65)
t.end_fill()

# 写信息
t.penup()
t.goto(0, 50)
t.color('black')
t.write("我爱你", align="center", font=("Courier", 24, "normal"))

turtle.done()
