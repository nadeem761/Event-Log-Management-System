from tkinter import *
from tkinter import ttk, messagebox
import pymysql

class SignUp:
    def __init__(self, root):
        self.window = root
        self.window.title("Event Log Management System Registration Form is")
        self.window.geometry("1280x800+0+0")
        self.window.config(bg = "white")

        self.frame1 = Frame(self.window, bg="yellow")
        self.frame1.place(x=0, y=0, width=450, relheight=1)

        label1 = Label(self.frame1, text="Event", font=("times new roman", 40, "bold"), bg="yellow", fg="red").place( x=100, y=300)
        label2 = Label(self.frame1, text="Log", font=("times new roman", 40, "bold"), bg="yellow", fg="RoyalBlue1").place(x=240, y=300)
        label3 = Label(self.frame1, text="System", font=("times new roman", 30, "bold"), bg="yellow",fg="brown4").place(x=100, y=360)


        frame = Frame(self.window, bg="white")
        frame.place(x=520,y=100,width=500,height=550)

        title1 = Label(frame, text="Sign Up", font=("times new roman",25,"bold"),bg="white").place(x=20, y=10)

        f_name = Label(frame, text="First name", font=("helvetica",15,"bold"),bg="white").place(x=20, y=100)
        l_name = Label(frame, text="Last name", font=("helvetica",15,"bold"),bg="white").place(x=240, y=100)

        self.fname_txt = Entry(frame,font=("arial"))
        self.fname_txt.place(x=20, y=130, width=200)

        self.lname_txt = Entry(frame,font=("arial"))
        self.lname_txt.place(x=240, y=130, width=200)

        email = Label(frame, text="Email", font=("helvetica",15,"bold"),bg="white").place(x=20, y=180)

        self.email_txt = Entry(frame,font=("arial"))
        self.email_txt.place(x=20, y=210, width=420)

        sec_question = Label(frame, text="Security questions", font=("helvetica",15,"bold"),bg="white").place(x=20, y=260)
        answer = Label(frame, text="Answer", font=("helvetica",15,"bold"),bg="white").place(x=240, y=260)

        self.questions = ttk.Combobox(frame,font=("helvetica",13),state='readonly',justify=CENTER)
        self.questions['values'] = ("Select","What's your pet name?","Your first teacher name","Your birthplace", "Your favorite movie")
        self.questions.place(x=20,y=290,width=200)
        self.questions.current(0)

        self.answer_txt = Entry(frame,font=("arial"))
        self.answer_txt.place(x=240, y=290, width=200)

        password =  Label(frame, text="New password", font=("helvetica",15,"bold"),bg="white").place(x=20, y=340)

        self.password_txt = Entry(frame,font=("arial"))
        self.password_txt.place(x=20, y=370, width=420)

        self.signup = Button(frame,text="Sign Up",command=self.signup_func,font=("times new roman",18, "bold"),bd=0,cursor="hand2",bg="green2",fg="white").place(x=20,y=470,width=150)

        self.create_button = Button(text="Login", command=self.redirect_window, font=("times new roman", 18, "bold"), bd=0, cursor="hand2", bg="green2", fg="white").place(x=750, y=570, width=170)


    def signup_func(self):
        if self.fname_txt.get()=="" or self.lname_txt.get()=="" or self.email_txt.get()=="" or self.questions.get()=="Select" or self.answer_txt.get()=="" or self.password_txt.get() == "":
            messagebox.showerror("Error!","Sorry!, All fields are required",parent=self.window)


        else:
            try:
                connection = pymysql.connect(host="localhost", user="nadeem", password="nadeem345", database="eventlog")
                cur = connection.cursor()
                cur.execute("select * from student_register where email=%s",self.email_txt.get())
                row=cur.fetchone()


                if row!=None:
                    messagebox.showerror("Error!","The email id is already exists, please try again with another email id",parent=self.window)
                else:
                    cur.execute("insert into student_register (f_name,l_name,email,question,answer,password) values(%s,%s,%s,%s,%s,%s)",
                                    (
                                        self.fname_txt.get(),
                                        self.lname_txt.get(),
                                        self.email_txt.get(),
                                        self.questions.get(),
                                        self.answer_txt.get(),

                                        self.password_txt.get()
                                    ))
                    connection.commit()
                    connection.close()
                    messagebox.showinfo("Congratulations!","Register Successful",parent=self.window)
                    self.reset_fields()
            except Exception as e:
                messagebox.showerror("Error!",f"Error due to {str(e)}",parent=self.window)

    def redirect_window(self):
        self.window.destroy()
        from login_page import login_page
        root = Tk()
        obj = login_page(root)
        root.mainloop()

    def reset_fields(self):
        self.fname_txt.delete(0, END)
        self.lname_txt.delete(0, END)
        self.email_txt.delete(0, END)
        self.questions.current(0)
        self.answer_txt.delete(0, END)
        self.password_txt.delete(0, END)



if __name__ == "__main__":
    root = Tk()
    obj = SignUp(root)
    root.mainloop()
