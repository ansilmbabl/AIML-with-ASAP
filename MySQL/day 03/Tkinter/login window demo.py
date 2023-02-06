from tkinter import *

w = Tk()
w.geometry("400x800")

def click():
    l3.place(x=150,y=650)

l = Label(text = "username",font=("Times 10 italic bold"))
l.place(x=150,y=180)
e1 = Entry()
e1.place(x=100,y=210)

l2 = Label(text = "password",font=("Times 10 italic bold"))
l2.place(x=150,y=380)
e2 = Entry(w,show="*")
e2.place(x=100,y=410)

l3 = Label(text = "Login succesful")

b =Button(text="login", font = ("Arial 15 bold"),bd = 2,command = click)
b.place(x=160,y=600)

w.mainloop()
