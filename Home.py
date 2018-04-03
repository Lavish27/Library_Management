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

import New_Book
import New_Student
import Issue
import Return
import Statistics
import Remove_Book
import Remove_Student

def vp_start_gui():
    global val, w, root
    root = Tk()
    top = Home (root)
    root.mainloop()

w = None
def create_Home(root, *args, **kwargs):
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Home (w)
    return (w, top)

def switch_frame(top,frame_class):
    top.destroy()
    frame_class.vp_start_gui()


class Home:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font10 = "-family {DejaVu Sans} -size 22 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font12 = "-family {DejaVu Sans} -size 15 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font13 = "-family {DejaVu Sans} -size 12 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"

        top.geometry("749x555+320+118")
        top.title("Home")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=0.14, relwidth=1.01)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d6d9d9")
        self.Frame1.configure(width=755)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.19, rely=0.27, height=49, width=586)
        self.Label1.configure(font=font10)
        self.Label1.configure(foreground="#00b1e0")
        self.Label1.configure(text='''SMART LIBRARY MANAGEMENT SYSTEM''')
        self.Label1.configure(width=586)

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.01, rely=-0.30, height=119, width=116)
        self._img1 = PhotoImage(file="./images/logo.png")
        self.Label2.configure(image=self._img1)
        self.Label2.photo=self._img1
        self.Label2.configure(width=116)

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)



        self.Labelframe1 = LabelFrame(top)
        self.Labelframe1.place(relx=0.04, rely=0.15, relheight=0.40
                , relwidth=0.92)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(borderwidth="4")
        self.Labelframe1.configure(font=font12)
        self.Labelframe1.configure(foreground="#d36c00")
        self.Labelframe1.configure(text='''Operation''')
        self.Labelframe1.configure(highlightcolor="#b84b13")
        self.Labelframe1.configure(width=690)

        self.Label3 = Label(self.Labelframe1)
        self.Label3.place(relx=0.18, rely=0.15, height=129, width=156)
        self._img2 = PhotoImage(file="./images/newbook.png")
        self.Label3.configure(image=self._img2)
        self.Label3.photo = self._img2
        self.Label3.configure(width=156)

        self.Label4 = Label(self.Labelframe1)
        self.Label4.place(relx=0.60, rely=0.15, height=129, width=156)
        self._img3 = PhotoImage(file="./images/newstudent.png")
        self.Label4.configure(image=self._img3)
        self.Label4.photo = self._img3
        self.Label4.configure(width=156)

        self.Button4 = Button(self.Labelframe1,command=lambda:switch_frame(top,New_Book))
        self.Button4.place(relx=0.15, rely=0.84, height=27, width=100)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(background="#acc9f8")
        self.Button4.configure(borderwidth="2")
        self.Button4.configure(foreground="#d36c00")
        self.Button4.configure(text='''Add Book''')

        self.Button5 = Button(self.Labelframe1,command=lambda:switch_frame(top,New_Student))
        self.Button5.place(relx=0.56, rely=0.84, height=27, width=100)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(background="#acc9f8")
        self.Button5.configure(borderwidth="2")
        self.Button5.configure(foreground="#d36c00")
        self.Button5.configure(text='''Add Student''')

        self.Button6 = Button(self.Labelframe1,command=lambda:switch_frame(top,Remove_Book))
        self.Button6.place(relx=0.32, rely=0.84, height=27, width=100)
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(background="#acc9f8")
        self.Button6.configure(foreground="#d36c00")
        self.Button6.configure(text='Remove Book')

        self.Button7 = Button(self.Labelframe1, command=lambda: switch_frame(top, Remove_Student))
        self.Button7.place(relx=0.73, rely=0.84, height=27, width=113)
        self.Button7.configure(activebackground="#d9d9d9")
        self.Button7.configure(background="#acc9f8")
        self.Button7.configure(borderwidth="2")
        self.Button7.configure(foreground="#d36c00")
        self.Button7.configure(text='''Remove Student''')

        self.Labelframe2 = LabelFrame(top)
        self.Labelframe2.place(relx=0.04, rely=0.56, relheight=0.40
                , relwidth=0.92)
        self.Labelframe2.configure(relief=GROOVE)
        self.Labelframe2.configure(borderwidth="4")
        self.Labelframe2.configure(font=font13)
        self.Labelframe2.configure(foreground="#8e1896")
        self.Labelframe2.configure(text='''Action''')
        self.Labelframe2.configure(width=630)

        self.Label9 = Label(self.Labelframe2)
        self.Label9.place(relx=0.03, rely=0.15, height=129, width=156)
        self._img5 = PhotoImage(file="./images/Study-icon.png")
        self.Label9.configure(image=self._img5)
        self.Label9.photo = self._img5
        self.Label9.configure(width=56)

        self.Label10 = Label(self.Labelframe2)
        self.Label10.place(relx=0.35, rely=0.15, height=129, width=156)
        self._img6 = PhotoImage(file="./images/return_icon.png")
        self.Label10.configure(image=self._img6)
        self.Label10.photo = self._img6
        self.Label10.configure(width=36)

        self.Label11 = Label(self.Labelframe2)
        self.Label11.place(relx=0.7, rely=0.15, height=129, width=156)
        self._img7 = PhotoImage(file="./images/statistics.png")
        self.Label11.configure(image=self._img7)
        self.Label11.photo = self._img7

        self.Button1 = Button(self.Labelframe2,command=lambda:switch_frame(top,Issue))
        self.Button1.place(relx=0.04, rely=0.84, height=27, width=137)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(background="#d38900")
        self.Button1.configure(borderwidth="2")
        self.Button1.configure(foreground="#8e1896")
        self.Button1.configure(text='''Issue Book''')
        self.Button1.configure(width=137)

        self.Button2 = Button(self.Labelframe2,command=lambda:switch_frame(top,Return))
        self.Button2.place(relx=0.36, rely=0.84, height=27, width=137)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(background="#d38900")
        self.Button2.configure(borderwidth="2")
        self.Button2.configure(foreground="#8e1896")
        self.Button2.configure(text='''Return Book''')
        self.Button2.configure(width=117)

        self.Button3 = Button(self.Labelframe2,command=lambda:switch_frame(top,Statistics))
        self.Button3.place(relx=0.71, rely=0.84, height=27, width=137)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(background="#d38900")
        self.Button3.configure(borderwidth="2")
        self.Button3.configure(foreground="#8e1896")
        self.Button3.configure(text='''Statistics''')
        self.Button3.configure(width=117)






if __name__ == '__main__':
    vp_start_gui()


