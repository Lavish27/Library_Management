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


def vp_start_gui():
    global val, w, root
    root = Tk()
    top = Statistics (root)
    root.mainloop()

w = None
import Reg_Books
import Reg_Students
import Issued_Books
import Returned_Books
import Home

def create_Statistics(root, *args, **kwargs):
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Statistics (w)
    return (w, top)

def switch_frame(top,frame_class):
    top.destroy()
    frame_class.vp_start_gui()


class Statistics:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'

        top.geometry("587x500+446+150")
        top.title("Statistics")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.09, rely=0.04, relheight=0.92, relwidth=0.84)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="4")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(width=495)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.1, rely=0.05, height=129, width=156)
        self._img1 = PhotoImage(file="./images/bookshelf-icon.png")
        self.Label1.configure(image=self._img1)
        self.Label1.configure(text='''Label''')
        self.Label1.configure(width=146)

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.63, rely=0.05, height=129, width=156)
        self._img2 = PhotoImage(file="./images/engineer-icon.png")
        self.Label2.configure(image=self._img2)

        self.Button1 = Button(self.Frame1,command=lambda:switch_frame(top,Reg_Books))
        self.Button1.place(relx=0.14, rely=0.35, height=27, width=117)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(background="#a9cbd9")
        self.Button1.configure(borderwidth="2")
        self.Button1.configure(text='''Registered Books''')
        self.Button1.configure(width=117)

        self.Button2 = Button(self.Frame1,command=lambda:switch_frame(top,Reg_Students))
        self.Button2.place(relx=0.65, rely=0.35, height=27, width=137)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(background="#a9cbd9")
        self.Button2.configure(borderwidth="2")
        self.Button2.configure(text='''Registered Students''')
        self.Button2.configure(width=137)

        self.Label3 = Label(self.Frame1)
        self.Label3.place(relx=0.1, rely=0.50, height=129, width=156)
        self._img3 = PhotoImage(file="./images/books-icon.png")
        self.Label3.configure(image=self._img3)

        self.Label4 = Label(self.Frame1)
        self.Label4.place(relx=0.63, rely=0.50, height=129, width=156)
        self._img4 = PhotoImage(file="./images/images1.png")
        self.Label4.configure(image=self._img4)
        self.Label4.photo=self._img4
        self.Label4.configure(text='''Label''')

        self.Button3 = Button(self.Frame1,command=lambda:switch_frame(top,Issued_Books))
        self.Button3.place(relx=0.14, rely=0.80, height=27, width=117)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(background="#a9cbd9")
        self.Button3.configure(borderwidth="2")
        self.Button3.configure(text='''Issued Books''')
        self.Button3.configure(width=117)

        self.Button4 = Button(self.Frame1,command=lambda:switch_frame(top,Returned_Books))
        self.Button4.place(relx=0.67, rely=0.80, height=27, width=117)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(background="#a9cbd9")
        self.Button4.configure(borderwidth="2")
        self.Button4.configure(text='''Returned Books''')
        self.Button4.configure(width=117)

        self.Button5 = Button(self.Frame1, command=lambda: switch_frame(top, Home))
        self.Button5.place(relx=0.40, rely=0.90, height=27, width=117)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(background="#a9cbd9")
        self.Button5.configure(borderwidth="2")
        self.Button5.configure(text='''Go To Home''')
        self.Button5.configure(width=117)





if __name__ == '__main__':
    vp_start_gui()


