from tkinter import *
from tkinter.ttk import Combobox


def clicked():
    global t
    global t_2
    t = num_1.get()
    t_2 = num_2.get()
    try:
        y = float(t)
        x = float(t_2)
        op = cb.get()

        if op == "+":
            plus(x, y)
        elif op == "-":
            minus(x, y)
        elif op == ":" or op == "/":  # Добавил поддержку /
            if y == 0:
                result.config(text="Ошибка: деление на 0")
            else:
                divide(x, y)
        elif op == "*":
            times(x, y)
        else:
            result.config(text="Ошибка")

    except ValueError:
        result.config(text="Ошибка ввода")  # Если введены не числа


# if num_1 != "" and num_2 != "":

wnd = Tk()  # Запуск окна
wnd.title("Calculator")  # Название окна
wnd.geometry("800x600")  # Установка расширения окна
wnd.iconbitmap("icon_512.ico")
wnd.title("Calculator")  # Окно с кнопкой
# wnd.resizable(False, False)
lbl = Label(wnd, text="", font=("Arial Bold", 20))  # Создание объекта метки
lbl.place(x=200, y=200)

t = ""  # Переменная для записи ввода
t_2 = ""

num_1 = Entry(master=wnd, width=7)  # создание объекта для ввода
num_2 = Entry(master=wnd, width=7)

use_case = ["+", "-", ":", "*"]
# Шрифт
fnt = ("Arial", 10, "bold")
# Индекс выбранного в начале пункта
index = 0

# Создание объекта для раскрывающегося списка
cb = Combobox(wnd, state="readonly")
# Содержимое раскрывающегося списка
cb.configure(values=use_case)
# Выбранное в начале значение
cb.current(index)
# Шрифт для этого списка
cb.configure(font=("Arial", 11, "bold"))

cb.bind("<<ComboboxSelected>>")

op = cb.get()

equals = Label(wnd, text="=")
equals.place(x=420, y=250, width=25, height=25)

# Создание объекта для текстовой метки
lbl = Label(master=wnd, text="Num")

# Шрифт для поля ввода
num_1.configure(font=fnt)
num_2.configure(font=fnt)

# Расположение кнопок
num_1.place(x=350, y=250, width=60, height=30)
num_2.place(x=250, y=250, width=60, height=30)
cb.place(x=300, y=250, width=50, height=30)

# Создание объектов кнопок
btn_1 = Button(master=wnd, text="Старт")

# Параметры кнопок
btn_1.configure(font=fnt)
btn_1.configure(command=clicked)

btn_1.place(x=300, y=300)

result = Label(wnd, text="")
result.place(x=440, y=250, width=25, height=25)


def plus(x, y):
    result.config(text=str(x + y))


def minus(x, y):
    result.config(text=str(x - y))


def times(x, y):
    result.config(text=str(x * y))


def divide(x, y):
    result.config(text=str(round(x / y, 2)))


wnd.mainloop()
