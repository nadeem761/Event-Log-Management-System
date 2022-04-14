from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
root = Tk()
root.geometry('1280x800+0+0')
root.title("Log In To Event Log Management System")
root.frame1 = Frame(root, bg="white")
root.frame1.place(x=200, y=2, width=800, height=500)
min_w = 50
max_w = 200
cur_width = min_w
expanded = False



def func():
    print("button is pressed")
def expand():
    global cur_width, expanded
    cur_width += 10
    rep = root.after(5, expand)
    frame.config(width=cur_width)
    if cur_width >= max_w:
        expanded = True
        root.after_cancel(rep)
        fill()


def contract():
    global cur_width, expanded
    cur_width -= 10
    rep = root.after(5, contract)
    frame.config(width=cur_width)
    if cur_width <= min_w:
        expanded = False
        root.after_cancel(rep)
        fill()


def fill():
    if expanded:

        application_b.config(text='Application Events', image='', font=(0, 16))
        system_b.config(text='System Events', image='', font=(0, 16))
        security_b.config(text='Security Events', image='', font=(0, 16))
        setting_b.config(text='Settings', image='', font=(0, 16))
        help_b.config(text='Help', image='', font=(0, 16))
    else:

        application_b.config(image=application, font=(0, 16))
        system_b.config(image=system, font=(0, 16))
        security_b.config(image=security, font=(0, 16))
        setting_b.config(image=setting, font=(0, 16))
        help_b.config(image=help, font=(0, 16))


application = ImageTk.PhotoImage(Image.open('application.png').resize((40, 40), Image.ANTIALIAS))
system = ImageTk.PhotoImage(Image.open('system.png').resize((40, 40), Image.ANTIALIAS))
security = ImageTk.PhotoImage(Image.open('security.png').resize((40, 40), Image.ANTIALIAS))
setting = ImageTk.PhotoImage(Image.open('settings.png').resize((40, 40), Image.ANTIALIAS))
help = ImageTk.PhotoImage(Image.open('help.png').resize((40, 40), Image.ANTIALIAS))

root.update()
frame = Frame(root, bg='orange', width=50, height=root.winfo_height())
frame.grid(row=0, column=0)

application_b = Button(frame, image=application, bg='orange', relief='flat', command= system )
system_b = Button(frame, image=system, bg='orange', relief='flat')
security_b = Button(frame, image=security, bg='orange', relief='flat')
setting_b = Button(frame, image=setting, bg='orange', relief='flat')
help_b = Button(frame, image=help, bg='orange', relief='flat')


application_b.grid(row=0, column=0, pady=10)
system_b.grid(row=1, column=0, pady=20)
security_b.grid(row=2, column=0, pady=30)
setting_b.grid(row=3, column=0, pady=40)
help_b.grid(row=4, column=0, pady=35)


frame.bind('<Enter>', lambda e: expand())
frame.bind('<Leave>', lambda e: contract())
frame.grid_propagate(False)

root.mainloop()
