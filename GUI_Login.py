from tkinter import *
from tkinter import messagebox

def ok():
    user = e1.get()
    password = e2.get()

    if(user == ""):
        messagebox.showinfo("", "Enter Username !")
    elif(password == ""):
        messagebox.showinfo("", "Enter Password !")
    elif(user == "Admin" and password == "12345"):
        messagebox.showinfo("","Login Successfully!")
    else:
        messagebox.showinfo("Wrong! error")

def clear():
    e1.delete(0,END)
    e2.delete(0,END)

root = Tk()
root.title("Login")
root.geometry("250x100")

global e1
global e2

Label(root,text="Username : ", font=('Lucida Fax', 8)).place(x=10,y=10)
e1 = Entry(root)
e1.place(x=80,y=10)

Label(root,text="Password : ", font=('Lucida Fax', 8)).place(x=10,y=40)
e2 = Entry(root)
e2.place(x=80,y=40)
e2.config(show="*")

Button(root,text="Login", command=ok, height=1, width=6, font=('Lucida Fax', 8), bg="orange").place(x=85,y=70)
Button(root,text="Clear", command=clear, height=1, width=6, font=('Lucida Fax', 8), bg="green").place(x=140,y=70)

root.mainloop()
