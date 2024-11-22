from tkinter import *
from tkinter import ttk
from ecalc import Calculator
from backend import *
from tkinter import messagebox
import subprocess
import os
from PIL import ImageTk,Image

window = Tk()
window.geometry("1360x702")
window.title("INVENTO")
window.iconbitmap("MASTER\\shopping-basket.ico")

def _next_(call):
    for i in Frame1.winfo_children():
        i.destroy()
    if stack[-1]==call:
        pass
    else:
        stack.append(call)

def back():
    for i in Frame1.winfo_children():
        i.destroy()
    stack.pop()
    stack[-1]()

def refresh():
    for i in Frame1.winfo_children():
        i.destroy()
    stack[-1]()
    
def delall():
    truncate_all()
    window.destroy()
    subprocess.run(["python","MASTER\\emain.py"])

def Logout():
    window.destroy()
    subprocess.run(["python","MASTER\\emain.py"])

menu = Menu(window)
window.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label="Options",menu=file_menu)
file_menu.add_command(label="Refresh",command=refresh)
file_menu.add_command(label="Exit",command=window.destroy)
file_menu.add_command(label="LogOut",command=Logout)
file_menu.add_command(label="Reset",command=delall)

accessories_menu = Menu(menu)
menu.add_cascade(label="Accessories",menu=accessories_menu)
accessories_menu.add_command(label="Calculator",command=Calculator)

def customer():
    _next_(customer)
    Labelx = Label(Frame1, text="----Customer Panel----",font=('Times',10,"bold"))
    Labelx.pack()
    Label_ = Label(Frame1, text="")
    Label_.pack()
    Label1 = Label(Frame1, text="Search Customer by one or more of the following fields",font=('Times',10,"bold"))
    Label1.pack()

    def execute():
        Frami=LabelFrame(Frame1)
        Frami.place(x=0,y=350,width=1181,height=345)
        _Label_ = Label(Frami, text="")
        _Label_.place(x=540,y=0)
        
        lst = check_cust(a.get(),b.get(),c.get())

        if len(lst)!=0 :
            s = ttk.Style()
            s.theme_use('clam')
            s.configure('Treeview', rowheight=40)

            tree = ttk.Treeview(Frami, column=("c1", "c2", "c3"), show='headings', height=5)

            tree.column("# 1", anchor=CENTER)
            tree.heading("# 1", text="NAME")
            tree.column("# 2", anchor=CENTER)
            tree.heading("# 2", text="PHONE")
            tree.column("# 3", anchor=CENTER)
            tree.heading("# 3", text="E-MAIL")

            scrollbar = ttk.Scrollbar(Frami, orient="vertical", command=tree.yview)
            tree.configure(yscrollcommand=scrollbar.set)
            scrollbar.pack(side="right", fill="y")
            
            count =0
            for i in lst:
                tree.insert('', 'end', text=count, values=i)
                count+=1
            tree.pack()
            
        else:
            _Label_.config(text="No Entries Found")
            
        btn=Button(Frami, text="^",command=Frami.destroy)
        btn.place(x=0,y=0)
        
    Label1 = Label(Frame1, text=" Name:")
    Label1.pack()
    a = Entry(Frame1,width=50, borderwidth=5)
    a.pack()
    Label2 = Label(Frame1, text=" Phone Number:")
    Label2.pack()
    b = Entry(Frame1,width=50,borderwidth=5)
    b.pack()
    Label3 = Label(Frame1, text=" E-Mail:")
    Label3.pack()
    c = Entry(Frame1,width=50, borderwidth=5)
    c.pack()
    buttond= Button(Frame1, text="SEARCH", command=execute)
    buttond.pack()
    
