from tkinter import *
from datetime import date
window = Tk()
window.title("HELlo")
window.geometry('400x300')
lb1 = Label(text = 'HEY THERE!',fg = 'white',bg = 'blue')
lb2 = Label(text = 'ENTER FULL NAME',fg = 'white',bg = 'lightblue')
ent1 = Entry()
def display():
    name = ent1.get()
    global message
    message = "WELCOME!\nTODAY'S DATE IS"
    greet = "CELLO" +name+ "\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())
text_box = Text(height=3)
btn = Button(text="BEGIN",command=display,height=1,bg = "#1261A0",fg = "white")  
lb1.pack()
lb2.pack()
ent1.pack()
text_box.pack()
btn.pack()
window.mainloop()
