from tkinter import *
root = Tk()
root.title("HELLO! WELCOME TO NUMBERPAD.")
root.geometry('250X300')
frame = Frame(master=root, height=200, width=360,bg = "#d0efff")
nums = [[9,8,7],[6,5,4],[3,2,1]['#',0,'*']]
for i in range(4):
    root.columnconfigure(i,weight=1,minsize=75)
    root.rowconfigure(i,weight=1,minsize=50)
    for a in range(0,3):
        frame = Frame(master=root, relief=SUNKEN, borderwidth=1)
        frame.grid(row=i,column=a)
        label = Label(master=frame,text=nums[i][a],bg = "#d0efff")
        label.pack(padx=3,pady=3)
root.mainloop()        