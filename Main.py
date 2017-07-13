import tkinter as tk
from lib2to3.fixes import fix_throw
from tkinter import ttk

def clickMe():
    aLabel.configure(text=name.get())
win = tk.Tk()
win.title('First Program')
aLabel= ttk.Label(win, text="First")
aLabel.grid(column=0,row=0)

action =ttk.Button(win,text="Click ME!", command = clickMe)
action.grid(column=1,row=0)

name=tk.StringVar()
xtext = ttk.Entry(win,width = 12, textvariable=name)
xtext.grid(column=0,row=2)



win.mainloop()