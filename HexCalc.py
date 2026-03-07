#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, messagebox

def calculate():
    try:
        a = float(entry_a.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Первое число введено неверно")
        return
    try:
        b = float(entry_b.get())
    except ValueError:
        messagebox.showerror("Ошибка", "Второе число введено неверно")
        return

    op = op_var.get()
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
    calculate()

root = tk.Tk()
root.title("HexCalc — калькулятор")
root.resizable(False, False)

frm = ttk.Frame(root, padding=10)
frm.grid(row=0, column=0, sticky="NSEW")

ttk.Label(frm, text="Первое число:").grid(row=0, column=0, sticky="W")
entry_a = ttk.Entry(frm, width=25)
entry_a.grid(row=0, column=1, pady=4)
entry_a.focus()

ttk.Label(frm, text="Операция:").grid(row=1, column=0, sticky="W")
op_var = tk.StringVar(value="+")
op_menu = ttk.Combobox(frm, textvariable=op_var, values=["+", "-", "*", "/"], state="readonly", width=22)
op_menu.grid(row=1, column=1, pady=4)

ttk.Label(frm, text="Второе число:").grid(row=2, column=0, sticky="W")
entry_b = ttk.Entry(frm, width=25)
entry_b.grid(row=2, column=1, pady=4)

calc_btn = ttk.Button(frm, text="Вычислить", command=calculate)
calc_btn.grid(row=3, column=0, columnspan=2, pady=(6,4))

result_var = tk.StringVar()
ttk.Label(frm, text="Результат:").grid(row=4, column=0, sticky="W")
ttk.Entry(frm, textvariable=result_var, width=25, state="readonly").grid(row=4, column=1, pady=4)

root.bind("<Return>", on_enter)
root.mainloop()
