import turtle


def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            # Рекурсія
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)


def main():
    screen = turtle.Screen()
    screen.title("Сніжинка Коха")

    t = turtle.Turtle()
    t.speed(0)

    order = 2
    size = 300

    # Створення сніжинки Коха
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()
    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120)
        
    screen.mainloop()


if __name__ == "__main__":
    main()