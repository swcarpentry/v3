import Tkinter

window = Tkinter.Tk()

big = Tkinter.Button(window, text="Click me", font=("",60))
medium = Tkinter.Button(window, text="Click me")
small = Tkinter.Button(window, text="Click me", font=("",8))

big.pack()
medium.pack()
small.pack()

window.mainloop()
