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

import Home
import pymysql
import connect
conn=connect.connect()
cur=conn.cursor()
from tkinter import messagebox
import Statistics

def vp_start_gui():
    global val, w, root
    root = Tk()
    top = Returned_Books (root)
    root.mainloop()

w = None
def create_Registered_Books(root, *args, **kwargs):
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Returned_Books (w)

    return (w, top)

def switch_frame(top,frame_class):
    top.destroy()
    frame_class.vp_start_gui()

def clear():
    try:
        sql="delete from Return_book"
        cur.execute(sql)
        conn.commit()
        messagebox.showinfo("Success", "List Cleared Successfully")
    except Exception as e:
        messagebox.showinfo("Error", e)

class Returned_Books:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'

        top.geometry("826x450+354+180")
        top.title("Returned Books")




        '''self.Button1 = Button(self.Frame1,command=lambda:switch_frame(top,Home))
        self.Button1.place(relx=0.78, rely=0.0, height=25, width=147)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(background="#a0d9d9")
        self.Button1.configure(borderwidth="2")
        self.Button1.configure(text="Go Back to Home")
        self.Button1.configure(width=147)'''

        self.Button1 = Button(top, command=lambda: switch_frame(top, Statistics))
        self.Button1.place(relx=0.05, rely=0.85, height=35, width=147)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(background="#a0d9d9")
        self.Button1.configure(borderwidth="3")
        self.Button1.configure(text='''Back''')
        self.Button1.configure(width=147)

        self.Button1 = Button(top, command=lambda: clear())
        self.Button1.place(relx=0.25, rely=0.85, height=35, width=147)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(background="#a0d9d9")
        self.Button1.configure(borderwidth="3")
        self.Button1.configure(text='''Clear List''')
        self.Button1.configure(width=147)

        conn = connect.connect()
        cur = conn.cursor()
        sql="select * from Return_book"
        cur.execute(sql)
        data=cur.fetchall()
        height = len(data)+1
        width = 5
        self.t=Entry(top)
        head=["Book_Id","Student Number","Date of Issue","Date of Return"]

        for i in range(height):  # Rows
            for j in range(width):  # Columns
                self.b = Entry(top,justify="center")
                if i==0:
                    if j==0:
                        self.b.insert(len("S.No."), "S.No.")
                    else:
                        self.b.insert(len(head[j-1]),head[j-1])
                else:
                    if j == 0:
                        self.b.insert(len(str(i)),i)
                    else:
                        self.b.insert(len(str(data[i-1][j-1])),data[i-1][j-1])
                self.b.grid(row=i, column=j)
                self.b.configure(state="readonly")






if __name__ == '__main__':
    vp_start_gui()


