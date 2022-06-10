from tkinter import *

root = Tk()
root.title("lambda on command")
root.geometry("285x200")
root.option_add("*font", "tahoma 10 bold")
root.option_add("*foreground", "navy")

frame = Frame(root)
frame.config(background="gold")
frame.place(width=285, height=200, x=0, y=0)

label1 = Label(frame, text="Customer Type", width=30, bg="gold")
label1.grid(column=0,row=0, columnspan=2, padx=5, pady=5)
show_msg = StringVar()
label2 = Label(frame, width=30, textvariable=show_msg)
label2.grid(column=0, row=2, columnspan=2, padx=5, pady=5)


def button_action(widget):
    customer_type = {1:"major", 2:"senior"}
    if widget == r1 or widget == r2:
        show_msg.set(customer_type[radio_var.get()])
    if widget == button1:
        show_msg.set("")
        radio_var.set(0)
    if widget == button2:
        sys.exit(0)


radio_var = IntVar()
r1 = Radiobutton(frame, text="major", width=10, variable=radio_var, value=1, bg="gold",
                 command=lambda: button_action(r1))
r1.grid(column=0, row=1, padx=15, pady=15)
r2 = Radiobutton(frame, text="senior",  width=10, variable=radio_var,  value=2, bg="gold",
                 command=lambda: button_action(r2))
r2.grid(column=1, row=1, padx=15, pady=15)

button1 = Button(frame,  text="ล้างข้อมูล",  width=12, command=lambda: button_action(button1))
button1.grid(column=0, row=3, padx=10, pady=10)
button2 = Button(frame,  text="จบการทำงาน",  width=12, command=lambda: button_action(button2))
button2.grid(column=1, row=3, padx=10, pady=10)
root.mainloop()
