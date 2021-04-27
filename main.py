#
# chess program
#

from tkinter import *

window = Tk()

mylabel = Label(window, text="Hello world!")  # makes a label widget
mylabel.grid(row=0, column=1)
# mylabel.pack()  # packs the window to the size of what it has in it. Keeps things in the middle

mylabel2 = Label(window, text="booples")  # makes a label widget
mylabel2.grid(row=1, column=0)  # places label at a specific row and col

window.mainloop()
