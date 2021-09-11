from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime


now = datetime.now()
index=Tk()
index.title("Logueo",)
index.geometry("300x150")
index.resizable (width=False, height=False)

def day():
    print(now.year, now.month, now.day)

botoncito = Button (index, text="")
lusu=Label (index, text="Username: ")
lusu.pack()
user=StringVar()
eusu=Entry(index, width=30, textvariable=user)
eusu.pack()
lpas=Label(index, text="Password: ")
lpas.pack(anchor=CENTER)

pas=StringVar()
epas=Entry(index, width=30, show="*", textvariable=pas)
epas.pack()

def v2():
    ventana2=Toplevel()
    ventana2.geometry("400x400")
    ventana2.title("Welcome")

boton1=Button(index,text="Aceptar",command=v2).pack()
    


def ingresar():
    if user.get()=="Admin" and pas.get()=="admin"  :
        messagebox.showinfo (title="Login", message="!Te has logueado¡", COMMAND=v2)
    else:
        messagebox.showerror("Login failed",
        "Password or username incorrect")

bl=Button (index, text="Login", command=ingresar)
bl.pack(side=BOTTOM)

index.mainloop()