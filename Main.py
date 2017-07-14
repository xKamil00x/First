import tkinter as tk
from lib2to3.fixes import fix_throw
from tkinter import ttk

def clickMe():

    aLabel.configure(text=name.get())
    printConsole()

def printConsole():
    print(name.get(),number.get())

#create windows
win = tk.Tk()
win.title('First Program')
#create label
aLabel= ttk.Label(win, text="First")
aLabel.grid(column=0,row=0)
#create button
action =ttk.Button(win,text="Click ME!", command = clickMe)
action.grid(column=2,row=1)
#create textField and focus on him
name=tk.StringVar()
xtext = ttk.Entry(win,width = 12, textvariable=name)
xtext.grid(column=0,row=1)
xtext.focus()

# Create Combobox and aLabel
labelCheckbox= ttk.Label(win, text="Choose a number").grid(column=1,row=0)
number = tk.IntVar()
numberChosen=ttk.Combobox(win,width=12, textvariable=number)
numberChosen['values']=(2,3,4,5,6)
numberChosen.grid(column=1,row=1)






win.mainloop()