from turtle import Turtle, Screen
import random

# Setup
tim = Turtle()
screen = Screen()

# -----------------------------
# Original Movement Functions
# -----------------------------
def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# -----------------------------
# Extra Features
# -----------------------------
# Pen colors
colors = ["red", "blue", "green", "purple", "orange", "yellow"]

def change_color():
    tim.color(random.choice(colors))

# Pen size
def thicker():
    tim.pensize(tim.pensize() + 1)

def thinner():
    tim.pensize(max(1, tim.pensize() - 1))

# Speed control
def speed_up():
    tim.speed(min(tim.speed() + 1, 10))  # max speed is 10

def slow_down():
    tim.speed(max(tim.speed() - 1, 1))  # min speed is 1

# -----------------------------
# Key Bindings
# -----------------------------
screen.listen()
# Original controls
screen.onkey(move_forward, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

# Extra controls
screen.onkey(change_color, "p")  # 'p' to change color
screen.onkey(thicker, "+")       # '+' to increase pen size
screen.onkey(thinner, "-")       # '-' to decrease pen size
screen.onkey(speed_up, "Up")     # Arrow Up to speed up
screen.onkey(slow_down, "Down")  # Arrow Down to slow down

# Exit
screen.exitonclick()