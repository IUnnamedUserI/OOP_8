#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Решите задачу: напишите программу по следующему описанию.
Нажатие Enter в однострочном текстовом поле приводит к перемещению текста
из него в список (экземпляр Listbox). При двойном клике (<Double-Button-1>)
по элементу-строке списка, она должна копироваться в текстовое поле.
"""

from tkinter import Tk, Entry, Listbox, END


def add_to_list(event=None):
    """Добавляет текст из поля ввода в список."""
    global entry, listbox
    text = entry.get()
    if text:
        listbox.insert(END, text)
        entry.delete(0, END)


def copy_to_entry(event):
    """Копирует выбранный элемент списка в поле ввода."""
    global entry, listbox
    selected_index = listbox.curselection()
    if selected_index:
        text = listbox.get(selected_index)
        entry.delete(0, END)
        entry.insert(0, text)


def main():
    """Основная функция для создания графического интерфейса."""
    global entry, listbox

    root = Tk()
    root.title("Текст и список")
    root.geometry("400x300")

    entry = Entry(root, width=40)
    entry.pack(pady=10)

    entry.bind("<Return>", add_to_list)

    listbox = Listbox(root, width=40)
    listbox.pack(pady=10)

    listbox.bind("<Double-Button-1>", copy_to_entry)

    root.mainloop()


if __name__ == "__main__":
    main()
