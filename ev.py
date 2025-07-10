from tkinter import *
window = Tk()
window.title("EVENT HANDLERSSSSSSSS")
window.geometry('100x100')
def handle_keypress(event):
    print(event.char)
window.bind("<Key>",handle_keypress)
def handle_click(event):
    print("\nTHE BUTTON WAS DELETED")
btn = Button(text="Click Me!")
btn.pack()
btn.bind("<Button-1>",handle_click)       
window.mainloop()