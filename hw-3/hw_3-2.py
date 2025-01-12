import turtle


def draw_koch_line(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            draw_koch_line(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order, size=300):

    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    for _ in range(3):
        draw_koch_line(t, order, size)
        t.right(120)  #

    window.mainloop()


draw_koch_snowflake(order=4, size=300)
