import tkinter as tk
from tkinter import *

s = tk.Tk()
s.title("fgvdfbg")
s.geometry('400x500')

def reset():
    Entry_umur.delete(0, END)
    Entry_Tumur.delete(0, END)
    Entry_jumlah.delete(0, END)

# magicmethod
# klu tak guna, guna nama biasa jak, tukar dkt command juga
# magicmethod

# def __add__():
#     try:
#         umur = int(Entry_umur.get())
#         Tumur = int(Entry_Tumur.get())
#         total = umur + Tumur
#         Entry_jumlah.delete(0, END)
#         Entry_jumlah.insert(0, str(total))
#     except ValueError:
#         Entry_jumlah.delete(0, END)
#         Entry_jumlah.insert(0, "Invalid input")
        
 
 # manual
 
def add_umur():
        try:
            umur = int(Entry_umur.get())
            Tumur = int(Entry_Tumur.get())
            total = umur + Tumur
            Entry_jumlah.delete(0, END)
            Entry_jumlah.insert(0, str(total))
        except ValueError:
            Entry_jumlah.delete(0, END)
            Entry_jumlah.insert(0, "Invalid input")


# label
label_umur = tk.Label(s, text="Umur :")
label_umur.grid(row=1, column=1, pady=0)

label_Tumur = tk.Label(s, text=" Tambah Umur:")
label_Tumur.grid(row=2, column=1, pady=0)

label_jumlah = tk.Label(s, text=" Jumlah Umur:")
label_jumlah.grid(row=3, column=1, pady=0)

# textbox
Entry_umur = tk.Entry(s, text="Umur:")
Entry_umur.grid(row=1, column=2, pady=0)

Entry_Tumur = tk.Entry(s, text="Tambah Umur:")
Entry_Tumur.grid(row=2, column=2, pady=0)

Entry_jumlah = tk.Entry(s, text="Jumlah Umur:")
Entry_jumlah.grid(row=3, column=2, pady=0)

# button
kira = tk.Button(s, text="count", command=add_umur)
kira.grid(row=4, column=1, padx=2, pady=5)

clear = tk.Button(s, text="clear", command=reset)
clear.grid(row=4, column=2, padx=2, pady=5)

keluar = tk.Button(s, text="keluar", command=quit)
keluar.grid(row=4, column=4, padx=3, pady=5)

s.mainloop()
