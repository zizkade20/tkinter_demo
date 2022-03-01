import tkinter as tk
from tkinter import messagebox


def get_user_input():
    user_input = entry1.get()
    messagebox.showinfo("Pozdrav zo slovenska", "ahoj " + user_input + "!")
    entry1.delete(0, tk.END)
    entry1.insert(0, "!")


window = tk.Tk()
window.geometry("500x250")
window.title("Fortnite")


label1 = tk.Label(
    text="Moje aplikace",
    background="black",
    foreground="purple"
)
label1.grid(row=0, column=1, columnspan=2)

entry1 = tk.Entry(
    width=20,

)
entry1.grid(row=1, column=1)
button1 = tk.Button(
    text="Klik!",
    background="green",
    fg="purple",
    width=25,
    height=5,
    command=get_user_input
)

button1.grid(row=1, column=2)


window.mainloop()

"""
from tkinter import *
Tk()

1) create
2) update
3) delete

WIDGETY:
label
entry
button
Text
frame
canvas

-------------------
I 0,O I 0,1 I 0,2 I
I --- I --- I --- I
I 1,0 I 1,1 I 1,2 I
I --- I --- I --- I
I 2,0 I 2,1 I 2,2 I
-------------------
"""