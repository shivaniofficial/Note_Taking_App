from tkinter import *
from tkinter import messagebox
from NoteDB import NoteDB
from dashboard import Dashboard
if __name__=="__main__":
    try:
        #Add Your Database username and password here
        db=NoteDB(username="root",password="shiv")
        Dashboard().initUI(db)
    except Exception as e:
        print(e)
