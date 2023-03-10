# Treeview Demo
from tkinter import *
from tkinter import ttk
win = Tk()

spalten=["0","1","2"]
tv = ttk.Treeview(win, columns=spalten, height=3, show="headings")

tv.heading("0", text="Vorname")
tv.heading("1", text="Nachname")
tv.heading("2", text="Kontostand")

tv.column("0", width=75)
tv.column("1", width=75, anchor = "center")
tv.column("2", width=70, anchor = "center")

ds0=["Hans", "Hansmann",345]
ds1=["Otto", "Knarrsack",250]
ds2=["Helga", "Helgafels",1345]

tv.insert("", END, values=ds0)
tv.insert("", END, values=ds1)
tv.insert("", END, values=ds2)

tv.pack(padx=20, pady=20)
win.mainloop()