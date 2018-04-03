#! /usr/bin/env python
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1
from tkinter import messagebox
import pymysql
import connect
import Home
import random

def vp_start_gui():
    global val, w, root
    root = Tk()
    top = Add_New_Book (root)
    root.mainloop()

w = None
conn=connect.connect()
cur=conn.cursor()

def create_Add_New_Book(root, *args, **kwargs):
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Add_New_Book (w)
    return (w, top)

def switch_frame(top,frame_class):
    top.destroy()
    frame_class.vp_start_gui()

def add(id,name,edition,publisher,price,pages):
    try:
        sql='insert into Book values(%s,%s,%s,%s,%s,%s)'
        cur.execute(sql,(int(id.get()),str(name.get()),str(edition.get()),str(publisher.get()),int(price.get()),int(pages.get())))
        conn.commit()
        messagebox.showinfo("Success", "New Book Added")

    except pymysql.IntegrityError as e:
        messagebox.showinfo("Try again", "Book already exist")
    except Exception as e:
        messagebox.showinfo("Error", e)
class Add_New_Book:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font13 = "-family {DejaVu Sans} -size 11 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font9 = "-family {DejaVu Sans} -size 15 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("578x450+467+173")
        top.title("Add New Book")



        self.Labelframe1 = LabelFrame(top)
        self.Labelframe1.place(relx=0.09, rely=0.04, relheight=0.88
                , relwidth=0.83)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(font=font9)
        self.Labelframe1.configure(foreground="#bb0000")
        self.Labelframe1.configure(text='''New Book''')
        self.Labelframe1.configure(width=480)

        self.Label1 = Label(self.Labelframe1)
        self.Label1.place(relx=0.05, rely=0.15, height=19, width=66)
        self.Label1.configure(font=font13)
        self.Label1.configure(text='''Book Id''')
        self.Label1.configure(width=66)

        self.Label2 = Label(self.Labelframe1)
        self.Label2.place(relx=0.06, rely=0.28, height=19, width=66)
        self.Label2.configure(font=font13)
        self.Label2.configure(text='''Name''')
        self.Label2.configure(width=66)

        self.Label3 = Label(self.Labelframe1)
        self.Label3.place(relx=0.06, rely=0.41, height=19, width=66)
        self.Label3.configure(font=font13)
        self.Label3.configure(text='''Edition''')
        self.Label3.configure(width=66)

        self.Label4 = Label(self.Labelframe1)
        self.Label4.place(relx=0.06, rely=0.53, height=22, width=66)
        self.Label4.configure(font=font13)
        self.Label4.configure(text='''Publisher''')
        self.Label4.configure(width=66)

        self.Label5 = Label(self.Labelframe1)
        self.Label5.place(relx=0.06, rely=0.66, height=22, width=66)
        self.Label5.configure(font=font13)
        self.Label5.configure(text='''Price''')

        self.Label6 = Label(self.Labelframe1)
        self.Label6.place(relx=0.06, rely=0.78, height=22, width=66)
        self.Label6.configure(font=font13)
        self.Label6.configure(text='''Pages''')

        id=StringVar()
        self.Entry1 = Entry(self.Labelframe1,textvariable=id)
        self.Entry1.place(relx=0.33, rely=0.15,height=21, relwidth=0.51)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(width=246)
        data=str(random.randint(1,1000))
        self.Entry1.insert(len(data),data)
        self.Entry1.configure(state=DISABLED)

        name=StringVar()
        self.Entry2 = Entry(self.Labelframe1, textvariable=name)
        self.Entry2.place(relx=0.33, rely=0.28,height=21, relwidth=0.51)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")

        edition=StringVar()
        self.Entry3 = Entry(self.Labelframe1,textvariable=edition)
        self.Entry3.place(relx=0.33, rely=0.41,height=21, relwidth=0.51)
        self.Entry3.configure(background="white")
        self.Entry3.configure(font="TkFixedFont")

        publisher=StringVar()
        self.Entry4 = Entry(self.Labelframe1,textvariable=publisher)
        self.Entry4.place(relx=0.33, rely=0.53,height=21, relwidth=0.51)
        self.Entry4.configure(background="white")
        self.Entry4.configure(font="TkFixedFont")

        price=StringVar()
        self.Entry5 = Entry(self.Labelframe1,textvariable=price)
        self.Entry5.place(relx=0.33, rely=0.66,height=21, relwidth=0.51)
        self.Entry5.configure(background="white")
        self.Entry5.configure(font="TkFixedFont")

        pages=StringVar()
        self.Entry6 = Entry(self.Labelframe1,textvariable=pages)
        self.Entry6.place(relx=0.33, rely=0.78,height=21, relwidth=0.51)
        self.Entry6.configure(background="white")
        self.Entry6.configure(font="TkFixedFont")

        self.Button1 = Button(self.Labelframe1,command=lambda:add(id,name,edition,publisher,price,pages))
        self.Button1.place(relx=0.19, rely=0.89, height=37, width=107)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(background="#9ed9d9")
        self.Button1.configure(borderwidth="4")
        self.Button1.configure(text='''Add''')
        self.Button1.configure(width=107)

        self.Button2 = Button(self.Labelframe1,command=lambda:switch_frame(top,Home))
        self.Button2.place(relx=0.5, rely=0.89, height=37, width=167)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(background="#b3d9d9")
        self.Button2.configure(borderwidth="4")
        self.Button2.configure(text='''Go Back to Home''')
        self.Button2.configure(width=167)






if __name__ == '__main__':
    vp_start_gui()


