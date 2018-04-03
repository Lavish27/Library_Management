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
    top = Remove_Student (root)
    root.mainloop()

w = None
conn=connect.connect()
cur=conn.cursor()

def create_Remove_Student(root, *args, **kwargs):
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Remove_Student (w)
    return (w, top)

def switch_frame(top,frame_class):
    top.destroy()
    frame_class.vp_start_gui()

def search(id,e2,e3,e4,e5,e6):
    try:
        sql = 'select * from Student where Student_Number=%s'
        cur.execute(sql,(int(id.get())))
        data = cur.fetchall()
        if data:
            e2.configure(state="normal")
            e2.insert(len(data[0][0]), data[0][0])
            e2.configure(state="readonly")
            e3.configure(state="normal")
            e3.insert(len(data[0][2]), data[0][2])
            e3.configure(state="readonly")
            e4.configure(state="normal")
            e4.insert(len(data[0][3]), data[0][3])
            e4.configure(state="readonly")
            e5.configure(state="normal")
            e5.insert(len(str(data[0][4])), data[0][4])
            e5.configure(state="readonly")
            e6.configure(state="normal")
            e6.insert(len(str(data[0][5])), data[0][5])
            e6.configure(state="readonly")
        else:
            messagebox.showinfo("Try Again", "Student doesn't exist")
    except Exception as e:
        messagebox.showinfo("Error", e)


def remove(id):
    try:
        sql1="delete from Student where Student_Number=%s"
        cur.execute(sql1,(int(id.get())))
        conn.commit()
        messagebox.showinfo("Success", "Student Removed")
    except Exception as e:
        messagebox.showinfo("Error", e)

class Remove_Student:
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
        top.title("Remove Book")



        self.Labelframe1 = LabelFrame(top)
        self.Labelframe1.place(relx=0.09, rely=0.04, relheight=0.88
                , relwidth=0.87)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(font=font9)
        self.Labelframe1.configure(foreground="#bb0000")
        self.Labelframe1.configure(text='''Remove Student''')
        self.Labelframe1.configure(width=480)

        self.Label1 = Label(self.Labelframe1)
        self.Label1.place(relx=0.05, rely=0.15, height=19, width=122)
        self.Label1.configure(font=font13)
        self.Label1.configure(text='''Student Number''')
        self.Label1.configure(width=66)


        self.Label2 = Label(self.Labelframe1)
        self.Label2.place(relx=0.06, rely=0.28, height=19, width=66)
        self.Label2.configure(font=font13)
        self.Label2.configure(text='''Name''')
        self.Label2.configure(width=66)

        self.Label3 = Label(self.Labelframe1)
        self.Label3.place(relx=0.06, rely=0.41, height=19, width=66)
        self.Label3.configure(font=font13)
        self.Label3.configure(text='''Course''')
        self.Label3.configure(width=66)

        self.Label4 = Label(self.Labelframe1)
        self.Label4.place(relx=0.06, rely=0.53, height=22, width=66)
        self.Label4.configure(font=font13)
        self.Label4.configure(text='''Branch''')
        self.Label4.configure(width=66)

        self.Label5 = Label(self.Labelframe1)
        self.Label5.place(relx=0.06, rely=0.66, height=22, width=66)
        self.Label5.configure(font=font13)
        self.Label5.configure(text='''Year''')

        self.Label6 = Label(self.Labelframe1)
        self.Label6.place(relx=0.04, rely=0.78, height=22, width=100)
        self.Label6.configure(font=font13)
        self.Label6.configure(text='''Semester''')

        id=StringVar()
        self.Entry1 = Entry(self.Labelframe1,textvariable=id)
        self.Entry1.place(relx=0.33, rely=0.15,height=21, relwidth=0.51)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(width=246)

        name=StringVar()
        self.Entry2 = Entry(self.Labelframe1, textvariable=name)
        self.Entry2.place(relx=0.33, rely=0.28,height=21, relwidth=0.51)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(state="readonly")

        edition=StringVar()
        self.Entry3 = Entry(self.Labelframe1,textvariable=edition)
        self.Entry3.place(relx=0.33, rely=0.41,height=21, relwidth=0.51)
        self.Entry3.configure(background="white")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(state="readonly")

        publisher=StringVar()
        self.Entry4 = Entry(self.Labelframe1,textvariable=publisher)
        self.Entry4.place(relx=0.33, rely=0.53,height=21, relwidth=0.51)
        self.Entry4.configure(background="white")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(state="readonly")

        price=StringVar()
        self.Entry5 = Entry(self.Labelframe1,textvariable=price)
        self.Entry5.place(relx=0.33, rely=0.66,height=21, relwidth=0.51)
        self.Entry5.configure(background="white")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(state="readonly")


        pages=StringVar()
        self.Entry6 = Entry(self.Labelframe1,textvariable=pages)
        self.Entry6.place(relx=0.33, rely=0.78,height=21, relwidth=0.51)
        self.Entry6.configure(background="white")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(state="readonly")

        self.Button3 = Button(self.Labelframe1,
                              command=lambda: search(id, self.Entry2, self.Entry3, self.Entry4, self.Entry5,
                                                     self.Entry6))
        self.Button3.place(relx=0.85, rely=0.13, height=37, width=70)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(background="#9ed9d9")
        self.Button3.configure(borderwidth="4")
        self.Button3.configure(text='''Search''')
        self.Button3.configure(width=107)

        self.Button1 = Button(self.Labelframe1,command=lambda:remove(id))
        self.Button1.place(relx=0.19, rely=0.89, height=37, width=107)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(background="#9ed9d9")
        self.Button1.configure(borderwidth="4")
        self.Button1.configure(text='''Remove''')
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


