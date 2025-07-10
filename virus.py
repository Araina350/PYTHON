from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('250x300')
def msg():
    messagebox.showwarning("Alert","Stop! Virus Found")
btn = Button(root, text="SCAN FOR A VIRUS", command=msg)    
btn.place(x=40,y=80)
root.mainloop()