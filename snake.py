import turtle
import random

# Game Initialization
window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Game Functions
def randomYCoor():
    return random.randrange(-300, 300, 10)
def randomXCoor():
    return random.randrange(-400, 400, 10)
def snake_up():
    y = snake.ycor()
    y += 20
    snake.sety(y)

def snake_down():
    y = snake.ycor()
    y += -20
    snake.sety(y)

def snake_right():
    x = snake.xcor()
    x += 20
    snake.setx(x)

def snake_left():
    x = snake.xcor()
    x += -20
    snake.setx(x)

# Snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("orange")
snake.shapesize(stretch_len= 1, stretch_wid= 1)
snake.penup()
snake.goto(0,0)
snake.dx = 2
snake.dy = 2

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.shapesize(stretch_wid= 0.5, stretch_len= 0.5)
food.penup()
food.goto(randomXCoor(), randomYCoor())
print(food.ycor(), food.xcor())

# Keyboard Binding
window.listen()
window.onkeypress(snake_up, "w")
window.onkeypress(snake_down, "s")
window.onkeypress(snake_right, "d")
window.onkeypress(snake_left, "a")

# Game Main Loop
while True:
    window.update()

    # Border Collision
    if snake.ycor() > 290:
        snake.sety(290)

    if snake.ycor() < -280:
        snake.sety(-280)

    if snake.xcor() > 380:
        snake.setx(380)

    if snake.xcor() < -390:
        snake.setx(-390)

    # Snake Collision