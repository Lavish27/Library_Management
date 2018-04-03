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
import Statistics
'''conn=connect.connect()
cur=conn.cursor()'''

def vp_start_gui():
    global val, w, root
    root = Tk()
    top = Registered_Students (root)
    root.mainloop()

w = None
def create_Registered_Books(root, *args, **kwargs):
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Registered_Students (w)

    return (w, top)

def switch_frame(top,frame_class):
    top.destroy()
    frame_class.vp_start_gui()


class Registered_Students:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'

        top.geometry("1150x450+180+180")
        top.title("Registered Students")


        self.Button1 = Button(top, command=lambda: switch_frame(top, Statistics))
        self.Button1.place(relx=0.02, rely=0.90, height=35, width=147)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(background="#a0d9d9")
        self.Button1.configure(borderwidth="3")
        self.Button1.configure(text='''Back''')
        self.Button1.configure(width=147)

        conn = connect.connect()
        cur = conn.cursor()
        sql="select * from Student"
        cur.execute(sql)
        data=cur.fetchall()
        height = len(data)+1
        width = 7
        self.t=Entry(top)
        head=["Name","Student Number","Course","Branch","Year","Semester"]

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


