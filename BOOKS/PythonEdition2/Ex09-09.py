from tkinter import *
from tkinter.ttk import Combobox

root = Tk()
root.title("GUI Example")
root.geometry("300x250")
root.option_add('*font', 'tahoma 10 bold')
frame = Frame(root)
frame.config(background="cyan")
frame.place(width=300, height=250, x=0, y=0)
root.option_add("*foreground", "navy")
label1 = Label(frame, text="***** Book List *****", bg="cyan")
label1.place(width=150, height=30, x=80, y=20)
combo1 = Combobox(frame, width=20)
combo1.place(width=150, x=80, y=50)
booklist = ["python", "java", "C", "PHP", "Access", "Excel"]
combo1['values'] = booklist
combo1.current(0)
root.mainloop()
