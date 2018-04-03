import pymysql as db
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk

def connect():
    try:
        conn = db.connect(host='localhost', user='root', password='6972', db='Library')
        return conn
    except ConnectionError as e:
        messagebox.showinfo("Connection Error",e)
        return None


