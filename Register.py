from tkinter import *
from tkinter import ttk
from tkinter import messagebox

index = Tk()
index.title("Registro")
index.geometry("300x160")
index.resizable  (width=False, height=False)

lusu = Label (index, text="Name")
lusu.pack()

user = StringVar()
susu = Entry (index, width = 30, textvariable = user)
susu.pack()

peru = Label(index, text="Mail: ")
peru.pack(anchor = CENTER)

eru = StringVar()
leru = Entry(index, width = 30, textvariable = eru)
leru.pack()

lpas = Label(index, text = "Password: ")
lpas.pack(anchor = CENTER)

pas = StringVar()
epas = Entry(index, width = 30, show="*", textvariable = pas)
epas.pack()



bl=Button (index, text="Login")
bl.pack(side=BOTTOM)

index.mainloop()