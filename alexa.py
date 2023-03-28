from tkinter import *
from tkinter import ttk
import time, os, subprocess
import other_funcs

def button1():
    time.sleep(1)
    subprocess.run(["python", "D:/Coursework/Mod-4/ChatBot/jarvis.py"], shell=True)

def button2():
    other_funcs.say_it(f"Goodbye, have a nice day!")
    exit()
    time.sleep(2)
    win.destroy()

win  = Tk()
win.geometry("900x600")
win.resizable(False, False)
win.title("You personal Jarvis")
win.wm_iconbitmap("D:/Coursework/Mod-4/ChatBot/jarvis.ico")

bg = PhotoImage(file = "D:/Coursework/Mod-4/ChatBot/ironman.png")
bg = bg.subsample(2, 2)
label1 = Label(win, image=bg)
label1.pack(expand=True)
label1.bind("<Configure>", lambda e: label1.config(width=e.width, height=e.height))

myButton1 = Button(win, text = "Run Jarvis", 
bg = '#0052cc', fg = '#ffffff', font= 'Helvetica 14', command = button1)
myButton1.config(height=2, width = 20)
myButton1.place(x = 200, y = 450)

myButton2 = Button(win, text = "Quit Jarvis", 
bg = '#0052cc', fg = '#ffffff', font= 'Helvetica 14', command = button2)
myButton2.config(height=2, width = 20)
myButton2.place(x = 500, y = 450)


win.mainloop()