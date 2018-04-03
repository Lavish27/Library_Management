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
import Home
import pymysql
import connect
conn=connect.connect()
cur=conn.cursor()

def vp_start_gui():
    global val, w, root
    root = Tk()
    top = Issue_Book (root)
    root.mainloop()

w = None
def switch_frame(top,frame_class):
    top.destroy()
    frame_class.vp_start_gui()

def create_Issue_Book(root, *args, **kwargs):
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Issue_Book (w)
    return (w, top)

def destroy_Issue_Book():
    global w
    w.destroy()
    w = None

def book(id,e2,e3,e4,e5,e6):
    try:
        sql="select * from Book where Book_Id=%s"
        cur.execute(sql,(int(id.get())))
        data=cur.fetchall()
        if data:
            e2.configure(state="normal")
            e2.insert(len(data[0][1]),data[0][1])
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
            messagebox.showinfo("Try Again", "Book not Registered")
    except Exception as e:
        messagebox.showinfo("Error",e)

def student(number,e2,e3,e4,e5,e6):
    try:
        sql="select * from Student where Student_Number=%s"
        cur.execute(sql,(int(number.get())))
        data=cur.fetchall()
        if data:
            e2.configure(state="normal")
            e2.insert(len(data[0][0]),data[0][0])
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
            messagebox.showinfo("Try Again", "Student not Registered")
    except Exception as e:
        messagebox.showinfo("Error",e)

def issue(id,number,date):
    try:
        sql="insert into issue values(%s,%s,%s)"
        cur.execute(sql,(int(id.get()),int(number.get()),str(date.get())))
        conn.commit()
        messagebox.showinfo("Success", "Book Issued")

    except pymysql.IntegrityError as e:
        messagebox.showinfo("Try Again", "Book Already Issued")
    except Exception as e:
        messagebox.showinfo("Error", e)



