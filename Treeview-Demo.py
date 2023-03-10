# Treeview Demo
from tkinter import *
from tkinter import ttk
win = Tk()
win.resizable(width=False, height=False)

spalten=["0","1","2","3"]
tv = ttk.Treeview(win, columns=spalten, height=6, show="headings")

tv.heading("0", text="Vorname")
tv.heading("1", text="Nachname")
tv.heading("2", text="Kontostand")
tv.heading("3", text="Telefon")

tv.column("0", width=75)
tv.column("1", width=75, anchor = "w")
tv.column("2", width=70, anchor = "e")
tv.column("3", width=100, anchor = "center")

ds0=["Hans", "Hansmann",345, "0228-768971226"]
ds1=["Otto", "Knarrsack",250, "0228-768911176"]
ds2=["Helga", "Helgafels",1345, "0228-7689111876"]
ds3=["Kalle", "Klawitter",3245, "0228-768911876"]
ds4=["Otto", "Schulz",2510, "0228-7689761111"]
ds5=["Greta", "Lachsberg",145, "0228-767897876"]

tv.insert("", END, values=ds0)
tv.insert("", END, values=ds1)
tv.insert("", END, values=ds2)
tv.insert("", END, values=ds3)
tv.insert("", END, values=ds4)
tv.insert("", END, values=ds5)
tv.pack(padx=20, pady=20)
win.mainloop()