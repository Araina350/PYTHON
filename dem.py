from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
window = Tk()
window.title("DENOMINATION CALCULATOR")
window.geometry('500x500')
label = Label(window,text="HEY User! Welcome to the DENOMINATION CALCULATOR ",bg = "light blue")
label.place(relx=0.5,rely=340)
def msg():
    msgbox = messagebox.showinfo("Alert!","Do you want to calculate the denomination amount?")
    if msgbox == "ok":
        topwin()
buttonst = Button(window,text="Let's get started",command=msg)   
buttonst.place(x=260,y=360)  
def topwin():
    top = Toplevel()
    top.title("Denominations Calculator")   
    top.geometry("600x350+50+50")
    label1 = Label(top, text="ENTER TOTAL AMOUNT",bg="light grey")
    Entry = (top)
    label2 = Label(top,text="HERE ARE THE NUMBER OF NOTES FOR EACH DENOMINATION",bg = "light grey")
    l1 = Label(top, text="500",bg="light grey") 
    l2 = Label(top, text="200",bg="light grey") 
    l3 = Label(top, text="100",bg="light grey") 
    l4 = Label(top, text="20",bg="light grey") 
    l5 = Label(top, text="10",bg="light grey") 
    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    t4 = Entry(top)
    t5 = Entry(top)
def calculator():
    try    