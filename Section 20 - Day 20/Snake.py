# Snake Game

from turtle import Turtle, Screen
import time
import random

# ===================== Snake =====================
class Snake:
    def __init__(self):
        self.segments = []
        self.colors = ["white", "cyan", "yellow", "magenta", "green"]
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        positions = [(0, 0), (-20, 0), (-40, 0)]
        for pos in positions:
            self.add_segment(pos)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color(random.choice(self.colors))
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

# ===================== Food =====================
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.speed("fastest")
        self.color("red")
        self.refresh()

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)

# ===================== PowerUp =====================
class PowerUp(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.speed("fastest")
        self.color(random.choice(["blue", "orange", "purple"]))
        self.active = False
        self.goto(1000, 1000)  # start off screen

    def spawn(self):
        if not self.active:
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            self.goto(x, y)
            self.active = True

    def deactivate(self):
        self.goto(1000, 1000)
        self.active = False

# ===================== Obstacles =====================
class Obstacle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("grey")
        self.penup()
        self.speed("fastest")
        self.goto(1000, 1000)  # off screen initially

    def spawn(self):
        x = random.randint(-260, 260)
        y = random.randint(-260, 260)
        self.goto(x, y)

# ===================== Scoreboard =====================
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 3
        self.level = 1
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f"Score: {self.score}  Lives: {self.lives}  Level: {self.level}",
                   align="center", font=("Arial", 18, "normal"))

    def increase_score(self):
        self.score += 1
        if self.score % 5 == 0:
            self.level += 1
        self.update_board()

    def lose_life(self):
        self.lives -= 1
        self.update_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "bold"))

# ===================== Game Setup =====================
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Ultimate Snake Game 🐍")
screen.tracer(0)

snake = Snake()
food = Food()
powerup = PowerUp()
obstacles = [Obstacle() for _ in range(5)]
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_speed = 0.12
game_is_on = True
powerup_timer = 0

# ===================== Game Loop =====================
while game_is_on:
    screen.update()
    time.sleep(game_speed)

    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        # Randomly spawn powerup
        if random.randint(1, 5) == 3:
            powerup.spawn()

    # Collision with powerup
    if powerup.active and snake.head.distance(powerup) < 15:
        effect = random.choice(["speed", "slow", "shrink"])
        if effect == "speed":
            game_speed = max(game_speed - 0.03, 0.05)
        elif effect == "slow":
            game_speed += 0.05
        elif effect == "shrink" and len(snake.segments) > 3:
            segment_to_remove = snake.segments.pop()
            segment_to_remove.goto(1000, 1000)
        powerup.deactivate()

    # Collision with walls
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        scoreboard.lose_life()
        if scoreboard.lives > 0:
            snake.reset()
        else:
            scoreboard.game_over()
            game_is_on = False

    # Collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.lose_life()
            if scoreboard.lives > 0:
                snake.reset()
            else:
                scoreboard.game_over()
                game_is_on = False

    # Spawn obstacles every level
    if scoreboard.level > 1:
        for obs in obstacles:
            if obs.xcor() > 900:  # off screen
                obs.spawn()
            # Collision with obstacles
            if snake.head.distance(obs) < 15:
                scoreboard.lose_life()
                if scoreboard.lives > 0:
                    snake.reset()
                else:
                    scoreboard.game_over()
                    game_is_on = False

screen.exitonclick()