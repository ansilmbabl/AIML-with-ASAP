## Tkinter 1

#importing module
from tkinter import *
from PIL import Image,ImageTk  # to resize image

w = Tk()
w.geometry("840x420") # changing size

## labels
l = Label(text = "label 1",font=("Times 12 italic bold"),fg = "red",bg = "black",height =3,width =5)

#l.place(x=0,y=0)
l.pack(side = "right") # random position (top ,bottom,right,left)

## image in a label
img = Image.open("D:\\AIML\\openCV\\1\\Resources\\jchar.png")
resize = img.resize((56,75))
label_img = ImageTk.PhotoImage(resize)
l1 = Label(w,image = label_img)
l1.place(x=300,y=200)

## button
l2 = Label(text="button clicked")
def click():
    l2.pack(side="top")

b =Button(text="click me", font = ("Arial 15 bold"),bd = 2,command = click)
b.place(x=300,y=300)

#text box
e = Entry(w)
e.pack()

w.mainloop()
