#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, messagebox

def get_float_from(entry):
    s = entry.get()
    if s == "":
        raise ValueError("Пустое значение")
    return float(s)

def calculate(op):
    try:
        a = get_float_from(entry_a)
    except ValueError:
        messagebox.showerror("Ошибка", "Первое число введено неверно")
        return
    try:
        b = get_float_from(entry_b)
    except ValueError:
        messagebox.showerror("Ошибка", "Второе число введено неверно")
        return

    try:
        if op == "+":
            res = a + b
        elif op == "-":
            res = a - b
        elif op == "*":
            res = a * b
        elif op == "/":
            res = a / b
        else:
            messagebox.showerror("Ошибка", "Неверная операция")
            return
    except Exception as e:
        messagebox.showerror("Ошибка выполнения", str(e))
        return

    result_var.set(str(res))

def on_enter(event):
    # По Enter выполняем сложение как пример
    calculate("+")

def backspace_active():
    w = root.focus_get()
    if isinstance(w, ttk.Entry) or isinstance(w, tk.Entry):
        s = w.get()
        w.delete(0, tk.END)
        w.insert(0, s[:-1])

def clear_all():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    result_var.set("")

root = tk.Tk()
root.title("HexCalc — калькулятор")
root.resizable(False, False)

frm = ttk.Frame(root, padding=10)
frm.grid(row=0, column=0, sticky="NSEW")

ttk.Label(frm, text="Первое число:").grid(row=0, column=0, sticky="W")
entry_a = ttk.Entry(frm, width=25)
entry_a.grid(row=0, column=1, pady=4)
entry_a.focus()

ttk.Label(frm, text="Второе число:").grid(row=1, column=0, sticky="W")
entry_b = ttk.Entry(frm, width=25)
entry_b.grid(row=1, column=1, pady=4)

# Кнопки операций
ops_frame = ttk.Frame(frm)
ops_frame.grid(row=2, column=0, columnspan=2, pady=(6,4))
btn_plus = ttk.Button(ops_frame, text="+", width=6, command=lambda: calculate("+"))
btn_minus = ttk.Button(ops_frame, text="−", width=6, command=lambda: calculate("-"))
btn_mul = ttk.Button(ops_frame, text="×", width=6, command=lambda: calculate("*"))
btn_div = ttk.Button(ops_frame, text="÷", width=6, command=lambda: calculate("/"))
btn_back = ttk.Button(ops_frame, text="⌫", width=6, command=backspace_active)
btn_clr = ttk.Button(ops_frame, text="CLR", width=6, command=clear_all)

btn_plus.grid(row=0, column=0, padx=2)
btn_minus.grid(row=0, column=1, padx=2)
btn_mul.grid(row=0, column=2, padx=2)
btn_div.grid(row=0, column=3, padx=2)
btn_back.grid(row=0, column=4, padx=8)
btn_clr.grid(row=0, column=5, padx=2)

result_var = tk.StringVar()
ttk.Label(frm, text="Результат:").grid(row=3, column=0, sticky="W")
ttk.Entry(frm, textvariable=result_var, width=25, state="readonly").grid(row=3, column=1, pady=4)

root.bind("<Return>", on_enter)
root.bind("<BackSpace>", lambda e: backspace_active())

root.mainloop()
