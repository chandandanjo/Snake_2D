import turtle
import random
import time


class Game:
    def __init__(self):
        # Main Game Window
        self.wn = turtle.Screen()
        self.wn.title("Pong")
        self.wn.bgcolor("black")
        self.wn.setup(width=800, height=600)
        self.wn.tracer(0)
        self.wn.listen()

        # Score
        self.score = 0
        self.scores = turtle.Turtle()
        self.scores.speed(0)
        self.scores.color("white")
        self.scores.penup()
        self.scores.hideturtle()
        self.scores.goto(0, 250)
        self.scores.write("Score :  {}".format(self.score), align="center", font=("canary", 24, "bold"))

        # Time Delay
        self.delay = 0.1


class Snake:
    def __init__(self):
        # Snake Head
        self.head = turtle.Turtle()
        self.head.color("white")
        self.head.speed(0)
        self.head.penup()
        self.head.shape("square")
        self.head.goto(0, 0)
        self.head.direction = "stop"

        # Body of Snake
        self.segments = []

    # Movement of Snake
    def go_up(self):
        if self.head.direction != "down":
            self.head.direction = "up"

    def go_down(self):
        if self.head.direction != "up":
            self.head.direction = "down"

    def go_left(self):
        if self.head.direction != "right":
            self.head.direction = "left"

    def go_right(self):
        if self.head.direction != "left":
            self.head.direction = "right"

    def head_move(self):
        if self.head.direction == "up":
            y_cor = self.head.ycor()
            self.head.sety(y_cor + 20)
        if self.head.direction == "down":
            y_cor = self.head.ycor()
            self.head.sety(y_cor - 20)
        if self.head.direction == "left":
            x_cor = self.head.xcor()
            self.head.setx(x_cor - 20)
        if self.head.direction == "right":
            x_cor = self.head.xcor()
            self.head.setx(x_cor + 20)


class Food:
    def __init__(self):
        self.food = turtle.Turtle()
        self.food.color("red")
        self.food.speed(0)
        self.food.penup()
        self.shapes = ["square", "circle", "triangle"]
        self.food.shape(random.choice(self.shapes))
        self.food.goto(0, 100)

    def food_move(self):
        self.food.shape(random.choice(self.shapes))
        self.food.goto(random.randint(-350, 350), random.randint(-250, 250))


# Instantiating Classes
Game = Game()
Snake = Snake()
Food = Food()

# Keybinding Snake Movement
Game.wn.onkeypress(Snake.go_up, "w")
Game.wn.onkeypress(Snake.go_left, "a")
Game.wn.onkeypress(Snake.go_down, "s")
Game.wn.onkeypress(Snake.go_right, "d")

# Main Game Loop
while True:
    Game.wn.update()

    # Boundary Defining
    if Snake.head.xcor() < -380:
        Snake.head.setx(380)
    if Snake.head.xcor() > 380:
        Snake.head.setx(-380)
    if Snake.head.ycor() < -280:
        Snake.head.sety(280)
    if Snake.head.ycor() > 280:
        Snake.head.sety(-280)

    # Snake Head & Food collision
    if Snake.head.distance(Food.food) < 20:
        Food.food_move()
        Game.score += 1
        Game.scores.clear()
        Game.scores.write("Score :  {}".format(Game.score), align="center", font=("canary", 24, "bold"))
        # Creating & Adding New Segments
        new_segment = turtle.Turtle()
        new_segment.color("yellow")
        new_segment.shape("square")
        new_segment.speed(0)
        new_segment.penup()
        Snake.segments.append(new_segment)
        Game.delay -= 0.001

    # Snake Head Collision With Body Segments
    for segment in Snake.segments:
        if Snake.head.distance(segment) < 20:
            time.sleep(1)
            Snake.head.goto(0, 0)
            Snake.head.direction = "stop"
            for segments in Snake.segments:
                segments.goto(1000, 1000)
            Snake.segments.clear()
            Game.score = 0
            Game.scores.clear()
            Game.scores.write("Score :  {}".format(Game.score), align="center", font=("canary", 24, "bold"))

    # Trailing effect of Snake Body Segments
    for index in range(len(Snake.segments) - 1, 0, -1):
        x = Snake.segments[index - 1].xcor()
        y = Snake.segments[index - 1].ycor()
        Snake.segments[index].goto(x, y)
    if len(Snake.segments) > 0:
        x = Snake.head.xcor()
        y = Snake.head.ycor()
        Snake.segments[0].goto(x, y)

    Snake.head_move()
    time.sleep(Game.delay)