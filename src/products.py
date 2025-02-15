#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите программу, состоящую из двух списков Listbox. В первом будет,
например, перечень товаров, заданный программно. Второй изначально пуст,
пусть это будет перечень покупок. При клике на одну кнопку товар должен
переходить из одного списка в другой. При клике на вторую
кнопку – возвращаться (человек передумал покупать). Предусмотрите возможность
множественного выбора элементов списка и их перемещения.
"""

from tkinter import Tk, Frame, Listbox, Button, END, LEFT, RIGHT, MULTIPLE


def move_to_cart():
    """Перемещает выбранные товары в список покупок."""
    selected_items = listbox1.curselection()

    for index in reversed(selected_items):
        item = listbox1.get(index)
        listbox2.insert(END, item)
        listbox1.delete(index)


def move_to_products():
    """Возвращает выбранные товары в список товаров."""
    selected_items = listbox2.curselection()

    for index in reversed(selected_items):
        item = listbox2.get(index)
        listbox1.insert(END, item)
        listbox2.delete(index)


def main():
    """Основная функция для создания графического интерфейса."""
    global listbox1, listbox2

    root = Tk()
    root.title("Список покупок")
    root.geometry("400x200")

    main_frame = Frame(root)
    main_frame.pack(pady=10)

    listbox1 = Listbox(main_frame, selectmode=MULTIPLE)
    listbox1.pack(side=LEFT, padx=10)

    button_frame = Frame(main_frame)
    button_frame.pack(side=LEFT, padx=10)

    add_button = Button(button_frame, text=">>>", command=move_to_cart)
    add_button.pack(pady=5)

    remove_button = Button(button_frame, text="<<<", command=move_to_products)
    remove_button.pack(pady=5)

    listbox2 = Listbox(main_frame, selectmode=MULTIPLE)
    listbox2.pack(side=RIGHT, padx=10)

    products = ["Яблоки", "Бананы", "Молоко", "Хлеб", "Сыр", "Мясо", "Рыба"]
    for product in products:
        listbox1.insert(END, product)

    root.mainloop()


if __name__ == "__main__":
    main()