def purchase():
    _next_(purchase)
    Labelx = Label(Frame1, text="----Purchase Panel----",font=('Times',10,"bold"))
    Labelx.pack()
    Label_ = Label(Frame1, text="")
    Label_.pack()

    def srch():
        Frami=LabelFrame(Frame1)
        Frami.place(x=0,y=350,width=1181,height=345)
        _Label_ = Label(Frami, text="")
        _Label_.place(x=540,y=0)
        
        lst = check_purchase(a.get(),b.get(),c.get(),Year.get(),Month.get(),Date.get())
        
        if len(lst) !=0:
            s = ttk.Style()
            s.theme_use('clam')
            s.configure('Treeview', rowheight=50)

            tree = ttk.Treeview(Frami, column=("c1", "c2", "c3","c4","c5"), show='headings', height=8)

            tree.column("# 1", anchor=CENTER)
            tree.heading("# 1", text="ORDER ID")
            tree.column("# 2", anchor=CENTER)
            tree.heading("# 2", text="CUSTOMER NAME")
            tree.column("# 3", anchor=CENTER)
            tree.heading("# 3", text="PHONE")
            tree.column("# 4", anchor=CENTER)
            tree.heading("# 4", text="DATE")
            tree.column("# 5", anchor=CENTER)
            tree.heading("# 5", text="REFERENCE")

            scrollbar = ttk.Scrollbar(Frami, orient="vertical", command=tree.yview)
            tree.configure(yscrollcommand=scrollbar.set)
            scrollbar.pack(side="right", fill="y")

            count =0
            for i in lst:
                tree.insert('', 'end', text=count, values=i)
                count+=1
            tree.pack()
        else:
            _Label_.config(text="No Entries Found")
            
        btn=Button(Frami, text="^",command=Frami.destroy)
        btn.place(x=0,y=0)

        def openbill():
            try:
                curItem = tree.focus()
                location = tree.item(curItem)["values"][4]
                os.system('"%s"' % location)
            except:
                pass
        btn=Button(Frami, text="🔍",command=openbill)
        btn.place(x=20,y=0)

    Label1 = Label(Frame1, text="Search Purchase by one or more of the following fields",font=('Times',10,"bold"))
    Label1.pack()
    Label3 = Label(Frame1, text="Bill Number:")
    Label3.pack()
    a = Entry(Frame1,width=50, borderwidth=5)
    a.pack()
    Label4 = Label(Frame1, text="Customer Name:")
    Label4.pack()
    b = Entry(Frame1,width=50, borderwidth=5)
    b.pack()
    Label5 = Label(Frame1, text="Phone:")
    Label5.pack()
    c = Entry(Frame1,width=50, borderwidth=5)
    c.pack()
    Label5 = Label(Frame1, text="Date:")
    Label5.pack()
    
    date_frame=Frame(Frame1)
    date_frame.pack()
    list_year=[2020,2021,2022,2023,2024,2025,2026,2027,2028]
    list_month=[]
    for i in range(1,13):
        list_month.append(i)
    list_date=[]
    for i in range(1,32):
        list_date.append(i)
    Year =StringVar(value="Year")
    Month =StringVar(value="Month")
    Date =StringVar(value="Date")
    year_dropdown = OptionMenu(date_frame, Year, *list_year)
    year_dropdown.grid(row=0,column=0)
    month_dropdown = OptionMenu(date_frame, Month, *list_month)
    month_dropdown.grid(row=0,column=1)
    date_dropdown = OptionMenu(date_frame, Date, *list_date)
    date_dropdown.grid(row=0,column=2)
    btn=Button(Frame1, text="SEARCH",command=srch)
    btn.pack()
    
