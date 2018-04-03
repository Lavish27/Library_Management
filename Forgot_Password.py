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
import Login
import connect

def vp_start_gui():
    global val, w, root
    root = Tk()
    top = Forgot_Password (root)
    #FP_support.init(root, top)
    root.mainloop()

w = None
conn=connect.connect()
cur=conn.cursor()

def create_Forgot_Password(root, *args, **kwargs):
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Forgot_Password (w)
    return (w, top)

def switch_frame(top,frame_class):
    top.destroy()
    frame_class.vp_start_gui()

def search(Text1,Text2,username):
    try:
        sql='select Name,sec_q from Account where Username=%s'
        cur.execute(sql,(str(username.get())))
        data=cur.fetchall()
        if data:
            Text1.configure(state=NORMAL)
            Text1.insert(len(data[0][0]),data[0][0])
            Text1.configure(state=DISABLED)
            Text2.configure(state=NORMAL)
            Text2.insert(len(data[0][1]), data[0][1])
            Text2.configure(state=DISABLED)
        else:
            messagebox.showinfo("Try Again", "Incorrect Username")
    except Exception as e:
        messagebox.showinfo("Error",e)

def retrieve(Text4,username,ans):
    try:
        sql='select Password from Account where Username=%s and Answer=%s'
        cur.execute(sql,(str(username.get()),str(ans.get())))
        data=cur.fetchall()
        if data:
            Text4.configure(state=NORMAL)
            Text4.insert(len(data[0][0]), data[0][0])
            Text4.configure(state=DISABLED)
        else:
            messagebox.showinfo("Try Again", "Incorrect Answer")
    except Exception as e:
        messagebox.showinfo("Error", e)

class Forgot_Password:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font10 = "-family {DejaVu Sans} -size 10 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font9 = "-family {DejaVu Sans} -size 16 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("600x450+459+187")
        top.title("Forgot Password")



        self.Labelframe1 = LabelFrame(top)
        self.Labelframe1.place(relx=0.05, rely=0.07, relheight=0.83
                , relwidth=0.88)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(font=font9)
        self.Labelframe1.configure(foreground="#db0000")
        self.Labelframe1.configure(text='''Retrieve Password''')
        self.Labelframe1.configure(highlightbackground="#41d9d9")
        self.Labelframe1.configure(highlightcolor="#ff0000")
        self.Labelframe1.configure(width=530)

        self.Label1 = Label(self.Labelframe1)
        self.Label1.place(relx=0.02, rely=0.13, height=19, width=106)
        self.Label1.configure(font=font10)
        self.Label1.configure(text='''Username''')
        self.Label1.configure(width=106)

        username=StringVar()
        self.Entry1 = Entry(self.Labelframe1,textvariable=username)
        self.Entry1.place(relx=0.34, rely=0.13,height=21, relwidth=0.41)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(width=216)

        self.Label2 = Label(self.Labelframe1)
        self.Label2.place(relx=0.02, rely=0.27, height=19, width=76)
        self.Label2.configure(font=font10)
        self.Label2.configure(text='''Name''')
        self.Label2.configure(width=76)

        self.Text1 = Entry(self.Labelframe1)
        self.Text1.place(relx=0.34, rely=0.27, relheight=0.07, relwidth=0.41)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(state=DISABLED)
        self.Text1.configure(width=216)

        self.Label3 = Label(self.Labelframe1)
        self.Label3.place(relx=0.04, rely=0.4, height=19, width=126)
        self.Label3.configure(font=font10)
        self.Label3.configure(text='''Security Question''')
        self.Label3.configure(width=126)

        self.Text2 = Entry(self.Labelframe1)
        self.Text2.place(relx=0.34, rely=0.4, relheight=0.07, relwidth=0.41)
        self.Text2.configure(background="white")
        self.Text2.configure(font="TkTextFont")
        self.Text2.configure(selectbackground="#c4c4c4")
        self.Text2.configure(state=DISABLED)
        self.Text2.configure(width=216)

        self.Label4 = Label(self.Labelframe1)
        self.Label4.place(relx=0.04, rely=0.53, height=21, width=72)
        self.Label4.configure(font=font10)
        self.Label4.configure(text='''Answer''')
        self.Label4.configure(width=72)

        ans=StringVar()
        self.Text3 = Entry(self.Labelframe1,textvariable=ans)
        self.Text3.place(relx=0.34, rely=0.53, relheight=0.07, relwidth=0.41)
        self.Text3.configure(background="white")
        self.Text3.configure(font="TkTextFont")
        self.Text3.configure(selectbackground="#c4c4c4")
        self.Text3.configure(width=216)


        self.Label5 = Label(self.Labelframe1)
        self.Label5.place(relx=0.02, rely=0.67, height=21, width=129)
        self.Label5.configure(font=font10)
        self.Label5.configure(text='''Your Password''')
        self.Label5.configure(width=129)

        self.Text4 = Entry(self.Labelframe1)
        self.Text4.place(relx=0.34, rely=0.67, relheight=0.07, relwidth=0.43)
        self.Text4.configure(background="white")
        self.Text4.configure(font="TkTextFont")
        self.Text4.configure(selectbackground="#c4c4c4")
        self.Text4.configure(width=226)
        self.Text4.configure(state=DISABLED)

        self.Button1 = Button(self.Labelframe1,command=lambda:search(self.Text1,self.Text2,username))
        self.Button1.place(relx=0.77, rely=0.11, height=37, width=97)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(background="#b0d9d9")
        self.Button1.configure(borderwidth="4")
        self.Button1.configure(text='''Search''')
        self.Button1.configure(width=97)

        self.Button2 = Button(self.Labelframe1,command=lambda:retrieve(self.Text4,username,ans))
        self.Button2.place(relx=0.77, rely=0.51, height=37, width=97)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(background="#a4d9d9")
        self.Button2.configure(borderwidth="4")
        self.Button2.configure(text='''Retrieve''')
        self.Button2.configure(width=97)

        self.Button3 = Button(self.Labelframe1,command=lambda:switch_frame(top,Login))
        self.Button3.place(relx=0.77, rely=0.64, height=37, width=97)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(background="#aed9d9")
        self.Button3.configure(borderwidth="4")
        self.Button3.configure(text='''Back''')
        self.Button3.configure(width=97)






if __name__ == '__main__':
    vp_start_gui()


