import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("300x250")
root.resizable(False, False)
font = ("Arial", 14)

# Поле для ввода и отображения текста
entry = tk.Entry(root, justify="right", bd=10, relief="flat")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

#  Функции логики
def on_click(symbol):
    entry.insert(tk.END, symbol)

def clear():
    entry.delete(0, tk.END)
 
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")

#  Список кнопок (текст, строка, колонка)
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

# Создание и размещение кнопок в сетке (grid)
for text, row, col in buttons:
    if text == "=":
        cmd = calculate
    elif text == "C":
        cmd = clear
    else:
        # lambda фиксирует конкретный символ для каждой кнопки
        cmd = lambda val=text: on_click(val)
        
    btn = tk.Button(root, text=text, font=font, command=cmd)
    
    # Кнопку "C" растянем на 4 колонки внизу
    if text == "C":
        btn.grid(row=row, column=col, columnspan=4, sticky="nsew", padx=3, pady=3)
    else:
        btn.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)

# Равномерное распределение строк и колонок по ширине/высоте окна
for i in range(6):
    root.rowconfigure(i, weight=1)
for i in range(4):
    root.columnconfigure(i, weight=1)

root.mainloop()