def employee():
    _next_(employee)
    Labelx = Label(Frame1, text="----Employee Panel----",font=('Times',10,"bold"))
    Labelx.pack()
    Label_ = Label(Frame1, text="")
    Label_.pack()

    Frim = Frame(Frame1)
    Frim.pack()

    s = ttk.Style()
    s.theme_use('clam')
    s.configure('Treeview', rowheight=40)

    tree = ttk.Treeview(Frim, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings', height=5)

    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="ID")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Name")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="Phone")
    tree.column("# 4", anchor=CENTER)
    tree.heading("# 4", text="E-Mail")
    tree.column("# 5", anchor=CENTER)
    tree.heading("# 5", text="Salary")
    tree.column("# 6", anchor=CENTER)
    tree.heading("# 6", text="Designation")

    scrollbar = ttk.Scrollbar(Frim, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    count =0
    for i in emp_data():
        tree.insert('', 'end', text=count, values=i)
        count+=1
    tree.pack()
     
    def checkey():
        skey_entry=e.get()
        qry3=f"select * from tempac where skey='{skey_entry}'"
        myc.execute(qry3)
        result=myc.fetchall()
        salarye=eval(e2.get())
        if result==[] :
            messagebox.showerror("Invalid Input","No request with this key found")
        elif type(salarye)!=type(123):
             messagebox.showerror("Invalid Input","Enter valid salary")
        else:
             
             Add_emp(result[0][0],result[0][2],result[0][1],salarye,result[0][4])
             login_entry(result[0][0],result[0][3],result[0][4])
             messagebox.showinfo("Employee Added successfully!","Your employee has been added")
             query="truncate table tempac"
             myc.execute(query)
             e.delete(0,END)
             e2.delete(0,END)
           

    def bac():
        Frami.destroy()
        btnme.pack()
        btnskey.pack()

    def skeyen():
        global e,e2,Frami
        btnme.pack_forget()
        btnskey.pack_forget()
        
        Frami=LabelFrame(Framez)
        Frami.pack()
        btn=Button(Frami, text="^",command=bac)
        btn.place(x=0,y=0)
        Label1 = Label(Frami, text="Enter the security key sent to your Email: ")
        Label1.pack(pady=8)
        e = Entry(Frami,width=50, borderwidth=5)
        e.pack()
        Label2 = Label(Frami, text="Enter the Salary :")
        Label2.pack(pady=8)
        e2=Entry(Frami,width=50, borderwidth=5)
        e2.pack()
        btn=Button(Frami, text="ADD",command=checkey)
        btn.pack()
    def manual():
        if type(eval(e0.get()))!=type(123) and len(g.get)!=10:
            messagebox.showerror("Invalid Input","Enter valid salary")
        else:
            Add_emp(eg.get(),g.get(),f.get(),e0.get(),option)
            messagebox.showinfo("Employee Added successfully!","Your employee has been added")
            eg.delete(0,END)
            e0.delete(0,END)
            g.delete(0,END)
            f.delete(0,END)
    def manualen():
        global eg,e0,g,f,option,Frami
        btnme.pack_forget()
        btnskey.pack_forget()
        Frami=LabelFrame(Framez)
        Frami.pack()
        btn=Button(Frami, text="^",command=bac)
        btn.place(x=0,y=0)
        Label1 = Label(Frami, text="Name")
        Label1.pack()
        eg = Entry(Frami,width=50, borderwidth=5)
        eg.pack(pady=5)
        Label2 = Label(Frami, text="E-Mail")
        Label2.pack()
        f = Entry(Frami,width=50, borderwidth=5)
        f.pack(pady=5)
        Label3 = Label(Frami, text="Phone Number")
        Label3.pack()
        g = Entry(Frami,width=50, borderwidth=5)
        g.pack(pady=5)
        Label2 = Label(Frami, text="Enter the Salary :")
        Label2.pack()
        option="Helper"
        e0=Entry(Frami,width=50, borderwidth=5)
        e0.pack(pady=5)
        btn=Button(Frami, text="ADD",command=manual)
        btn.pack(pady=5)
        
    def add():
        global Framez,btnme,btnskey
        for i in Frame1.winfo_children():
            i.destroy()
        Framez=Frame(Frame1)
        Framez.pack()
        btnme=Button(Framez,text="ADD HELPER",command=manualen)
        btnme.pack()
        btnskey=Button(Framez,text="ADD ACCOUNTANT",command=skeyen)
        btnskey.pack()
        
    def remove():
        fro = messagebox.askokcancel("Beware","The selected employee from the table would be deleted")
        if fro==1:
            curItem = tree.focus()
            delete_emp(tree.item(curItem)["values"][0])
            refresh()
        else:
            pass
    
    Frm = LabelFrame(Frame1, text="Actions")
    Frm.pack(pady=20)
    button1= Button(Frm, text="Add Employee",command=add)
    button1.grid(row=0,column=1,padx=20,pady=20)
    button2= Button(Frm, text="Remove Employee",command=remove)
    button2.grid(row=0,column=2,padx=20,pady=20)
    
def stocks():
    _next_(stocks)

    lst1=tblview()
    lst2=tblview()
    lst3=[]
    labela=Label(Frame1,text="---Stocks Panel---",font=('Times',10,"bold"))
    labela.pack()

    Frim = Frame(Frame1)
    Frim.pack()
    
    s = ttk.Style()
    s.theme_use('clam')
    s.configure('Treeview', rowheight=40)

    tree = ttk.Treeview(Frim, column=("c1", "c2", "c3","c4","c5"), show='headings', height=5)

    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="ID")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Name")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="Price")
    tree.column("# 4", anchor=CENTER)
    tree.heading("# 4", text="Units")
    tree.column("# 5", anchor=CENTER)
    tree.heading("# 5", text="In-Stock")
    
    scrollbar = ttk.Scrollbar(Frim, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    
    count =0
    for i in stock_data():
        tree.insert('', 'end', text=count, values=i)
        count+=1
    tree.pack()

    def adnew():
        Frami=LabelFrame(Frame1)
        Frami.place(x=0,y=280,width=1181,height=415)
        Frame3 = Frame(Frami)
        Frame3.pack()
        Label1 = Label(Frame3, text="Item id:")
        Label1.grid(row=0,column=0,pady=2)
        e = Entry(Frame3,width=50, borderwidth=3)
        e.grid(row=0,column=1,pady=2)
        def cmd():
            e.delete(0, END)
            e.insert(END,str(item_id()))
        btn=Button(Frame3, text="🔍",command=cmd)
        btn.grid(row=0,column=3,pady=2)
        Label2 = Label(Frame3, text="Item Name:")
        Label2.grid(row=1,column=0,pady=2)
        f = Entry(Frame3,width=50, borderwidth=3)
        f.grid(row=1,column=1,pady=2)
        Label3 = Label(Frame3, text="Item Price:")
        Label3.grid(row=2,column=0,pady=2)
        g = Entry(Frame3,width=50, borderwidth=3)
        g.grid(row=2,column=1,pady=2)
        Label4 = Label(Frame3, text=" Price per/:")
        Label4.grid(row=3,column=0,pady=2)
        
        choices=["Packet","Kilogram","Gram","Litre"]
        option=ttk.Combobox(Frame3,values=choices,width=30)
        option.grid(row=3,column=1,pady=2)
        
        Label5 = Label(Frame3, text="Item Qty:")
        Label5.grid(row=4,column=0,pady=2)
        h = Entry(Frame3,width=50, borderwidth=3)
        h.grid(row=4,column=1,pady=2)
        def new():
            try:
                add_item(int(e.get()),str(f.get()),int(g.get()),str(option.get()),int(h.get()))
                e.delete(0, END)
                f.delete(0, END)
                g.delete(0, END)
                option.delete(0, END)
                h.delete(0, END)
                refresh()
            except:
                messagebox.showerror("Error","Duplicated Item Id/Name Or Invalid datatype")

        button_ = Button(Frame3, text = "Add", command=new,width=15)
        button_.grid(row=5,column=1,pady=2)
        btn=Button(Frami, text="^",command=Frami.destroy)
        btn.place(x=0,y=0)

    def drop():
        try:
            fro = messagebox.askokcancel("Beware","Only the first selection from the table would be deleted")
            if fro==1:
                curItem = tree.focus()
                delete_item(tree.item(curItem)["values"][0])
                refresh()
        except:
            messagebox.showerror("Error","Single Selection allowed")
        
    Fromi=Frame(Frame1)
    Fromi.pack()
    but_1= Button(Fromi, text="Add New",command=adnew,height=1,width=12)
    but_1.grid(row=0,column=0)
    but_2= Button(Fromi, text="Drop",command=drop,height=1,width=12)
    but_2.grid(row=0,column=1)

    label_=Label(Frame1,text=" ")
    label_.pack()
    
    frame2x= LabelFrame(Frame1, text="Alter Stock",padx=20, pady= 20)
    frame2x.pack()
    
    list2 = Listbox(frame2x, selectmode = "multiple")
    list2.grid(row=1,column=1)
    for i in range(0,len(lst2)):
        list2.insert(i+1,lst2[i])
    
    list3 = Listbox(frame2x, selectmode = "multiple")
    list3.grid(row=1,column=4)
    for i in range(0,len(lst3)):
        list3.insert(i+1,lst3[i])

    def on_click1():
        try:
            a=list2.get(ANCHOR)
            if a=='':
                pass
            else:
                count=0
                for i in list2.curselection():
                    a=list2.get(i)
                    list3.insert(len(lst2)+1,a)
                    lst3.append(a)
                    lst2.remove(a)
                for i in list2.curselection():
                    list2.delete(i-count)
                    count+=1
        except:
            pass

    def on_click2():
        try:
            b=list3.get(ANCHOR)
            if b=='':
                pass
            else:
                count=0
                for i in list3.curselection():
                    b=list3.get(i)
                    list2.insert(len(lst3)+1,b)
                    lst2.append(b)
                    lst3.remove(b)
                for i in list3.curselection():
                    list3.delete(i-count)
                    count+=1
        except:
            pass

    btn__1= Button(frame2x, text=">>",command=on_click1,height=1,width=3)

    btn__1.grid(row=1,column=2)

    but_2= Button(frame2x, text="<<",command=on_click2,height=1,width=3)
    but_2.grid(row=1,column=3)

    lbl=Label(frame2x,text="  ")
    lbl.grid(row=2,column=2)

    def nextwin2():
        if len(lst3)>0:
            lst3_copy=[]
            lst3_copy.extend(lst3)
            lst3_copy.reverse()
            Frami=LabelFrame(Frame1)
            Frami.place(x=0,y=280,width=1181,height=415)
            Frame3 = Frame(Frami)
            Frame3.pack()
            Label1 = Label(Frame3, text="Add Quantity for {i}:".format(i=lst3_copy[-1][0]))
            Label1.pack()
            e = Entry(Frame3,width=50, borderwidth=5)
            e.pack()
            Label_ = Label(Frame3, text="Or/And")
            Label_.pack()
            Label2 = Label(Frame3, text="Input New Price for {i}:".format(i=lst3_copy[-1][0]))
            Label2.pack()
            f = Entry(Frame3,width=50, borderwidth=5)
            f.pack()
            def update_item():
                i=lst3_copy[-1][0]
                y = getitem(i)
                w = y[4]
                if e.get() !="":
                    u = int(e.get())+w
                    update_itemquan(i,u)
                    e.delete(0, END)

                if f.get() !="":
                    update_itemprice(i,f.get())
                    f.delete(0, END)

                try:
                    lst3_copy.pop()
                    i=lst3_copy[-1][0]
                    Label1.config(text=f"Enter Quantity for {i}:")
                    Label2.config(text=f"Enter New Price for {i}:")
                except:
                    Frame3.destroy()

            button = Button(Frame3, text = "ADD", command=update_item)
            button.pack()
            btn=Button(Frami, text="^",command=Frami.destroy)
            btn.place(x=0,y=0)

    but__= Button(frame2x, text="Add",command=nextwin2,height=1,width=12)
    but__.grid(row=3,column=2, columnspan=2)

Frame1=LabelFrame(window)
Frame1.place(x=172,y=0,width=1186,height=700)

Frame2=LabelFrame(window,font=('Times',10,"bold"))
Frame2.place(x=0,y=0,width=170,height=700)

button2 = Button(Frame2, text ="Customer Panel",command=customer,borderwidth=0, height=2, width=16)
button2.grid(row=3,column=1)
button4 = Button(Frame2, text ="Search Purchase",command=purchase,borderwidth=0, height=2, width=16)
button4.grid(row=5,column=1)
button5 = Button(Frame2, text ="Employee Panel",command=employee,borderwidth=0, height=2, width=16)
button5.grid(row=6,column=1)
button6 = Button(Frame2, text ="Stocks",command=stocks,borderwidth=0, height=2, width=16)
button6.grid(row=7,column=1)

stack=[stocks]
stocks()

window.mainloop()