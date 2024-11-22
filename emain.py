from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import subprocess
from mail import send_msg,aotp,skey,j
from backend import *
import mysql.connector as s

db=s.connect(
    host='localhost',
    user='root',
    password='tiger',
    database='project')   #cursor object = myc
myc=db.cursor()

def _next_(call):
    for i in main_win.winfo_children():
        i.destroy()
    if stack[-1]==call:
        pass
    else:
        stack.append(call)

def back():
    for i in main_win.winfo_children():
        i.destroy()
    stack.pop()
    stack[-1]()

def signup(uname,pwd,desig):
    qry='INSERT INTO login (uname,password,Designation) VALUES(%s,%s,%s)'
    value=(uname,pwd,desig)
    myc.execute(qry,value)
    db.commit()

def signin():
    global choices,frames
    _next_(signin)
    frames =Frame(main_win)
    frames.pack()
    back_btn=Button(main_win,text=" ⬅️ ",command=back)
    Label6=Label(frames,text="INVENTO",font=('Times',50,"bold"),bg="black",fg="white")
    Label6.pack()
    label8=Label(frames,text="Grow your business by our extensive Inventory Management system",font=('Arial',10,"italic"))
    label8.pack()
    framez= LabelFrame(frames,padx=100,pady=100)
    framez.pack(padx=50,pady=50)
    Label7 = Label(framez, text=" Enter Username:")
    Label7.pack()
    unames = Entry(framez,width=50, borderwidth=5)
    unames.pack()
    Label10 = Label(framez, text=" Password:")
    Label10.pack()
    upass = Entry(framez,width=50,borderwidth=5,show="*")
    upass.pack()
    Label20 = Label(framez, text=" Enter email:")
    Label20.pack()
    umail=Entry(framez,width=50,borderwidth=5)
    umail.pack()
    Label22 = Label(framez, text="Phone no.:")
    Label22.pack()
    phno=Entry(framez,width=50,borderwidth=5)
    phno.pack()
    Label20 = Label(framez, text=" Select Designation:")
    Label20.pack()

    choices=['Manager','Accountant']
    option=ttk.Combobox(framez,values=choices)
    option.pack(padx=50)
    label14=Label(framez, text="*Please Sign Up to continue*", font=("Courier",6,"bold"))
    label14.pack()

    def oreo():
        global um,up,ou,un,phn,pd
        un=str(unames.get())
        up=str(upass.get())
        um=str(umail.get())
        ou=str(option.get())
        phn=str(phno.get())
        pd=str(upass.get())
        if len(un)==0 or len(up)==0 or len(um)==0 or len(phn)!=10:
            messagebox.showerror("Sigin Error","Error:Invalid input")
        else:
            try:
                if ou==choices[0]:
                    if get_emp_desig()==None:
                        send_msg(um,un)
                        otpwin()
                    else:
                        messagebox.showerror("Manager Exists","Manager account already exists")
                        
                else:
                    query0="select Email, employee_name from employee Where Designation='Manager';"
                    myc.execute(query0)
                    db_result=myc.fetchall()
                    
                    if db_result==[]:
                        messagebox.showerror("No Manager Available","Please Create a Manager account")

                    else:
                        skey(db_result[0][0],db_result[0][1],un)
                        actemp()
                        otpwin()
            except:
                
                messagebox.showerror("Sigin Error","Error:Invalid input")    

            
    button21=Button(framez,text="Sign Up",command=oreo)
    button21.pack()
    back_btn.place(x=-5,y=0)


def login(uname,pwd):
    query=f"SELECT * FROM login WHERE uname='{uname}' and password='{pwd}'"
    myc.execute(query)
    db_result=myc.fetchall()
    if db_result==[]:
        messagebox.showerror("Login Error","Error:Incorrect Login or Password")
    else:
        main_win.destroy()
        n=[]
        for ip in db_result[0]:
            n.append(ip)
        if n[3]=="Manager":
            subprocess.run(["python","MASTER\\manager.py"])
        else:
            subprocess.run(["python","MASTER\\account.py"])

def win():

    window=Frame(main_win)
    window.pack()

    Label1=Label(window,text="INVENTO",font=('Times',50,"bold"),bg="black",fg="white")
    Label1.pack()

    label2=Label(window,text="Grow your business by our extensive Inventory Management system",font=('Arial',10,"italic"))
    label2.pack()

    frame= LabelFrame(window,padx=100,pady=100)
    frame.pack(padx=50,pady=50)

    Label3 = Label(frame, text=" Enter Username:")
    Label3.pack()
    e = Entry(frame,width=50, borderwidth=5)
    e.pack()

    Label3 = Label(frame, text=" Password:")
    Label3.pack()
    f = Entry(frame,width=50,borderwidth=5,show="*")
    f.pack()

    label4=Label(frame, text="*Please Log in to continue*", font=("Courier",6,"bold"))
    label4.pack()

    def check():
        uname=e.get()
        pwd=f.get()
        login(uname,pwd)

    btn = Button(frame, text="Log In",command=check)
    btn.pack() #button to enter the next window

    btnsgnin=Button(frame,text="Sign Up",command=signin)
    btnsgnin.pack()

    label5= Label(window,text="Team invento©",fg= "Black" ,font=('Times',15,"italic"))
    label17=Label(window,text="Innovating Miracles",fg= "Black" ,font=('Times',10,"italic"))
    label5.pack()
    label17.pack()

def actemp():
    qry='INSERT INTO tempac(namet,email,phno,passw,desig,skey) VALUES(%s,%s,%s,%s,%s,%s)'
    valu=(un,um,phn,pd,ou,j)
    myc.execute(qry,valu)
    db.commit()



def otpwin():
    _next_(otpwin)
    back_btn=Button(main_win,text=" ⬅️ ",command=back)
    back_btn.place(x=0,y=0)
    def verify():
        ot=str(otp.get())
        if ot==aotp:
            Add_emp(un,phn,um,"NULL",ou)
            signup(un,up,ou)
            main_win.destroy()
            subprocess.run(["python","MASTER\\manager.py"])     
        else:            
            messagebox.showerror('SignUp Error', 'Error: Incorrect OTP')
    
    if ou==choices[0]:
        if get_emp_desig()==None:
            frames.destroy()
            otpwind=Frame(main_win)
            otpwind.pack()
            label31=Label(otpwind,text="An otp has been sent kindly check you mail inbox")
            label31.pack()
            otp = Entry(otpwind,width=50,borderwidth=5)
            otp.pack()
            verifbtn=Button(otpwind,text="Verify", command=verify)
            verifbtn.pack()
        else:
            messagebox.showerror("Manager Exists","Manager account already exists")
    elif ou==choices[1]:
        back()
        messagebox.showinfo("REQUEST SENT !","A request has been sent to the manager and he will shortly reply")
    else:
        messagebox.showerror("Error","One or more unspecified columns")

main_win =Tk()
main_win.title("INVENTO")
main_win.iconbitmap("MASTER\\shopping-basket.ico")
main_win.geometry("1000x800")

win()
stack =[win]

main_win.mainloop()