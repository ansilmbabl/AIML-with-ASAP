# login window mysql

from tkinter import *
from tkinter import messagebox
import mysql.connector

## db connection............................................................................

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root1234",
    database = "userdetails"
    )
c = mydb.cursor()

def validate():
    sql = "select * from login_details where usr = %s and psd = %s"
    values = (usr.get(),psd.get())
    c.execute(sql,values)
    results = c.fetchall()
    if results:
        for i in results:
            #print("login succesfull")
            messagebox.showinfo("success","Login Succesfull")
    else:
        #print("Invalid credentials")
        messagebox.showerror("Failed","Username or password is incorrect")

def psdshow():
    if v.get() == 1:
        psd.config(show="")
    else:
        psd.config(show="*")

def show_register():
    login_frame.place_forget() # pack -> pack.forget() / gird -> grid.forget()
    reg_frame.place(x=150,y=150)

def insert():
    sql = "insert into login_details (usr,psd) values (%s,%s)"
    s1 = usr1.get()
    s2 = psd1.get()
    s3 = psd2.get()

    if s1 == "" or s2=="" or s3=="":
        messagebox.shoqwarning("Warning!!","fileda cannot be empty")
    elif s2 != s3:
        messagebox.showerror("Error","Password do not match")
    else:
        try:
            val = (s1,s2)
            c.execute(sql,val)
            mybd.commit()
            messagebox.showinfo("Succes","Account created")
        except Exception as e:
            messagebox.showerror("Duplicate user","user already exist")
        

def show_login():
    reg_frame.place_forget()
    login_frame.place(x=150,y=150)

## login fame..................................................................................
w = Tk() #window (class object)
w.geometry ("600x400")
login_frame = Frame(w,highlightbackground = "green",highlightthickness=2)
login_frame.place(x=150,y=150)

l1 = Label(login_frame,text="Enter Username")
l1.grid(row=0,column=0)

l2 = Label(login_frame,text="Enter Password")
l2.grid(row=1,column=0)

usr = Entry(login_frame)
usr.grid(row=0,column=1)
psd = Entry(login_frame,show="*")
psd.grid(row=1,column=1)

# check button
v = IntVar(value = 0)
c1 = Checkbutton(login_frame,text="show password",variable = v,onvalue = 1, offvalue = 0,command = psdshow)
c1.grid(row= 1, column =2)

#sign in button
b1 = Button(login_frame,text="sign in", command = validate)
b1.grid(row=2,column=1)

# create account button
b2 = Button(login_frame,text="create account", command = show_register)
b2.grid(row=3,column=1)



## new frame........................................
reg_frame = Frame(w)

l3 = Label(reg_frame,text="Enter Username")
l3.grid(row=0,column=0)

l4 = Label(reg_frame,text="Enter Password")
l4.grid(row=1,column=0)

l5 = Label(reg_frame,text="Confirm Password")
l5.grid(row=2,column=0)


usr1 = Entry(reg_frame)
usr1.grid(row=0,column=1)
psd1 = Entry(reg_frame,show="*")
psd1.grid(row=1,column=1)
psd2 = Entry(reg_frame,show="*")
psd2.grid(row=2,column=1)

#sign in button
b3 = Button(reg_frame,text="save", command = insert)
b3.grid(row=3,column=1)

# create account button
b4 = Button(reg_frame,text="back to login", command = show_login)
b4.grid(row=4,column=1)

w.mainloop()
