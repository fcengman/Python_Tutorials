# This program draws a design using repeated lines.

import turtle

# Named constants


def draw_spiral_lines():
    START_X = -200
    START_Y = 0
    NUM_LINES = 36
    LINE_LENGTH = 400
    ANGLE = 170
    ANIMATION_SPEED = 0

    turtle.hideturtle()
    turtle.penup()
    turtle.goto(START_X, START_Y)
    turtle.pendown()

    turtle.speed(ANIMATION_SPEED)

    for x in range(NUM_LINES):
        turtle.forward(LINE_LENGTH)
        turtle.left(ANGLE)


def draw_spiral_circles():
    NUM_CIRCLES = 36
    RADIUS = 100
    ANGLE = 10
    ANIMATION_SPEED = 0

    turtle.speed(ANIMATION_SPEED)
    for x in range(NUM_CIRCLES):
        turtle.circle(RADIUS)
        turtle.left(ANGLE)


draw_spiral_lines()
draw_spiral_circles()
turtle.done()
