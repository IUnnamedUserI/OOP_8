#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
В данной программе создается анимация круга, который движется от левой границы
холста до правой. Выражение c.coords(ball) возвращает список текущих координат
объекта (в данном случае это ball). Третий элемент списка соответствует его
второй координате x. Метод after вызывает функцию, переданную вторым
аргументом, через количество миллисекунд, указанных первым аргументом. Изучите
приведенную программу и самостоятельно запрограммируйте постепенное движение
фигуры в ту точку холста, где пользователь кликает левой кнопкой мыши.
Координаты события хранятся в его атрибутах x и y (event.x, event.y).
"""

from tkinter import Tk, Canvas


def on_click(event):
    """Обрабатывает клик мыши и запоминает координаты цели."""
    global target_x, target_y
    target_x, target_y = event.x, event.y
    move_towards_target()


def move_towards_target():
    """Плавно перемещает фигуру к целевой точке."""
    global target_x, target_y

    current_x1, current_y1, current_x2, current_y2 = c.coords(ball)
    current_x = (current_x1 + current_x2) / 2
    current_y = (current_y1 + current_y2) / 2

    dx = target_x - current_x
    dy = target_y - current_y

    if abs(dx) > 1 or abs(dy) > 1:
        c.move(ball, dx * 0.1, dy * 0.1)
        root.after(10, move_towards_target)


root = Tk()
root.title("Движение к клику")

c = Canvas(root, width=300, height=200, bg="white")
c.pack()

ball = c.create_oval(0, 100, 40, 140, fill='green')

target_x, target_y = 0, 0

c.bind("<Button-1>", on_click)

root.mainloop()
