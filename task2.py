import turtle
import math


def draw_branch(t, length, depth):
    if depth == 0:
        return

    t.speed(0)
    t.forward(length)
    x, y = t.pos()
    angle = t.heading()
    new_length = length * math.sqrt(2) / 2

    t.left(45)
    draw_branch(t, new_length, depth - 1)
    return_to_branch_start(t, x, y, angle)

    t.right(45)
    draw_branch(t, new_length, depth - 1)
    return_to_branch_start(t, x, y, angle)


def return_to_branch_start(t, x, y, angle):
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.pendown()


def build_pythagoras_tree(recursion_depth):
    screen = turtle.Screen()
    screen.setup(width=600, height=600)

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    t.penup()
    t.goto(0, -300)
    t.setheading(90)
    t.pendown()

    draw_branch(t, 100, recursion_depth)
    screen.mainloop()


if __name__ == '__main__':
    depth = input("Enter recursion depth: ")
    build_pythagoras_tree(int(depth))
