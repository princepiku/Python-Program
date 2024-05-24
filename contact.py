
#import libraries
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3
#function to define database
def Database():
    global conn, cursor
    #creating contact database
    conn = sqlite3.connect("contact.db")
    cursor = conn.cursor()
    #creating REGISTRATION table
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS REGISTRATION (RID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FNAME TEXT, LNAME TEXT, GENDER TEXT, ADDRESS TEXT, CONTACT TEXT)")
#defining function for creating GUI Layout
def DisplayForm():
    #creating window
    display_screen = Tk()
    #setting width and height for window
    display_screen.geometry("900x400")
    #setting title for window
    display_screen.title("krazyprogrammer.com presents")
    global tree
    global SEARCH
    global fname,lname,gender,address,contact
    SEARCH = StringVar()
    fname = StringVar()
    lname = StringVar()
    gender = StringVar()
    address = StringVar()
    contact = StringVar()
    #creating frames for layout
    #topview frame for heading
    TopViewForm = Frame(display_screen, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    #first left frame for registration from
    LFrom = Frame(display_screen, width="350",bg="#15244C")
    LFrom.pack(side=LEFT, fill=Y)
    #seconf left frame for search form
    LeftViewForm = Frame(display_screen, width=500,bg="#0B4670")
    LeftViewForm.pack(side=LEFT, fill=Y)
    #mid frame for displaying lnames record
    MidViewForm = Frame(display_screen, width=600)
    MidViewForm.pack(side=RIGHT)
    #label for heading
    lbl_text = Label(TopViewForm, text="Contact Management System", font=('verdana', 18), width=600,bg="cyan")
    lbl_text.pack(fill=X)
    #creating registration form in first left frame
    Label(LFrom, text="First Name  ", font=("Arial", 12),bg="#15244C",fg="white").pack(side=TOP)
    Entry(LFrom,font=("Arial",10,"bold"),textvariable=fname).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Last Name ", font=("Arial", 12),bg="#15244C",fg="white").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=lname).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Gender ", font=("Arial", 12),bg="#15244C",fg="white").pack(side=TOP)
    #Entry(LFrom, font=("Arial", 10, "bold"),textvariable=gender).pack(side=TOP, padx=10, fill=X)
    gender.set("Select Gender")
    content={'Male','Female'}
    OptionMenu(LFrom,gender,*content).pack(side=TOP, padx=10, fill=X)


    Label(LFrom, text="Address ", font=("Arial", 12),bg="#15244C",fg="white").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=address).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Contact ", font=("Arial", 12),bg="#15244C",fg="white").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=contact).pack(side=TOP, padx=10, fill=X)
    Button(LFrom,text="Submit",font=("Arial", 10, "bold"),command=register,bg="#15244C",fg="white").pack(side=TOP, padx=10,pady=5, fill=X)

    #creating search label and entry in second frame
    lbl_txtsearch = Label(LeftViewForm, text="Enter fname to Search", font=('verdana', 10),bg="#0B4670")
    lbl_txtsearch.pack()
    #creating search entry
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('verdana', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    #creating search button
    btn_search = Button(LeftViewForm, text="Search", command=SearchRecord,bg="cyan")
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating view button
    btn_view = Button(LeftViewForm, text="View All", command=DisplayData,bg="cyan")
    btn_view.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating reset button
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset,bg="cyan")
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating delete button
    btn_delete = Button(LeftViewForm, text="Delete", command=Delete,bg="cyan")
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    #create update button
    btn_delete = Button(LeftViewForm, text="Update", command=Update,bg="cyan")
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    #setting scrollbar
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm,columns=("Student Id", "Name", "Contact", "Email","Rollno","Branch"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    #setting headings for the columns
    tree.heading('Student Id', text="Id", anchor=W)
    tree.heading('Name', text="FirstName", anchor=W)
    tree.heading('Contact', text="LastName", anchor=W)
    tree.heading('Email', text="Gender", anchor=W)
    tree.heading('Rollno', text="Address", anchor=W)
    tree.heading('Branch', text="Contact", anchor=W)
    #setting width of the columns
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=150)
    tree.column('#3', stretch=NO, minwidth=0, width=80)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayData()
