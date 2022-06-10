from tkinter import *

root = Tk()
root.title("GUI Example")
root.geometry("300x250")
root.option_add('*font', 'tahoma 10 bold')
frame = Frame(root)
frame.config(background="cyan")
frame.place(width=300, height=250, x=0, y=0)
root.mainloop()
