from tkinter import *
from tkinter import ttk, messagebox
class RestaurantOrderManagement:
    def __init__(self,root):
        self.root = root
        self.root.title("Restaurant Management App")
        self.menu_items = {"FRENCH FRIES":2,"LUNCH MEAL":2,"BURGER":3,"PIZZA":4,"DRINKS":1}
        self.exchange = 84
        frame = ttk.Frame(root)
        frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
        ttk.Label(frame,text="Restaurant Order Management",font=("Arial",20,"Bold")).grid(row=0,columnspan=3,padx=10,pady=10)
        self.menu_labels={}
        self.menu_quantities={}
        for i ,(item,price) in enumerate (self.menu_items.items(),start=1):
            label = ttk.Label(frame,text="f{item} (${price}):",font=("Arial",12))
if __name__  == "__main__":
    root = tk.Tk()
    app = RestaurantOrderManagement(root)
    root.geometry("800x600")
