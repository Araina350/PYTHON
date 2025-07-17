import tkinter as tk
import re
def check_password_strength():
    password = password_entry
    lower_c = re.compile(r'[a-z]')
    uc = re.compile(r'[A-Z]')
    digits = re.compile(r'[0-9]')
    special_c = re.compile(r'[^a-zA-Z0-9]')
    min_length = 8
    if len(password) < min_length:
        strength_label.config(text="PASSWORD IS TOO SHORT.MINIMUM LENGTH SHOULD BE{}CHARACTERS".format(min_length),fg="red")
        return
    if not lower_c.search(password):
        strength_label.config(text="PASSWORD MUST CONTAIN ATLEAST 1 LOWER CASE LETTER.",fg="red")
        return
    if not uc.search(password):
        strength_label.config(text="PASSWORD MUST CONTAIN ATLEAST 1 UPPER CASE LETTER.",fg="red")
        return
    if not digits.search(password):
        strength_label.config(text="PASSWORD MUST CONTAIN ATLEAST 1 NUMBER.",fg="red" )
        return
    if not special_c.search(password):
        strength_label.config(text="PASSWORD MUST CONTAIN ATLEAST 1 SPECIAL CHARACTER.",fg="red")
        return
    strength_label.config(text="PASSWORD IS STRONG",fg="green")
root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400") 
password_label =  tk.Label(root, text="ENTER PASSWORD:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()
c_btn = tk.Button(root, text="CHECK STRENGTH", command=check_password_strength)
c_btn.pack()
strength_label = tk.Label(root,text=" ",fg="black")
strength_label.pack
root.mainloop()