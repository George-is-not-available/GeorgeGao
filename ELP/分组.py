import tkinter as tk
from tkinter import font
import random

names = {}

def add_name(event):
    name = entry.get()
    if name in names:
        names[name] += 1
    else:
        names[name] = 1
    text.insert(tk.END, name + "\n")
    entry.delete(0, tk.END)

def click():
    if names:
        while True:
            name = random.choice(list(names.keys()))
            if names[name] < 4:
                break
            if names[name] >= 4:
                result_label.config(text="本组已满，请重选", fg='red')
                return
        names[name] += 1

        f = font.Font(size=50, weight='bold', slant='italic')
        result_label['font'] = f
        result_label['fg'] = 'blue'
        result_label.config(text=name)
    else:
        result_label.config(text="请一个响亮的组名", fg='red')

def reset():
    global names
    names = {}
    text.delete(1.0, tk.END)
    result_label.config(text="", fg='black')

root = tk.Tk()
root.title("随机分组小工具")
root.option_add("*Font", "Arial 15")
root.geometry("400x500")  # Set a fixed window size

# Header Label
header_label = tk.Label(root, text="随机分组小工具", font=("Arial", 20, "bold"), pady=10)
header_label.pack()

# Entry for Group Name
label = tk.Label(root, text="请输入车名:", font=("Arial", 14))
label.pack(pady=5)

entry = tk.Entry(root, font=("Arial", 12))
entry.bind("<Return>", add_name)
entry.pack(pady=5)

# Display Entered Names
text = tk.Text(root, font=("Arial", 12), height=5, width=30)
text.pack(pady=10)


# Buttons
button = tk.Button(root, text="随机选组", command=click, font=("Arial", 14), bg='#4CAF50', fg='white')
button.pack(pady=5)

button_reset = tk.Button(root, text='重置', command=reset, font=("Arial", 14), bg='#f44336', fg='white')
button_reset.pack(pady=5)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 18), fg='black')
result_label.pack(pady=10)

root.mainloop()
