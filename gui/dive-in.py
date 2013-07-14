import Tkinter

window = Tkinter.Tk()

question = Tkinter.Label(window, text="Are you sure you want to learn?")
ok = Tkinter.Button(window, text="OK")
cancel = Tkinter.Button(window, text="Cancel")

question.grid(row=0, column=0, columnspan=3)
ok.grid(row=1, column=1)
cancel.grid(row=1, column=2)

window.mainloop()
