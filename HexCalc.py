# HexCalc - Simple calculator
# Copyright (C) 2026 oceantee21
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import tkinter as tk
from tkinter import messagebox
import math

# Цвета (все кнопки цифр/фона кнопок — один тёмно-синий)
BG = "#0b1f2e"        # фон окна
FRAME_BG = "#0e2836"
BTN_BG = "#1f6b8f"    # основной синий (для всех кнопок по просьбе)
BTN_OP_BG = "#165a75" # операции чуть темнее
BTN_EQ_BG = BTN_BG    # равно тот же синий
FG = "#ffffff"

def insert_text(s):
    ent = root.focus_get()
    if isinstance(ent, tk.Entry):
        i = ent.index(tk.INSERT)
        ent.insert(i, s)
    else:
        expr_entry.insert(tk.INSERT, s)

def backspace():
    w = root.focus_get()
    if isinstance(w, tk.Entry):
        i = w.index(tk.INSERT)
        if i > 0:
            w.delete(i-1)
    else:
        i = expr_entry.index(tk.INSERT)
        if i > 0:
            expr_entry.delete(i-1)

def clear_all():
    expr_entry.delete(0, tk.END)
    result_var.set("")

def evaluate():
    expr = expr_entry.get()
    if not expr.strip():
        return
    try:
        safe = expr.replace("×", "*").replace("÷", "/").replace("√", "sqrt")
        def sqrt(x): return math.sqrt(x)
        allowed = {"sqrt": sqrt, "pi": math.pi, "e": math.e}
        res = eval(safe, {"__builtins__": {}}, allowed)
        result_var.set(str(res))
    except Exception as e:
        messagebox.showerror("Ошибка", f"Неправильное выражение:\n{e}")

def press_key(event):
    if event.keysym == "Return":
        evaluate()
    elif event.keysym == "BackSpace":
        backspace()

root = tk.Tk()
root.title("HexCalc — калькулятор")
root.configure(bg=BG)
root.minsize(320, 480)

frm = tk.Frame(root, bg=FRAME_BG, padx=8, pady=8)
frm.pack(fill="both", expand=True, padx=12, pady=12)

expr_entry = tk.Entry(frm, font=("Segoe UI", 20), justify="right", bd=0, relief="flat",
                      insertbackground=FG, bg="#071622", fg=FG)
expr_entry.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=(0,8), ipady=10)
expr_entry.focus()

result_var = tk.StringVar()
result_entry = tk.Entry(frm, textvariable=result_var, font=("Segoe UI", 14),
                        justify="right", bd=0, relief="flat", state="readonly",
                        readonlybackground="#071622", fg="#bfe8ff")
result_entry.grid(row=1, column=0, columnspan=4, sticky="nsew", pady=(0,12), ipady=6)

# сетка: строки 2..7, колонки 0..3
for r in range(2, 8):
    frm.rowconfigure(r, weight=1)
for c in range(4):
    frm.columnconfigure(c, weight=1, uniform="col")

btn_style = {"font": ("Segoe UI", 16), "bd": 0, "fg": FG, "relief": "flat", "activeforeground": FG}

def make_btn(text, row, col, colspan=1, bg=BTN_BG, cmd=None):
    b = tk.Button(frm, text=text, bg=bg, **btn_style, command=(cmd if cmd else lambda t=text: insert_text(t)))
    b.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=4, pady=4)
    return b

# Первая строка функций
make_btn("C", 2, 0, bg=BTN_OP_BG, cmd=clear_all)
make_btn("⌫", 2, 1, bg=BTN_OP_BG, cmd=backspace)
make_btn("(", 2, 2)
make_btn(")", 2, 3)

# Цифры 7 8 9
make_btn("7", 3, 0)
make_btn("8", 3, 1)
make_btn("9", 3, 2)
make_btn("÷", 3, 3, bg=BTN_OP_BG, cmd=lambda: insert_text("÷"))

# Цифры 4 5 6
make_btn("4", 4, 0)
make_btn("5", 4, 1)
make_btn("6", 4, 2)
make_btn("×", 4, 3, bg=BTN_OP_BG, cmd=lambda: insert_text("×"))

# Цифры 1 2 3
make_btn("1", 5, 0)
make_btn("2", 5, 1)
make_btn("3", 5, 2)
make_btn("-", 5, 3, bg=BTN_OP_BG, cmd=lambda: insert_text("-"))

# Ноль, точка, плюс, равно/операции внизу
make_btn("0", 6, 0, colspan=2)  # ноль занимает два столбца (обычно)
make_btn(".", 6, 2)
make_btn("+", 6, 3, bg=BTN_OP_BG, cmd=lambda: insert_text("+"))

# Дополнительные функции: корень, x^2, 1/x, +/- и большая кнопка "="
# Разместим их над цифрами (в первой колонке блоков) или добавим снизу слева — тут добавим в столбец 0..2 верхне-нижне
make_btn("√", 7, 0, bg=BTN_OP_BG, cmd=lambda: insert_text("√("))
make_btn("x²", 7, 1, bg=BTN_OP_BG, cmd=lambda: insert_text("**2"))
make_btn("1/x", 7, 2, bg=BTN_OP_BG, cmd=lambda: insert_text("1/("))
make_btn("=", 7, 3, bg=BTN_EQ_BG, cmd=evaluate)

# Чтобы "=" была крупной и заметной, растянем её по высоте:
frm.rowconfigure(7, weight=1)

# Приведение всех кнопок к единой основной синей палитре, операции — чуть темнее
for w in frm.grid_slaves():
    if isinstance(w, tk.Button):
        txt = w.cget("text")
        if txt in ("÷", "×", "+", "-", "√", "x²", "1/x", "C", "⌫"):
            w.configure(bg=BTN_OP_BG, activebackground="#134956")
        else:
            w.configure(bg=BTN_BG, activebackground="#195f79")

# Стилизация полей
expr_entry.configure(bg="#071622", fg="#e6f7ff")
result_entry.configure(readonlybackground="#071622", fg="#bfe8ff")

# Клавиатурные бинды
root.bind("<Return>", lambda e: evaluate())
root.bind("<BackSpace>", lambda e: backspace())
root.bind("<Key>", press_key)

root.mainloop()