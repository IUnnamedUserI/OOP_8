#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите программу по описанию. Размеры многострочного текстового поля
определяются значениями, введенными в однострочные текстовые поля. Изменение
размера происходит при нажатии мышью на кнопку, а также при нажатии клавиши
Enter. Цвет фона экземпляра Text светлосерый (lightgrey), когда поле не в
фокусе, и белый, когда имеет фокус. Событие получения фокуса обозначается как
<FocusIn>, потери – как <FocusOut>. Для справки: фокус перемещается по виджетам
при нажатии Tab, Ctrl+Tab, Shift+Tab, а также при клике по ним мышью (к кнопкам
последнее не относится).
"""

from tkinter import Tk, Frame, Label, Entry
from tkinter import Button, Text, messagebox, BOTH, LEFT


def resize_text(event=None):
    """Изменяет размеры текстового поля на основе введенных значений."""
    global width_entry, height_entry, text_field, text_frame

    try:
        width = int(width_entry.get())
        height = int(height_entry.get())

        text_field.config(width=width, height=height)
        text_frame.config(width=width * 10, height=height * 20)
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа!")


def on_focus_in(event):
    """Изменяет цвет фона текстового поля при получении фокуса."""
    global text_field
    text_field.config(bg="white")


def on_focus_out(event):
    """Изменяет цвет фона текстового поля при потере фокуса."""
    global text_field
    text_field.config(bg="lightgrey")


def main():
    """Основная функция для создания графического интерфейса."""
    global width_entry, height_entry, text_field, text_frame

    root = Tk()
    root.title("Изменение размеров текстового поля")
    root.geometry("400x300")

    input_frame = Frame(root)
    input_frame.pack(pady=10)

    width_label = Label(input_frame, text="Ширина:")
    width_label.pack(side=LEFT, padx=5)
    width_entry = Entry(input_frame, width=10)
    width_entry.pack(side=LEFT, padx=5)

    height_label = Label(input_frame, text="Высота:")
    height_label.pack(side=LEFT, padx=5)
    height_entry = Entry(input_frame, width=10)
    height_entry.pack(side=LEFT, padx=5)

    resize_button = Button(root, text="Изменить размер", command=resize_text)
    resize_button.pack(pady=5)

    text_frame = Frame(root)
    text_frame.pack(pady=10)

    text_frame.pack_propagate(False)

    text_field = Text(text_frame, bg="lightgrey")
    text_field.pack(fill=BOTH, expand=True)

    text_field.bind("<FocusIn>", on_focus_in)
    text_field.bind("<FocusOut>", on_focus_out)

    width_entry.bind("<Return>", resize_text)
    height_entry.bind("<Return>", resize_text)

    root.mainloop()


if __name__ == "__main__":
    main()
