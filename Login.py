#! /usr/bin/env python

from tkinter import messagebox

import Signup
import Forgot_Password
import connect
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

import pymysql
import Loading


def vp_start_gui():
    global val, w, root
    root = Tk()
    top = Login (root)
    #login_support.init(root, top)
    root.mainloop()

w = None

conn=connect.connect()
cur=conn.cursor()

def create_Login(root, *args, **kwargs):
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Login (w)
    return (w, top)

def switch_frame(top,frame_class):
    top.destroy()
    frame_class.vp_start_gui()

def login(top,username,passw):
    try:
        sql="select * from Account where Username=%s and Password=%s"
        cur.execute(sql,(str(username.get()),str(passw.get())))
        data=cur.fetchall()
        if data:
            cur.close()
            conn.close()
            switch_frame(top,Loading)

        else:
            messagebox.showinfo("Try Again", "Incorrect username or password")
    except Exception as e:
        messagebox.showinfo("Error", e)



class Login:
    def __init__(self,top=None,):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font11 = "-family {DejaVu Sans} -size 20 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font13 = "-family {DejaVu Sans} -size 12 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"

        top.geometry("600x450+459+187")
        top.title("Login")



        self.Labelframe1 = LabelFrame(top)
        self.Labelframe1.place(relx=0.07, rely=0.07, relheight=0.87
                , relwidth=0.89)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(font=font11)
        self.Labelframe1.configure(foreground="#0000f0")
        self.Labelframe1.configure(text='''Login''')
        self.Labelframe1.configure(highlightcolor="#0000f6")
        self.Labelframe1.configure(width=540)

        self.Label1 = Label(self.Labelframe1)
        self.Label1.place(relx=0.06, rely=0.22, height=29, width=116)
        self.Label1.configure(font=font13)
        self.Label1.configure(text='''Username''')
        self.Label1.configure(width=116)

        username =  StringVar()
        self.Text1 = Entry(self.Labelframe1, textvariable=username)
        self.Text1.place(relx=0.35, rely=0.22, relheight=0.07, relwidth=0.44)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(selectbackground="#c4c4c4")
        #self.Text1.configure(setgrid="1")
        self.Text1.configure(width=236)


        self.Label2 = Label(self.Labelframe1)
        self.Label2.place(relx=0.07, rely=0.38, height=19, width=86)
        self.Label2.configure(font=font13)
        self.Label2.configure(text='''Password''')
        self.Label2.configure(width=86)

        passw=StringVar()
        self.Entry1 = Entry(self.Labelframe1,show='*', textvariable=passw)
        self.Entry1.place(relx=0.35, rely=0.38,height=26, relwidth=0.44)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(width=236)

        self.Button1 = Button(self.Labelframe1, command=lambda:login(top,username,passw))
        self.Button1.place(relx=0.26, rely=0.58, height=37, width=97)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(background="#5ed9d9")
        self.Button1.configure(borderwidth="4")
        self.Button1.configure(text='''Login''')
        self.Button1.configure(width=97)


        self.Button2 = Button(self.Labelframe1,command=lambda:switch_frame(top,Signup))
        self.Button2.place(relx=0.52, rely=0.58, height=37, width=107)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(background="#58d9d9")
        self.Button2.configure(borderwidth="4")
        self.Button2.configure(foreground="#000003")
        self.Button2.configure(text='''Signup''')
        self.Button2.configure(width=107)

        self.Button3 = Button(self.Labelframe1,command=lambda:switch_frame(top,Forgot_Password))
        self.Button3.place(relx=0.33, rely=0.74, height=47, width=167)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(background="#3bd9d9")
        self.Button3.configure(borderwidth="4")
        self.Button3.configure(text='''Forgot Password''')
        self.Button3.configure(width=167)






if __name__ == '__main__':
    vp_start_gui()


