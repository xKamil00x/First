import tkinter as tk
from tkinter import ttk

def clickMe():
    if(action.cget('text')=="asdfasdf"):
        action.configure(text="First")
    else:
        action.configure(text="asdfasdf")
    aLabel.configure(foreground='red')
    print(action.cget('text'))
win = tk.Tk()
win.title('First Program')
aLabel= ttk.Label(win, text="First")
aLabel.grid(column=0,row=0)

action =ttk.Button(win,text="Click ME!", command = clickMe)
action.grid(column=1,row=0)



win.mainloop()