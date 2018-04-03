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

import time
import threading
import Login

def vp_start_gui():
    global val, w, root
    root = Tk()
    top =Loading (root)



    root.mainloop()

w = None

import Home

def create_Loading(root, *args, **kwargs):
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Loading (w)
    return (w, top)

def switch_frame(top,frame_class):
    top.destroy()
    frame_class.vp_start_gui()



class Loading:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font10 = "-family {DejaVu Sans} -size 24 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font12 = "-family {DejaVu Sans} -size 12 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+468+229")
        top.title("Welcome")



        self.Label1 = Label(top)
        self.Label1.place(relx=0.1, rely=0.11, height=89, width=486)
        self.Label1.configure(font=font10)
        self.Label1.configure(foreground="#088b88")
        self.Label1.configure(text='''Welcome to Smart Library''')
        self.Label1.configure(width=486)



        self.Label2 = Label(top)
        self.Label2.place(relx=0.23, rely=0.58, height=150, width=330)
        self._img1 = PhotoImage(file="./images/download.png")
        self.Label2.configure(image=self._img1)
        self.Label2.photo=self._img1
        self.Label2.configure(text='''Label''')
        self.Label2.configure(width=226)

        '''self.progress = ttk.Progressbar(top,orient="horizontal",mode='determinate')
        self.progress.place(relx=0.22, rely=0.40, relwidth=0.58
                , relheight=0.0, height=19)
        self.progress.configure(length="350")
        self.progress.configure(cursor="X_cursor")
        #self.TProgressbar1["maximum"]=100'''
        '''def progressbar():
            for progress in range(0,101,2):
                self.TProgressbar1["value"] = progress
                time.sleep(0.1
            #switch_frame(top,Login)'''

        #threading.Thread(target=progressbar).start()

        # self.Button1 = Button(top,command=lambda:progressbar(top,self.TProgressbar1))
        self.Button1 = Button(top,command=lambda:switch_frame(top,Home))
        self.Button1.place(relx=0.36, rely=0.34, height=35, width=147)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(background="#a0d9d9")
        self.Button1.configure(borderwidth="3")
        self.Button1.configure(text='Click Here To Proceed ')
        self.Button1.configure(width=147)


        '''self.Label3 = Label(top)
        self.Label3.place(relx=0.58, rely=0.45, height=19, width=126)
        self.Label3.configure(font=font12)
        self.Label3.configure(text='Please Wait...')
        self.Label3.configure(width=126)'''

    '''def traitement(self,top):
        def real_traitement():
            #self.progress.grid(row=1, column=0)
            self.progress.start()
            time.sleep(5)
            self.progress.stop()
            self.progress.grid_forget()

            #self.Button1['state'] = 'normal'

        #threading.Thread(target=real_traitement).join()

        #self.Button1['state'] = 'disabled'
        threading.Thread(target=real_traitement).start()
        switch_frame(top, Home)'''


if __name__ == '__main__':
    vp_start_gui()





