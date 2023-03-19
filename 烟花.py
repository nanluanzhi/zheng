import turtle
import random

# Set up the turtle screen
# 设置画布
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Fireworks")

# Create a list of colors
# 创建颜色列表
colors = ["red", "orange", "yellow", "green", "blue", "purple", "white"]

# Create a function to draw a firework
# 创建绘制烟花的函数


def draw_firework(x, y):
    # Create a turtle for the firework
    # 创建烟花的海龟
    firework = turtle.Turtle()
    firework.hideturtle()
    firework.speed(0)
    firework.penup()
    firework.goto(x, y)
    firework.pendown()

    # Choose a random color for the firework
    # 为烟花选择随机颜色
    color = random.choice(colors)
    firework.color(color)

    # Draw the firework
    # 绘制烟花
    for i in range(25):
        firework.forward(i * 2)
        firework.right(10)

    # Create a turtle for the explosion
    # 创建爆炸的海龟
    explosion = turtle.Turtle()
    explosion.hideturtle()
    explosion.speed(0)
    explosion.penup()
    explosion.goto(x, y)
    explosion.pendown()

    # Choose a random color for the explosion
    # 为爆炸选择随机颜色
    color = random.choice(colors)
    explosion.color(color)

    # Draw the explosion
    # 绘制爆炸
    for i in range(25):
        explosion.circle(i * 2)

    # Clean up the turtles
    # 清除海龟
    firework.clear()
    explosion.clear()

# Create a function to launch a firework
# 创建发射烟花的函数


def launch_firework():
    # Choose a random position for the firework
    # 为烟花选择随机位置
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)

    # Draw the firework
    # 绘制烟花
    draw_firework(x, y)

    # Schedule the next firework launch
    # 安排下一次发射烟花
    turtle.ontimer(launch_firework, random.randint(500, 2000))


# Launch the first firework
# 发射第一颗烟花
launch_firework()

# Start the turtle screen
turtle.mainloop()
# 开始画布
turtle.mainloop()
