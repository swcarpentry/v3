import Tkinter

window = Tkinter.Tk()

titleLabel = Tkinter.Label(window, text="Calculator Ultra", font=("Helvetica", 16))

result = Tkinter.StringVar()
resultLabel = Tkinter.Label(window, textvariable=result)

equation = Tkinter.StringVar()

def evalCommand():
    result.set(eval(equation.get()))

equationEntry = Tkinter.Entry(window, textvariable=equation, font=("Futura",))
solveButton = Tkinter.Button(window, text="Enter", font=("Helvetica",), command=evalCommand)

titleLabel.grid(row=0, column=0, columnspan=3)
equationEntry.grid(row=1, column=0, columnspan=2)
solveButton.grid(row=1, column=2)

resultLabel.grid(row=3, column=0, columnspan=3)

window.mainloop()
