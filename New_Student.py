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
    top = Add_New_Student (root)
    root.mainloop()

w = None
conn=connect.connect()
cur=conn.cursor()

def create_Add_New_Student(root, *args, **kwargs):
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Add_New_Student (w)
    return (w, top)

def switch_frame(top,frame_class):
    top.destroy()
    frame_class.vp_start_gui()

def add(name,number,course,branch,year,sem):
    try:
        sql='insert into Student values(%s,%s,%s,%s,%s,%s)'
        cur.execute(sql,(str(name.get()),int(number.get()),str(course.get()),str(branch.get()),int(year.get()),int(sem.get())))
        conn.commit()
        messagebox.showinfo("Success", "New Student Added")

    except pymysql.IntegrityError as e:
        messagebox.showinfo("Try again", "Student already exist")
    except Exception as e:
        messagebox.showinfo("Error", e)

class Add_New_Student:
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
        top.title("Add New Student")



        self.Labelframe1 = LabelFrame(top)
        self.Labelframe1.place(relx=0.09, rely=0.04, relheight=0.88
                , relwidth=0.83)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(font=font9)
        self.Labelframe1.configure(foreground="#bb0000")
        self.Labelframe1.configure(text='''New Student''')
        self.Labelframe1.configure(width=480)

        self.Label1 = Label(self.Labelframe1)
        self.Label1.place(relx=0.05, rely=0.15, height=19, width=66)
        self.Label1.configure(font=font13)
        self.Label1.configure(text='''Name''')
        self.Label1.configure(width=66)

        self.Label2 = Label(self.Labelframe1)
        self.Label2.place(relx=0.06, rely=0.28, height=19, width=126)
        self.Label2.configure(font=font13)
        self.Label2.configure(text='''Student Number''')
        self.Label2.configure(width=126)

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
        self.Label6.place(relx=0.06, rely=0.78, height=22, width=76)
        self.Label6.configure(font=font13)
        self.Label6.configure(text='''Semester''')

        name=StringVar()
        self.Entry1 = Entry(self.Labelframe1,textvariable=name)
        self.Entry1.place(relx=0.33, rely=0.15,height=21, relwidth=0.51)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(width=246)


        number=StringVar()
        self.Entry2 = Entry(self.Labelframe1, textvariable=number)
        self.Entry2.place(relx=0.33, rely=0.28,height=21, relwidth=0.51)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")

        course = StringVar()
        self.box = ttk.Combobox(self.Labelframe1, textvariable=course, state="readonly")
        self.box['values'] = ("B.Tech.","MCA","M.Tech.")
        self.box.current(0)
        self.box.place(relx=0.33, rely=0.41, height=21, relwidth=0.51)
        self.box.configure(background="white")
        self.box.configure(font="TkTextFont")

        branch = StringVar()
        self.box1 = ttk.Combobox(self.Labelframe1, textvariable=branch, state="readonly")
        self.box1['values'] = ("CS","IT","ECE","ME","Civil","EN","None")
        self.box1.current(0)
        self.box1.place(relx=0.33, rely=0.53, height=21, relwidth=0.51)
        self.box1.configure(background="white")
        self.box1.configure(font="TkTextFont")

        year = StringVar()
        self.box2 = ttk.Combobox(self.Labelframe1, textvariable=year, state="readonly")
        self.box2['values'] = ("1", "2", "3", "4")
        self.box2.current(0)
        self.box2.place(relx=0.33, rely=0.66, height=21, relwidth=0.51)
        self.box2.configure(background="white")
        self.box2.configure(font="TkTextFont")

        sem = StringVar()
        self.box1 = ttk.Combobox(self.Labelframe1, textvariable=sem, state="readonly")
        self.box1['values'] = ("1", "2", "3", "4","5","6","7","8")
        self.box1.current(0)
        self.box1.place(relx=0.33, rely=0.78, height=21, relwidth=0.51)
        self.box1.configure(background="white")
        self.box1.configure(font="TkTextFont")


        self.Button1 = Button(self.Labelframe1,command=lambda:add(name,number,course,branch,year,sem))
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