class Issue_Book:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font10 = "-family {DejaVu Sans} -size 15 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font9 = "-family {DejaVu Sans} -size 11 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("1060x519+200+150")
        top.title("Issue Book")
        top.configure(highlightcolor="black")



        self.Labelframe1 = LabelFrame(top)
        self.Labelframe1.place(relx=0.02, rely=0.06, relheight=0.68
                , relwidth=0.48)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(font=font10)
        self.Labelframe1.configure(foreground="#bb0000")
        self.Labelframe1.configure(text='''Book Details''')
        self.Labelframe1.configure(width=510)

        self.Label1 = Label(self.Labelframe1)
        self.Label1.place(relx=0.05, rely=0.17, height=19, width=66)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(font=font9)
        self.Label1.configure(text='''Book Id''')

        self.Label2 = Label(self.Labelframe1)
        self.Label2.place(relx=0.06, rely=0.31, height=19, width=66)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(font=font9)
        self.Label2.configure(text='''Name''')
        self.Label2.configure(width=126)

        self.Label3 = Label(self.Labelframe1)
        self.Label3.place(relx=0.06, rely=0.45, height=19, width=66)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(font=font9)
        self.Label3.configure(text='''Edition''')

        self.Label4 = Label(self.Labelframe1)
        self.Label4.place(relx=0.06, rely=0.59, height=22, width=66)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(font=font9)
        self.Label4.configure(text='''Publisher''')

        self.Label5 = Label(self.Labelframe1)
        self.Label5.place(relx=0.06, rely=0.73, height=22, width=66)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(font=font9)
        self.Label5.configure(text='''Price''')

        self.Label6 = Label(self.Labelframe1)
        self.Label6.place(relx=0.06, rely=0.87, height=22, width=66)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(font=font9)
        self.Label6.configure(text='''Pages''')
        self.Label6.configure(width=76)

        id=StringVar()
        self.Entry1 = Entry(self.Labelframe1,textvariable=id)
        self.Entry1.place(relx=0.31, rely=0.17,height=21, relwidth=0.48)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(selectbackground="#c4c4c4")

        self.Entry2 = Entry(self.Labelframe1)
        self.Entry2.place(relx=0.31, rely=0.31,height=21, relwidth=0.48)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(selectbackground="#c4c4c4")
        READONLY = 'readonly'
        self.Entry2.configure(state=READONLY)

        self.Entry3 = Entry(self.Labelframe1)
        self.Entry3.place(relx=0.31, rely=0.45,height=21, relwidth=0.48)
        self.Entry3.configure(background="white")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(selectbackground="#c4c4c4")
        READONLY = 'readonly'
        self.Entry3.configure(state=READONLY)

        self.Entry4 = Entry(self.Labelframe1)
        self.Entry4.place(relx=0.31, rely=0.59,height=21, relwidth=0.48)
        self.Entry4.configure(background="white")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(selectbackground="#c4c4c4")
        READONLY = 'readonly'
        self.Entry4.configure(state=READONLY)

        self.Entry5 = Entry(self.Labelframe1)
        self.Entry5.place(relx=0.31, rely=0.73,height=21, relwidth=0.48)
        self.Entry5.configure(background="white")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(selectbackground="#c4c4c4")
        READONLY = 'readonly'
        self.Entry5.configure(state=READONLY)

        self.Entry6 = Entry(self.Labelframe1)
        self.Entry6.place(relx=0.31, rely=0.87,height=21, relwidth=0.48)
        self.Entry6.configure(background="white")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(selectbackground="#c4c4c4")
        READONLY = 'readonly'
        self.Entry6.configure(state=READONLY)

        self.Button1 = Button(self.Labelframe1,command=lambda:book(id,self.Entry2,self.Entry3,self.Entry4,self.Entry5,self.Entry6))
        self.Button1.place(relx=0.82, rely=0.17, height=27, width=77)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(background="#aed9d9")
        self.Button1.configure(borderwidth="3")
        self.Button1.configure(text='''Search''')
        self.Button1.configure(width=77)

        self.Labelframe2 = LabelFrame(top)
        self.Labelframe2.place(relx=0.52, rely=0.06, relheight=0.68
                , relwidth=0.46)
        self.Labelframe2.configure(relief=GROOVE)
        self.Labelframe2.configure(font=font10)
        self.Labelframe2.configure(foreground="#08a6f3")
        self.Labelframe2.configure(text='''Student Details''')
        self.Labelframe2.configure(width=490)

        self.Label7 = Label(self.Labelframe2)
        self.Label7.place(relx=0.04, rely=0.17, height=19, width=124)
        self.Label7.configure(font=font9)
        self.Label7.configure(text='''Student Number''')
        self.Label7.configure(width=76)

        number=StringVar()
        self.Entry7 = Entry(self.Labelframe2,textvariable=number)
        self.Entry7.place(relx=0.31, rely=0.17,height=21, relwidth=0.48)
        self.Entry7.configure(background="white")
        self.Entry7.configure(font="TkFixedFont")
        self.Entry7.configure(width=236)

        self.Label8 = Label(self.Labelframe2)
        self.Label8.place(relx=0.04, rely=0.31, height=22, width=66)
        self.Label8.configure(font=font9)
        self.Label8.configure(text='''Name''')

        self.Entry8 = Entry(self.Labelframe2)
        self.Entry8.place(relx=0.31, rely=0.31,height=21, relwidth=0.48)
        self.Entry8.configure(background="white")
        self.Entry8.configure(font="TkFixedFont")
        READONLY = 'readonly'
        self.Entry8.configure(state=READONLY)

        self.Label9 = Label(self.Labelframe2)
        self.Label9.place(relx=0.04, rely=0.45, height=19, width=66)
        self.Label9.configure(font=font9)
        self.Label9.configure(text='''Course''')
        self.Label9.configure(width=46)

        self.Entry9 = Entry(self.Labelframe2)
        self.Entry9.place(relx=0.31, rely=0.45,height=21, relwidth=0.48)
        self.Entry9.configure(background="white")
        self.Entry9.configure(font="TkFixedFont")
        READONLY = 'readonly'
        self.Entry9.configure(state=READONLY)

        self.Label10 = Label(self.Labelframe2)
        self.Label10.place(relx=0.04, rely=0.59, height=19, width=66)
        self.Label10.configure(font=font9)
        self.Label10.configure(text='''Branch''')
        self.Label10.configure(width=46)

        self.Entry10 = Entry(self.Labelframe2)
        self.Entry10.place(relx=0.31, rely=0.59,height=21, relwidth=0.48)
        self.Entry10.configure(background="white")
        self.Entry10.configure(font="TkFixedFont")
        READONLY = 'readonly'
        self.Entry10.configure(state=READONLY)

        self.Label11 = Label(self.Labelframe2)
        self.Label11.place(relx=0.04, rely=0.73, height=22, width=66)
        self.Label11.configure(font=font9)
        self.Label11.configure(text='''Year''')

        self.Entry11 = Entry(self.Labelframe2)
        self.Entry11.place(relx=0.31, rely=0.73,height=21, relwidth=0.48)
        self.Entry11.configure(background="white")
        self.Entry11.configure(font="TkFixedFont")
        READONLY = 'readonly'
        self.Entry11.configure(state=READONLY)

        self.Label12 = Label(self.Labelframe2)
        self.Label12.place(relx=0.04, rely=0.87, height=22, width=74)
        self.Label12.configure(font=font9)
        self.Label12.configure(text='''Semester''')

        self.Entry12 = Entry(self.Labelframe2)
        self.Entry12.place(relx=0.31, rely=0.87,height=21, relwidth=0.48)
        self.Entry12.configure(background="white")
        self.Entry12.configure(font="TkFixedFont")
        READONLY = 'readonly'
        self.Entry12.configure(state=READONLY)

        self.Button2 = Button(self.Labelframe2,command=lambda:student(number,self.Entry8,self.Entry9,self.Entry10,self.Entry11,self.Entry12))
        self.Button2.place(relx=0.84, rely=0.17, height=31, width=72)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(background="#aed9d9")
        self.Button2.configure(borderwidth="3")
        self.Button2.configure(text='''Search''')

        self.Label13 = Label(top)
        self.Label13.place(relx=0.51, rely=0.77, height=19, width=126)
        self.Label13.configure(font=font9)
        self.Label13.configure(text='''Date of Issue''')
        self.Label13.configure(width=126)

        date=StringVar()
        self.Entry13 = Entry(top,textvariable=date)
        self.Entry13.place(relx=0.64, rely=0.77,height=21, relwidth=0.2)
        self.Entry13.configure(background="white")
        self.Entry13.configure(font="TkFixedFont")
        self.Entry13.configure(width=216)

        self.Button3 = Button(top,command=lambda:issue(id,number,date))
        self.Button3.place(relx=0.38, rely=0.89, height=37, width=107)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(background="#e19826")
        self.Button3.configure(borderwidth="4")
        self.Button3.configure(text='''Issue''')
        self.Button3.configure(width=107)

        self.Button4 = Button(top,command=lambda:switch_frame(top,Home))
        self.Button4.place(relx=0.54, rely=0.89, height=37, width=127)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(background="#e19826")
        self.Button4.configure(borderwidth="4")
        self.Button4.configure(text='''Go Back to Home''')
        self.Button4.configure(width=127)

        self.Label14 = Label(top)
        self.Label14.place(relx=0.86, rely=0.77, height=19, width=66)
        self.Label14.configure(justify=LEFT)
        self.Label14.configure(text='''dd-mm-yy''')
        self.Label14.configure(width=66)






if __name__ == '__main__':
    vp_start_gui()


