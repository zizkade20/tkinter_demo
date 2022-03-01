import tkinter as tk

window = tk.Tk()
window.geometry("700x500")
window.title("Fortnite")

button1 = tk.Button(
    text="1",
    background="green",
    fg="purple",
    width=10,
    height=5,
)
button2 = tk.Button(
    text="2",
    background="green",
    fg="purple",
    width=10,
    height=5,
)
button3 = tk.Button(
    text="3",
    background="green",
    fg="purple",
    width=10,
    height=5,
)
button4 = tk.Button(
    text="4",
    background="green",
    fg="purple",
    width=10,
    height=5,
)
button5 = tk.Button(
    text="5",
    background="green",
    fg="purple",
    width=10,
    height=5,
)
button6 = tk.Button(
    text="6",
    background="green",
    fg="purple",
    width=10,
    height=5,
)
button7 = tk.Button(
    text="7",
    background="green",
    fg="purple",
    width=10,
    height=5,
)
button8 = tk.Button(
    text="8",
    background="green",
    fg="purple",
    width=10,
    height=5,
)
button9 = tk.Button(
    text="9",
    background="green",
    fg="purple",
    width=10,
    height=5,
)
button10 = tk.Button(
    text="0",
    background="green",
    fg="purple",
    width=10,
    height=5,
)
button11 = tk.Button(
    text="+",
    background="green",
    fg="pink",
    width=10,
    height=5,
)
button12 = tk.Button(
    text="-",
    background="green",
    fg="pink",
    width=10,
    height=5,
)
button13 = tk.Button(
    text="*",
    background="green",
    fg="pink",
    width=10,
    height=5,
)
button14 = tk.Button(
    text="/",
    background="green",
    fg="pink",
    width=10,
    height=5,
)
button15 = tk.Button(
    text="=",
    background="green",
    fg="black",
    width=10,
    height=5,
)

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
button10.grid(row=3, column=1)
button11.grid(row=0, column=3)
button12.grid(row=1, column=3)
button13.grid(row=2, column=3)
button14.grid(row=3, column=3)
button15.grid(row=4, column=3)


window.mainloop()