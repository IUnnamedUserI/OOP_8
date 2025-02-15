#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Создайте на холсте изображение домика, солнца и травы. Для создания
травы необходимо использовать цикл.
"""

from tkinter import Tk, Canvas


def main():
    """Основная функция для создания графического интерфейса."""
    root = Tk()
    root.title("Картинка")
    root.geometry("300x350")

    canvas = Canvas(root, bg="white", width=500, height=400)
    canvas.pack()

    canvas.create_rectangle(100, 200, 200, 300, fill="lightblue",
                            outline="lightblue")
    canvas.create_polygon(75, 200, 225, 200, 150, 150, fill="lightblue",
                          outline="lightblue")

    canvas.create_oval(200, 50, 250, 100, fill="orange", outline="orange")

    for i in range(0, 500, 10):
        canvas.create_line(i, 350, i + 10, 320, fill="green", smooth=True)

    root.mainloop()


if __name__ == "__main__":
    main()