def register():
    Database()
    #getting form data
    fname1=fname.get()
    lname1=lname.get()
    gender1=gender.get()
    address1=address.get()
    contact1=contact.get()
    #applying empty validation
    if fname1=='' or lname1==''or gender1=='' or address1==''or contact1=='':
        tkMessageBox.showinfo("Warning","fill the empty field!!!")
    else:
        #execute query
        conn.execute('INSERT INTO REGISTRATION (FNAME,LNAME,GENDER,ADDRESS,CONTACT) \
              VALUES (?,?,?,?,?)',(fname1,lname1,gender1,address1,contact1));
        conn.commit()
        tkMessageBox.showinfo("Message","Stored successfully")
        #refresh table data
        DisplayData()
        conn.close()
#function to update data into database
def Update():
    Database()
    #getting form data
    fname1=fname.get()
    lname1=lname.get()
    gender1=gender.get()
    address1=address.get()
    contact1=contact.get()
    #applying empty validation
    if fname1=='' or lname1==''or gender1=='' or address1==''or contact1=='':
        tkMessageBox.showinfo("Warning","fill the empty field!!!")
    else:
        #getting selected data
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['values']
        #update query
        conn.execute('UPDATE REGISTRATION SET FNAME=?,LNAME=?,GENDER=?,ADDRESS=?,CONTACT=? WHERE RID = ?',(fname1,lname1,gender1,address1,contact1, selecteditem[0]))
        conn.commit()
        tkMessageBox.showinfo("Message","Updated successfully")
        #reset form
        Reset()
        #refresh table data
        DisplayData()
        conn.close()
