from tkinter import *
import tkinter.ttk as ttk
import csv

root = Tk()
root.title("Event log management system csv Table")
width = 1280
height = 800
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)

TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("id","date","user", "pc", "activity"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('id', text="id", anchor=W)
tree.heading('date', text="date", anchor=W)
tree.heading('user', text="user", anchor=W)
tree.heading('pc', text="pc", anchor=W)
tree.heading('activity', text="activity", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=200)
tree.column('#2', stretch=NO, minwidth=0, width=200)
tree.column('#3', stretch=NO, minwidth=0, width=300)
tree.column('#4', stretch=NO, minwidth=0, width=200)
tree.column('#5', stretch=NO, minwidth=0, width=300)
tree.pack()

with open('device.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        id = row['id']
        date = row['date']
        user = row['user']
        pc = row['pc']
        activity = row['activity']
        tree.insert("", 0, values=(id,date,user,pc,activity))


if __name__ == '__main__':
    root.mainloop()