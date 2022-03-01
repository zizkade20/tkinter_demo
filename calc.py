import tkinter as tk

#def calc_get():

window = tk.Tk()
window.geometry("400x420")
window.title("Fortnite")

entry = tk.Entry(
    width=40,

)

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
button0 = tk.Button(
    text="0",
    background="green",
    fg="purple",
    width=10,
    height=5,
)
buttonplus = tk.Button(
    text="+",
    background="green",
    fg="black",
    width=10,
    height=5,
)
buttonminus = tk.Button(
    text="-",
    background="green",
    fg="black",
    width=10,
    height=5,
)
buttonkrat = tk.Button(
    text="x",
    background="green",
    fg="black",
    width=10,
    height=5,
)
buttondeleno = tk.Button(
    text="÷",
    background="green",
    fg="black",
    width=10,
    height=5,
)
buttonrovnase = tk.Button(
    text="=",
    background="green",
    fg="red",
    width=10,
    height=5,
)
buttondelete = tk.Button(
    text="C",
    background="green",
    fg="black",
    width=10,
    height=5,
)
entry.grid(columnspan=4)
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
button0.grid(row=4, column=1)
buttonplus.grid(row=1, column=3)
buttonminus.grid(row=2, column=3)
buttonkrat.grid(row=3, column=3)
buttondeleno.grid(row=4, column=3)
buttonrovnase.grid(row=4, column=2)
buttondelete.grid(row=4, column=0)

window.mainloop()