def Delete():
    #open database
    Database()
    if not tree.selection():
        tkMessageBox.showwarning("Warning","Select data to delete")
    else:
        result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            cursor=conn.execute("DELETE FROM REGISTRATION WHERE RID = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
def Reset():
    #clear current data from table
    tree.delete(*tree.get_children())
    #refresh table data
    DisplayData()
    #clear search text
    SEARCH.set("")
    fname.set("")
    lname.set("")
    gender.set("")
    address.set("")
    contact.set("")
#function to search data
def SearchRecord():
    #open database
    Database()
    #checking search text is empty or not
    if SEARCH.get() != "":
        #clearing current display data
        tree.delete(*tree.get_children())
        #select query with where clause
        cursor=conn.execute("SELECT * FROM REGISTRATION WHERE FNAME LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        #fetch all matching records
        fetch = cursor.fetchall()
        #loop for displaying all records into GUI
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
#defining function to access data from SQLite database
def DisplayData():
    #open database
    Database()
    #clear current data
    tree.delete(*tree.get_children())
    #select query
    cursor=conn.execute("SELECT * FROM REGISTRATION")
    #fetch all data from database
    fetch = cursor.fetchall()
    #loop for displaying all data in GUI
    for data in fetch:
        tree.insert('', 'end', values=(data))
        tree.bind("<Double-1>",OnDoubleClick)
    cursor.close()
    conn.close()
#import libraries
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3

#function to define database
def Database():
    global conn, cursor
    #creating contact database
    conn = sqlite3.connect("contact.db")
    cursor = conn.cursor()
    #creating REGISTRATION table
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS REGISTRATION (RID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FNAME TEXT, LNAME TEXT, GENDER TEXT, ADDRESS TEXT, CONTACT TEXT)")

#defining function for creating GUI Layout
def DisplayForm():
    #creating window
    display_screen = Tk()
    #setting width and height for window
    display_screen.geometry("900x400")
    #setting title for window
    display_screen.title("krazyprogrammer.com presents")
    global tree
    global SEARCH
    global fname,lname,gender,address,contact
    SEARCH = StringVar()
    fname = StringVar()
    lname = StringVar()
    gender = StringVar()
    address = StringVar()
    contact = StringVar()
    #creating frames for layout
    #topview frame for heading
    TopViewForm = Frame(display_screen, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    #first left frame for registration from
    LFrom = Frame(display_screen, width="350",bg="#15244C")
    LFrom.pack(side=LEFT, fill=Y)
    #seconf left frame for search form
    LeftViewForm = Frame(display_screen, width=500,bg="#0B4670")
    LeftViewForm.pack(side=LEFT, fill=Y)
    #mid frame for displaying lnames record
    MidViewForm = Frame(display_screen, width=600)
    MidViewForm.pack(side=RIGHT)
    #label for heading
    lbl_text = Label(TopViewForm, text="Contact Management System", font=('verdana', 18), width=600,bg="cyan")
    lbl_text.pack(fill=X)
    #creating registration form in first left frame
    Label(LFrom, text="First Name  ", font=("Arial", 12),bg="#15244C",fg="white").pack(side=TOP)
    Entry(LFrom,font=("Arial",10,"bold"),textvariable=fname).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Last Name ", font=("Arial", 12),bg="#15244C",fg="white").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=lname).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Gender ", font=("Arial", 12),bg="#15244C",fg="white").pack(side=TOP)
    #Entry(LFrom, font=("Arial", 10, "bold"),textvariable=gender).pack(side=TOP, padx=10, fill=X)
    gender.set("Select Gender")
    content={'Male','Female'}
    OptionMenu(LFrom,gender,*content).pack(side=TOP, padx=10, fill=X)


    Label(LFrom, text="Address ", font=("Arial", 12),bg="#15244C",fg="white").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=address).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Contact ", font=("Arial", 12),bg="#15244C",fg="white").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=contact).pack(side=TOP, padx=10, fill=X)
    Button(LFrom,text="Submit",font=("Arial", 10, "bold"),command=register,bg="#15244C",fg="white").pack(side=TOP, padx=10,pady=5, fill=X)

    #creating search label and entry in second frame
    lbl_txtsearch = Label(LeftViewForm, text="Enter fname to Search", font=('verdana', 10),bg="#0B4670")
    lbl_txtsearch.pack()
    #creating search entry
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('verdana', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    #creating search button
    btn_search = Button(LeftViewForm, text="Search", command=SearchRecord,bg="cyan")
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating view button
    btn_view = Button(LeftViewForm, text="View All", command=DisplayData,bg="cyan")
    btn_view.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating reset button
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset,bg="cyan")
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating delete button
    btn_delete = Button(LeftViewForm, text="Delete", command=Delete,bg="cyan")
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    #create update button
    btn_delete = Button(LeftViewForm, text="Update", command=Update,bg="cyan")
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    #setting scrollbar
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm,columns=("Student Id", "Name", "Contact", "Email","Rollno","Branch"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    #setting headings for the columns
    tree.heading('Student Id', text="Id", anchor=W)
    tree.heading('Name', text="FirstName", anchor=W)
    tree.heading('Contact', text="LastName", anchor=W)
    tree.heading('Email', text="Gender", anchor=W)
    tree.heading('Rollno', text="Address", anchor=W)
    tree.heading('Branch', text="Contact", anchor=W)
    #setting width of the columns
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=150)
    tree.column('#3', stretch=NO, minwidth=0, width=80)
    tree.column('#4', stretch=NO, minwidth=0, width=120)
    tree.pack()
    DisplayData()
#function to update data into database
def Update():
    Database()
    #getting form data
    fname1=fname.get()
    lname1=lname.get()
    gender1=gender.get()
    address1=address.get()
    contact1=contact.get()
    #applying empty validation
    if fname1=='' or lname1==''or gender1=='' or address1==''or contact1=='':
        tkMessageBox.showinfo("Warning","fill the empty field!!!")
    else:
        #getting selected data
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['values']
        #update query
        conn.execute('UPDATE REGISTRATION SET FNAME=?,LNAME=?,GENDER=?,ADDRESS=?,CONTACT=? WHERE RID = ?',(fname1,lname1,gender1,address1,contact1, selecteditem[0]))
        conn.commit()
        tkMessageBox.showinfo("Message","Updated successfully")
        #reset form
        Reset()
        #refresh table data
        DisplayData()
        conn.close()

def register():
    Database()
    #getting form data
    fname1=fname.get()
    lname1=lname.get()
    gender1=gender.get()
    address1=address.get()
    contact1=contact.get()
    #applying empty validation
    if fname1=='' or lname1==''or gender1=='' or address1==''or contact1=='':
        tkMessageBox.showinfo("Warning","fill the empty field!!!")
    else:
        #execute query
        conn.execute('INSERT INTO REGISTRATION (FNAME,LNAME,GENDER,ADDRESS,CONTACT) \
              VALUES (?,?,?,?,?)',(fname1,lname1,gender1,address1,contact1));
        conn.commit()
        tkMessageBox.showinfo("Message","Stored successfully")
        #refresh table data
        DisplayData()
        conn.close()
def Reset():
    #clear current data from table
    tree.delete(*tree.get_children())
    #refresh table data
    DisplayData()
    #clear search text
    SEARCH.set("")
    fname.set("")
    lname.set("")
    gender.set("")
    address.set("")
    contact.set("")
def Delete():
    #open database
    Database()
    if not tree.selection():
        tkMessageBox.showwarning("Warning","Select data to delete")
    else:
        result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            cursor=conn.execute("DELETE FROM REGISTRATION WHERE RID = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

#function to search data
def SearchRecord():
    #open database
    Database()
    #checking search text is empty or not
    if SEARCH.get() != "":
        #clearing current display data
        tree.delete(*tree.get_children())
        #select query with where clause
        cursor=conn.execute("SELECT * FROM REGISTRATION WHERE FNAME LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        #fetch all matching records
        fetch = cursor.fetchall()
        #loop for displaying all records into GUI
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
#defining function to access data from SQLite database
def DisplayData():
    #open database
    Database()
    #clear current data
    tree.delete(*tree.get_children())
    #select query
    cursor=conn.execute("SELECT * FROM REGISTRATION")
    #fetch all data from database
    fetch = cursor.fetchall()
    #loop for displaying all data in GUI
    for data in fetch:
        tree.insert('', 'end', values=(data))
        tree.bind("<Double-1>",OnDoubleClick)
    cursor.close()
    conn.close()
def OnDoubleClick(self):
    #getting focused item from treeview
    curItem = tree.focus()
    contents = (tree.item(curItem))
    selecteditem = contents['values']
    #set values in the fields
    fname.set(selecteditem[1])
    lname.set(selecteditem[2])
    gender.set(selecteditem[3])
    address.set(selecteditem[4])
    contact.set(selecteditem[5])
# METHODS
def Exit():
    wayOut = tkinter.messagebox.askyesno("Contact Management System", "Do you want to exit the system")
    if wayOut > 0:
        root.destroy()
        return

#calling function
DisplayForm()
if __name__=='__main__':
    #Running Application
    mainloop()



"""
from tkinter import *
import sqlite3
import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

from tkinter import *
import sqlite3
import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox


root = Tk()
root.title("Contact System")
root.geometry("700x400+0+0")
root.resizable(0, 0)
root.config(bg="dark gray")

# VARIABLES
f_name = StringVar()
m_name = StringVar()
l_name = StringVar()
age = StringVar()
home_address = StringVar()
phone_number = StringVar()
gender = StringVar()
religion = StringVar()
nationality = StringVar()

# METHODS
def Exit():
    wayOut = tkinter.messagebox.askyesno("Contact Management System", "Do you want to exit the system")
    if wayOut > 0:
        root.destroy()
        return

def Reset():
    f_name.set("")
    m_name.set("")
    l_name.set("")
    gender.set("")
    age.set("")
    home_address.set("")
    phone_number.set("")
    religion.set("")
    nationality.set("")

def Database():
    conn = sqlite3.connect("contactdb.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `contactable` (id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, first_name TEXT, middle_name TEXT, last_name TEXT, gender TEXT, age TEXT, home_address TEXT, phone_number TEXT, religion TEXT, nationality TEXT)")
    cursor.execute("SELECT * FROM `contactable` ORDER BY `last_name` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def Submit():
    if f_name.get() == "" or m_name.get() == "" or l_name.get() == "" or gender.get() == "" or age.get() == "" or home_address.get() == "" or phone_number.get() == "" or religion.get() == "" or nationality.get() == "":
        result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("contactdb.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO `contactable` (first_name, middle_name, last_name, gender, age, home_address, phone_number, religion, nationality) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", (str(f_name.get()), str(m_name.get()), str(l_name.get()), str(gender.get()), int(age.get()), str(home_address.get()),
            int(phone_number.get()), str(religion.get()), str(nationality.get())))
        conn.commit()
        cursor.execute("SELECT * FROM `contactable` ORDER BY `last_name` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        f_name.set("")
        m_name.set("")
        l_name.set("")
        gender.set("")
        age.set("")
        home_address.set("")
        phone_number.set("")
        religion.set("")
        nationality.set("")


def Update():
    if gender.get() == "":
        result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("contactdb.db")
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE `contactable` SET `first_name` = ?, `middle_name` = ? , `last_name` = ?, `gender` =?, `age` = ?,  `home_address` = ?, `phone_number` = ?, `religion` = ?, `nationality` = ? WHERE `id` = ?",
            (str(f_name.get()), str(m_name.get()),  str(l_name.get()), str(gender.get()), int(age.get()), str(home_address.get()),
            str(phone_number.get()), str(religion.get()), str(nationality.get()), int(id)))
        conn.commit()
        cursor.execute("SELECT * FROM `contactable` ORDER BY `last_name` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        f_name.set("")
        m_name.set("")
        l_name.set("")
        gender.set("")
        age.set("")
        home_address.set("")
        phone_number.set("")
        religion.set("")
        nationality.set("")

def UpdateContactWindow(event):
    global id, UpdateWindow
    curItem = tree.focus()
    contents = (tree.item(curItem))
    selecteditem = contents['values']
    id = selecteditem[0]
    f_name.set("")
    m_name.set("")
    l_name.set("")
    gender.set("")
    age.set("")
    home_address.set("")
    phone_number.set("")
    religion.set("")
    nationality.set("")

    f_name.set(selecteditem[1])
    m_name.set(selecteditem[2])
    l_name.set(selecteditem[3])

    age.set(selecteditem[5])
    home_address.set(selecteditem[6])
    phone_number.set(selecteditem[7])
    religion.set(selecteditem[8])
    nationality.set(selecteditem[9])

    UpdateWindow = Toplevel()
    UpdateWindow.title("Contact Details")
    UpdateWindow.geometry("500x520+0+0")
    UpdateWindow.config(bg="dark gray")
    UpdateWindow.resizable(0, 0)
    if 'NewWindow' in globals():
        NewWindow.destroy()

    # FRAMES
    FormTitle = Frame(UpdateWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(UpdateWindow)
    ContactForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(ContactForm)
    Male = Radiobutton(RadioGroup, text="Male", variable=gender, value="Male", font=('arial', 14)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup, text="Female", variable=gender, value="Female", font=('arial', 14)).pack(side=LEFT)
    Transgender = Radiobutton(RadioGroup, text="Transgender", variable=gender, value="Transgender", font=('arial', 14)).pack(side=LEFT)
    # LABELS
    lbl_title = Label(FormTitle, text="Updating Contacts", bd=12, relief=GROOVE, fg="White", bg="blue",
                      font=("Calibri", 14, "bold"), pady=3)
    lbl_title.pack(fill=X)
    lbl_FirstName = Label(ContactForm, text="First Name", font=('arial', 14), bd=5)
    lbl_FirstName.grid(row=0, sticky=W)

    lbl_MiddleName = Label(ContactForm, text="Middle Name", font=('arial', 14), bd=5)
    lbl_MiddleName.grid(row=1, sticky=W)

    lbl_LastName = Label(ContactForm, text="Last Name", font=('arial', 14), bd=5)
    lbl_LastName.grid(row=2, sticky=W)

    lbl_Gender = Label(ContactForm, text="Gender", font=('arial', 14), bd=5)
    lbl_Gender.grid(row=3, sticky=W)

    lbl_Age = Label(ContactForm, text="Age", font=('arial', 14), bd=5)
    lbl_Age.grid(row=4, sticky=W)

    lbl_HomeAddress = Label(ContactForm, text=" Home Address", font=('arial', 14), bd=5)
    lbl_HomeAddress.grid(row=5, sticky=W)

    lbl_PhoneNumber = Label(ContactForm, text="Phone Number", font=('arial', 14), bd=5)
    lbl_PhoneNumber.grid(row=6, sticky=W)

    lbl_Religion = Label(ContactForm, text="Religion", font=('arial', 14), bd=5)
    lbl_Religion.grid(row=7, sticky=W)

    lbl_Nationality = Label(ContactForm, text="Nationality", font=('arial', 14), bd=5)
    lbl_Nationality.grid(row=8, sticky=W)

    # TEXT ENTRY
    FirstName = Entry(ContactForm, textvariable=f_name, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    FirstName.grid(row=0, column=1)

    MiddleName = Entry(ContactForm, textvariable=m_name, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    MiddleName.grid(row=1, column=1)

    LastName = Entry(ContactForm, textvariable=l_name, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    LastName.grid(row=2, column=1)

    RadioGroup.grid(row=3, column=1)

    Age = Entry(ContactForm, textvariable=age, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    Age.grid(row=4, column=1)

    HomeAddress = Entry(ContactForm, textvariable=home_address, font=('arial', 14, 'bold'), bd=10, width=20,
                        justify='left')
    HomeAddress.grid(row=5, column=1)

    PhoneNumber = Entry(ContactForm, textvariable=phone_number, font=('arial', 14, 'bold'), bd=10, width=20,
                        justify='left')
    PhoneNumber.grid(row=6, column=1)

    Religion = Entry(ContactForm, textvariable=religion, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    Religion.grid(row=7, column=1)

    Nationality = Entry(ContactForm, textvariable=nationality, font=('arial', 14, 'bold'), bd=10, width=20,
                        justify='left')
    Nationality.grid(row=8, column=1)
    # ==================BUTTONS==============================
    ButtonUpdatContact = Button(ContactForm, text='Update', bd=10, font=('arial', 12, 'bold'), relief="ridge", fg="white",
                              bg="blue", command=Update)
    ButtonUpdatContact.grid(row=9, columnspan=2, pady=10)



def Delete():
    if not tree.selection():
        result = tkMessageBox.showwarning('', 'Please Select in the Table First!', icon="warning")
    else:
        result = tkMessageBox.askquestion('', 'Are You Sure You Want To Delete This Record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            conn = sqlite3.connect("contactdb.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM `contactable` WHERE `id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()


def AddNewContact():
    global NewWindow
    f_name.set("")
    m_name.set("")
    l_name.set("")
    gender.set("")
    age.set("")
    home_address.set("")
    phone_number.set("")
    religion.set("")
    nationality.set("")
    NewWindow = Toplevel()
    NewWindow.title("Contact Details")
    NewWindow.resizable(0, 0)
    NewWindow.geometry("500x520+0+0")
    NewWindow.config(bg="dark gray")
    if 'UpdateWindow' in globals():
        UpdateWindow.destroy()

    # ===================FRAMES==============================
    FormTitle = Frame(NewWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(NewWindow)
    ContactForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(ContactForm)
    Male = Radiobutton(RadioGroup, text="Male", variable=gender, value="Male", font=('arial', 14)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup, text="Female", variable=gender, value="Female", font=('arial', 14)).pack(side=LEFT)
    Transgender = Radiobutton(RadioGroup, text="Transgender", variable=gender, value="Transgender", font=('arial', 14)).pack(side=LEFT)
    # ===================LABELS==============================
    lbl_title = Label(FormTitle, text="Adding New Contacts",  bd=12, relief=GROOVE, fg="White", bg="blue",
                      font=("Calibri", 14, "bold"), pady=3)
    lbl_title.pack(fill=X)
    lbl_FirstName = Label(ContactForm, text="First Name", font=('arial', 14), bd=5)
    lbl_FirstName.grid(row=0, sticky=W)

    lbl_MiddleName = Label(ContactForm, text="Middle Name", font=('arial', 14), bd=5)
    lbl_MiddleName.grid(row=1, sticky=W)

    lbl_LastName = Label(ContactForm, text="Last Name", font=('arial', 14), bd=5)
    lbl_LastName.grid(row=2, sticky=W)

    lbl_Gender = Label(ContactForm, text="Gender", font=('arial', 14), bd=5)
    lbl_Gender.grid(row=3, sticky=W)

    lbl_Age = Label(ContactForm, text="Age", font=('arial', 14), bd=5)
    lbl_Age.grid(row=4, sticky=W)

    lbl_HomeAddress = Label(ContactForm, text=" Home Address", font=('arial', 14), bd=5)
    lbl_HomeAddress.grid(row=5, sticky=W)

    lbl_PhoneNumber = Label(ContactForm, text="Phone Number", font=('arial', 14), bd=5)
    lbl_PhoneNumber.grid(row=6, sticky=W)

    lbl_Religion = Label(ContactForm, text="Religion", font=('arial', 14), bd=5)
    lbl_Religion.grid(row=7, sticky=W)

    lbl_Nationality = Label(ContactForm, text="Nationality", font=('arial', 14), bd=5)
    lbl_Nationality.grid(row=8, sticky=W)

    # ===================ENTRY===============================
    FirstName = Entry(ContactForm, textvariable=f_name, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    FirstName.grid(row=0, column=1)

    MiddleName = Entry(ContactForm, textvariable=m_name, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    MiddleName.grid(row=1, column=1)

    LastName = Entry(ContactForm, textvariable=l_name, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    LastName.grid(row=2, column=1)

    RadioGroup.grid(row=3, column=1)

    Age = Entry(ContactForm, textvariable=age, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    Age.grid(row=4, column=1)

    HomeAddress = Entry(ContactForm, textvariable=home_address, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    HomeAddress.grid(row=5, column=1)

    PhoneNumber = Entry(ContactForm, textvariable=phone_number, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    PhoneNumber.grid(row=6, column=1)

    Religion = Entry(ContactForm, textvariable=religion, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    Religion.grid(row=7, column=1)

    Nationality = Entry(ContactForm, textvariable=nationality, font=('arial', 14, 'bold'), bd=10, width=20, justify='left')
    Nationality.grid(row=8, column=1)

    # ==================BUTTONS==============================
    ButtonAddContact = Button(ContactForm, text='Save',  bd=10, font=('arial', 12, 'bold'), relief="ridge", fg="white",
                   bg="blue", command=Submit)
    ButtonAddContact.grid(row=9, columnspan=2, pady=10)


# ============================FRAMES======================================
Top = Frame(root, width=500, bd=1, relief=SOLID)
Top.pack(side=TOP)
Mid = Frame(root, width=500, bg="dark gray")
Mid.pack(side=BOTTOM)
f1 = Frame(root, width=6, height=8, bd=8, bg="dark gray")
f1.pack(side=BOTTOM)
flb = Frame(f1, width=6, height=8, bd=8, bg="blue")
flb.pack(side=BOTTOM)
MidLeft = Frame(Mid, width=100)
MidLeft.pack(side=LEFT, pady=10)
MidLeftPadding = Frame(Mid, width=370, bg="dark gray")
MidLeftPadding.pack(side=LEFT)
MidRight = Frame(Mid, width=100)
MidRight.pack(side=RIGHT, pady=10)
TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)

# LABELS
lbl_title = Label(Top,  text="Contact Management System", bd=12, relief=GROOVE, fg="White", bg="blue",
                      font=("Calibri", 36, "bold"), pady=3)
lbl_title.pack(fill=X)


# BUTTONS
ButtonAdd = Button(flb, text='Add New Contact',  bd=8, font=('arial', 12, 'bold'), relief="groove", fg="black",
                   bg="dark gray", command=AddNewContact).grid(row=0, column=0, ipadx=20, padx=30)

ButtonDelete = Button(flb, text='Delete', bd=8, font=('arial', 12, 'bold'), relief="groove",  command=Delete,
                  fg="black", bg="dark gray").grid(row=0, column=1, ipadx=20)

ButtonExit = Button(flb, text='Exit System', bd=8, font=('arial', 12, 'bold'), relief="groove",  command=Exit,
                 fg="black", bg="dark gray").grid(row=0, column=2, ipadx=20, padx=30)

# TABLES
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("Id", "First Name", "Middle Name", "Last Name", "Gender", "Age", "Home Address", "Phone Number", "Religion", "Nationality"),
                    height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('Id', text="Id", anchor=W)
tree.heading('First Name', text="First Name", anchor=W)
tree.heading('Middle Name', text="Middle Name", anchor=W)
tree.heading('Last Name', text="Last Name", anchor=W)
tree.heading('Gender', text="Gender", anchor=W)
tree.heading('Age', text="Age", anchor=W)
tree.heading('Home Address', text="Home Address", anchor=W)
tree.heading('Phone Number', text="phone Number", anchor=W)
tree.heading('Religion', text="Religion", anchor=W)
tree.heading('Nationality', text="Nationality", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=0)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=90)
tree.column('#5', stretch=NO, minwidth=0, width=80)
tree.column('#6', stretch=NO, minwidth=0, width=30)
tree.column('#7', stretch=NO, minwidth=0, width=120)
tree.column('#8', stretch=NO, minwidth=0, width=120)
tree.column('#9', stretch=NO, minwidth=0, width=120)
tree.pack()
tree.bind('<Double-Button-1>', UpdateContactWindow)

# ============================INITIALIZATION==============================
if __name__ == '__main__':
    Database()
    root.mainloop()

"""