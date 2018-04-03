#! /usr/bin/env python
import sys

import Login
import connect
import pymysql


try:
    from Tkinter import *
except ImportError:
    from tkinter import *
from tkinter import messagebox

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1


def vp_start_gui():
    global val, w, root
    root = Tk()
    top = Signup (root)
    #Signup_support.init(root, top)
    root.mainloop()

w = None
conn=connect.connect()
cur=conn.cursor()
def create_Signup(root, *args, **kwargs):
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Signup (w)
    Signup_support.init(w, top, *args, **kwargs)
    return (w, top)

def switch_frame(top,frame_class):
    top.destroy()
    frame_class.vp_start_gui()

def insert(username,name,passw,sec,ans):
    try:
        sql = "insert into Account values(%s,%s,%s,%s,%s)"
        cur.execute(sql,(str(username.get()),str(name.get()),str(passw.get()),str(sec.get()),str(ans.get())))
        conn.commit()
        cur.close()
        conn.close()
        messagebox.showinfo("Success","New Account created")
    except pymysql.IntegrityError as e:
        messagebox.showinfo("Try again", "Username already exist")
    except Exception as e:
        messagebox.showinfo("Error",e)



class Signup:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font11 = "-family {DejaVu Sans} -size 12 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font12 = "-family {DejaVu Sans} -size -12 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {DejaVu Sans} -size 16 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("600x450+459+187")
        top.title("Signup")



        self.Labelframe1 = LabelFrame(top)
        self.Labelframe1.place(relx=0.07, rely=0.04, relheight=0.88
                , relwidth=0.88)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(font=font9)
        self.Labelframe1.configure(foreground="#000080")
        self.Labelframe1.configure(text='''New Account''')
        self.Labelframe1.configure(takefocus="5")
        self.Labelframe1.configure(width=530)

        self.Label1 = Label(self.Labelframe1)
        self.Label1.place(relx=0.09, rely=0.13, height=29, width=86)
        self.Label1.configure(font=font11)
        self.Label1.configure(text='''Username''')
        self.Label1.configure(width=86)

        username = StringVar()
        self.Text1 = Entry(self.Labelframe1, textvariable=username)
        self.Text1.place(relx=0.38, rely=0.13, relheight=0.07, relwidth=0.48)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(width=256)
        #self.Text1.configure(wrap=WORD)


        self.Label2 = Label(self.Labelframe1)
        self.Label2.place(relx=0.08, rely=0.25, height=19, width=76)
        self.Label2.configure(font=font11)
        self.Label2.configure(text='''Name''')
        self.Label2.configure(width=76)

        name = StringVar()
        self.Text2 = Entry(self.Labelframe1,textvariable=name)
        self.Text2.place(relx=0.38, rely=0.25, relheight=0.07, relwidth=0.48)
        self.Text2.configure(background="white")
        self.Text2.configure(font="TkTextFont")
        self.Text2.configure(selectbackground="#c4c4c4")
        self.Text2.configure(width=256)


        self.Label3 = Label(self.Labelframe1)
        self.Label3.place(relx=0.09, rely=0.38, height=19, width=86)
        self.Label3.configure(font=font11)
        self.Label3.configure(text='''Password''')
        self.Label3.configure(width=86)

        passw = StringVar()
        self.Entry1 = Entry(self.Labelframe1,show='*', textvariable=passw)
        self.Entry1.place(relx=0.38, rely=0.38,height=21, relwidth=0.48)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(width=256)


        self.Label4 = Label(self.Labelframe1)
        self.Label4.place(relx=0.08, rely=0.51, height=19, width=156)
        self.Label4.configure(font=font11)
        self.Label4.configure(text='''Security Question''')
        self.Label4.configure(width=156)

        sec = StringVar()
        self.box = ttk.Combobox(self.Labelframe1,textvariable=sec, state="readonly")
        self.box['values'] = ("What is your favourite subject ?", "What is your favourite picnic spot ?","Who is your favourite writer/poet ?", "What is your first school's name ?","What is your pet's name ?")
        self.box.current(0)
        self.box.place(relx=0.38, rely=0.51, relheight=0.07, relwidth=0.48)
        self.box.configure(background="white")
        self.box.configure(font="TkTextFont")
        #self.box.configure(selectbackground="#c4c4c4")
        self.box.configure(width=256)
        #self.box.configure(wrap=WORD)


        self.Label5 = Label(self.Labelframe1)
        self.Label5.place(relx=0.04, rely=0.63, height=19, width=116)
        self.Label5.configure(font=font11)
        self.Label5.configure(text='''Answer''')
        self.Label5.configure(width=116)

        ans = StringVar()
        self.Text4 = Entry(self.Labelframe1, textvariable=ans)
        self.Text4.place(relx=0.38, rely=0.63, relheight=0.07, relwidth=0.48)
        self.Text4.configure(background="white")
        self.Text4.configure(font="TkTextFont")
        self.Text4.configure(selectbackground="#c4c4c4")
        self.Text4.configure(width=256)


        self.Button1 = Button(self.Labelframe1,command=lambda:insert(username,name,passw,sec,ans))
        self.Button1.place(relx=0.28, rely=0.78, height=37, width=97)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(background="#3ed9d9")
        self.Button1.configure(borderwidth="4")
        self.Button1.configure(font=font12)
        self.Button1.configure(text='''Create''')
        self.Button1.configure(width=97)

        self.Button2 = Button(self.Labelframe1,command=lambda:switch_frame(top,Login))
        self.Button2.place(relx=0.58, rely=0.78, height=37, width=97)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(background="#31d9d9")
        self.Button2.configure(borderwidth="4")
        self.Button2.configure(text='''Back''')
        self.Button2.configure(width=97)






if __name__ == '__main__':
    vp_start_gui()


