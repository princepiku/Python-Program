from tkinter import *
from tkinter import messagebox

def ok():
    SRN = n1.get()
    Name = n2.get()
    Email_id = n3.get()
    Phone_no = n4.get()
    Address = n5.get()

    if(SRN == ""):
        messagebox.showinfo("","Please Enter SRN !")
    elif(Name == ""):
        messagebox.showinfo("","Please Enter Name !")
    elif(Email_id == ""):
        messagebox.showinfo("","Please Enter Email-id !")
    elif(Phone_no == ""):
        messagebox.showinfo("","Please Enter Phone No !")
    elif(Address == ""):
        messagebox.showinfo("","Please Enter Address !")
    elif(SRN == "R179"  and Name == "Prince" and Email_id == "prince@gmail.com" and Phone_no == "9142382053" and Address == "Bihar"):
        messagebox.showinfo("","Save Successfully!")
    else:
        messagebox.showinfo("","Wrong Information!")

def clear():
    n1.delete(0,END)
    n2.delete(0,END)
    n3.delete(0,END)
    n4.delete(0,END)
    n5.delete(0,END)

root = Tk()
root.title("Student Infromation")
root.geometry("280x240")

global n1
global n2
global n3
global n4
global n5

Label(root,text="Student Details", font=('Lucida Fax', 15), bg="yellow").place(x=60,y=10)

Label(root,text="SRN  ", font=('Lucida Fax', 12)).place(x=20,y=60)
n1 = Entry(root)
n1.place(x=110,y=60)

Label(root,text="Name  ", font=('Lucida Fax', 12)).place(x=20,y=80)
n2 = Entry(root)
n2.place(x=110,y=80)

Label(root,text="Email-id  ", font=('Lucida Fax', 12)).place(x=20,y=100)
n3 = Entry(root)
n3.place(x=110,y=100)

Label(root,text="Phone No  ", font=('Lucida Fax', 12)).place(x=20,y=120)
n4 = Entry(root)
n4.place(x=110,y=120)

Label(root,text="Address  ", font=('Lucida Fax', 12)).place(x=20,y=140)
n5 = Entry(root)
n5.place(x=110,y=140)

Gender = IntVar()
Label(root,text="Gender  ", font=('Lucida Fax', 12)).place(x=20,y=160)
Radiobutton(root,text="Male", variable=Gender, value="Male", font=('Lucida Fax', 12)).place(x=110,y=160)
Radiobutton(root,text="Female", variable=Gender, value="Female", font=('Lucida Fax', 12)).place(x=180,y=160)

Button(root,text="Save", command=ok, height=1, width=6, font=('Lucida Fax', 10), bg="orange").place(x=100,y=200)
Button(root,text="Clear", command=clear, height=1, width=6, font=('Lucida Fax', 10), bg="green").place(x=160,y=200)

root.mainloop()

