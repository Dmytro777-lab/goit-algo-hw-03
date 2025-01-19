import turtle
import argparse


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
        t.right(120)

    window.mainloop()


# Парсинг аргументов командной строки
parser = argparse.ArgumentParser(
    description="Візуалізація фракталу 'Сніжинка Коха' з вказаним рівнем рекурсії."
)
parser.add_argument(
    "--order", type=int, default=4, help="Рівень рекурсії (за замовчуванням: 4)"
)
parser.add_argument(
    "--size", type=int, default=300, help="Розмір сніжинки (за замовчуванням: 300)"
)
args = parser.parse_args()

# Вызов функции с переданными параметрами
draw_koch_snowflake(order=args.order, size=args.size)