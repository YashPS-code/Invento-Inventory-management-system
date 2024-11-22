from tkinter import *
from tkinter import ttk
from ecalc import Calculator
from backend import *
from tkinter import messagebox
import subprocess
from fpdf import FPDF
from fpdf.enums import XPos, YPos
from datetime import datetime,date
import os
from PIL import ImageTk,Image
from mail import sendbill


date_time=datetime.now()
date_time=date_time.strftime("%d-%m-%Y,%H:%M:%S")



Root = Tk()
Root.geometry("1360x702")
Root.title("INVENTO")
Root.iconbitmap("MASTER\\shopping-basket.ico")
Tab = ttk.Notebook(Root)
Tab.pack()

window1=Frame(Tab, width = 1360, height=702)
window1.pack(fill="both",expand=1)

window2 = Frame(Tab, width = 1360, height=702)
window2.pack(fill="both",expand=1)

Tab.add(window1, text = "Base window")
Tab.add(window2, text = "Billing")

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

def Logout():
    Root.destroy()
    subprocess.run(["python","MASTER\\emain.py"])

menu = Menu(Root)
Root.config(menu=menu)

file_menu = Menu(menu)
menu.add_cascade(label="Options",menu=file_menu)
file_menu.add_command(label="Refresh",command=refresh)
file_menu.add_command(label="Exit",command=Root.destroy)
file_menu.add_command(label="LogOut",command=Logout)

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
            tree.column("# 4", anchor=CENTER)

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
    buttond.pack(pady=15)
    
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
        
        date1=Year.get()
        date2=Month.get()
        date3=Date.get()
        
        lst = check_purchase(a.get(),b.get(),c.get(),date1,date2,date3)
        
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
    list_year=[2020,2021,2022,2023,2024]
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
    btn.pack(pady=5)


Frame1=LabelFrame(window1)
Frame1.place(x=172,y=0,width=1186,height=700)

Frame2=LabelFrame(window1,font=('Times',10,"bold"))
Frame2.place(x=0,y=0,width=170,height=700)

button2 = Button(Frame2, text ="Customer Panel",command=customer,borderwidth=0, height=2, width=16)
button2.grid(row=3,column=1)
button4 = Button(Frame2, text ="Search Purchase",command=purchase,borderwidth=0, height=2, width=16)
button4.grid(row=5,column=1)

stack=[purchase]
purchase()

bag_p=[]
def myf():
    global framez,ser,bag,lstitbig,beta

    framez= LabelFrame(window2,padx=100,pady=60)
    framez.pack()

    lstitbig=[]
    for j in get_all_items():
        lstitbig.append([j[0],j[1],int(j[2])])

    def ser():
        try:
            if len(option3.get()) != 10 :
                messagebox.showerror("Invalid input","Enter valid phone number")
            else:
                cus = phn_get(option3.get())
                centry.delete(0,END)
                centry.insert(END,str(cus[0][0]))
                option4.delete(0,END)
                option4.insert(END,str(cus[0][2]))
        except:
            messagebox.showinfo("Not Found","No Customer with this Phone number")

    Label1=Label(framez,text="Select Item",font=('Times',10,"bold"))
    Label1.pack()
    selected_item=ttk.Combobox(framez,width=50,values=lstitbig)
    selected_item.pack(padx=50)
    Label2=Label(framez,text="Select Quantity",font=('Times',10,"bold"))
    Label2.pack()
    a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    selected_qty=ttk.Combobox(framez,width = 50,values = a)
    selected_qty.pack(padx=50)
    
    def bagad():
        selected_item_list = (selected_item.get()).split()

        try:
            if isinstance(eval(selected_qty.get()),int) == False:
                pass
                
            elif len(selected_item.get())==0 or len(selected_qty.get())==0:
                pass

            else:
                beta = []
                flag = 0
                beta.append(selected_item_list[1])
                beta.append(selected_qty.get()) 
                
                for i in bag_p:                 #Finding if beta[0] present in bag
                    if beta[0] == i[0]:
                        i[1] = str(int(beta[1]) + int(i[1])) 
                        flag = 1
                        break
                
                if flag != 1:
                    bag_p.append(beta)   
        
                bag.delete(0,END)
                for i in bag_p:           
                    bag.insert(END,i)

                selected_item.delete(0,END)
                selected_qty.delete(0,END)

        except:
            messagebox.showerror("Invalid input","Enter valid data")
    
    Frim = Frame(framez)
    Frim.pack()
    bag=Listbox(Frim)
    bag.pack(side = LEFT, fill = BOTH)

    scrollbar = Scrollbar(Frim)
    scrollbar.pack(side = RIGHT, fill = BOTH)

    bag.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = bag.yview)

    btnz=Button(framez,text="Add item to Bag",command=bagad)
    btnz.place(x=160,y=250)

    def rem():
        selct=bag.curselection()
        try:
            bag_p.pop(selct[0])
        except:
            pass
        bag.delete(selct)

    def removeall():
        bag.delete(0,END)
        for i in range(len(bag_p)):
            bag_p.pop()

    btnr=Button(framez,text="Remove",command=rem)
    btnr.place(x=103,y=250)
    btnra=Button(framez,text="Remove All",command=removeall)
    btnra.place(x=260,y=250)

myf()
def gen_Bill():
    cnam=str(centry.get())
    cphn=str(option3.get())
    cmail=str(option4.get())
    if len(cnam)==00 or len(cphn)==0 or len(cmail)==0 :
        messagebox.showerror("Invalid Input","Enter Valid Data")
    else:
        try:
            inc = int(pur_sno()[0])+1
        except:
            inc=1
        S_no=0
        for i in bagitem:
            S_no+=1
            item_name=i[0]
            item_qty=int(i[1])
            cus_name=cnam
            for k in lstitbig:
                if k[1]==item_name:
                    item_price=k[2]
            item_amount=str((int(item_price))*(int(item_qty ))) 
            qry="insert into tempbill values(%s,%s,%s,%s,%s)"
            val=(str(S_no),item_name,item_qty,item_price,item_amount)
            myc.execute(qry,val)
            db.commit()
        qry="select * from tempbill"
        myc.execute(qry)
        res=myc.fetchall()

        gamma=[]
        for q in res:
            gamma.append(int(q[4]))
        sumgt=float(sum(gamma))
        qry2="truncate table tempbill"
        bagitem.clear()
        myc.execute(qry2)

        myInv=FPDF()
        myInv.add_page()

        myInv.set_font('Times','B',30)
        myInv.cell(0,10,'INVOICE',align='C',new_y=YPos.NEXT,new_x=XPos.LMARGIN)
        myInv.set_font('Times','B',10)
        myInv.cell(0,10,'Order id: '+str(inc),align='L',border=1,new_y=YPos.NEXT,new_x=XPos.LMARGIN)
        myInv.cell(0,10,'Customer Name: '+cus_name,align='L',border=1,new_y=YPos.NEXT,new_x=XPos.LMARGIN)
        myInv.cell(0,10,'Date/Time: '+date_time,align='L',border=1,new_y=YPos.NEXT,new_x=XPos.LMARGIN)
        myInv.cell(38,10,'SNO.',align='L',border=1)
        myInv.cell(38,10,'Item Name',align='C',border=1)
        myInv.cell(38,10,'Quantity',align='C',border=1)
        myInv.cell(38,10,'Price',align='C',border=1)
        myInv.cell(38,10,'Amount',align='C',border=1,new_y=YPos.NEXT,new_x=XPos.LMARGIN)

        myInv.set_font('Times','',8)
        for i in res:
            for k in i:
                if k==i[-1]:
                    myInv.cell(38,8,k,align='C',border=1,new_y=YPos.NEXT,new_x=XPos.LMARGIN)
                else:
                    myInv.cell(38,8,k,align='C',border=1,)
        myInv.set_font('Times','B',10)
        myInv.cell(0,10,'Grand Total: Rs.'+str(sumgt),align='L',border=1)

        try:
            inc = int(pur_sno()[0])+1
        except:
            inc=1
        

        myInv.output(f'MASTER\\Invoices\\Invoice{inc}.pdf')
        try:
            if get_cus_name(int(cphn))==[]: 
                Add_cust(cus_name,cphn,cmail)
                sendbill(cmail,cnam)
                pur_insert(inc,cus_name,cphn,date.today(),f'MASTER\\Invoices\\Invoice{inc}.pdf')
                for t in bag_p:
                    y = getitem(t[0])
                    w = y[4]
                    u = w - int(t[1])
                    update_itemquan(t[0],u)   
                messagebox.showinfo("Invoice Generated Successfully!","Mail sent successfully") 
            else:
                if get_cus_name(int(cphn))[0][0]==cus_name:
                    sendbill(cmail,cnam)
                    pur_insert(inc,cus_name,cphn,date.today(),f'MASTER\\Invoices\\Invoice{inc}.pdf')
                    for t in bag_p:
                        y = getitem(t[0])
                        w = y[4]
                        u = w - int(t[1])
                        update_itemquan(t[0],u)
                    messagebox.showinfo("Invoice Generated Successfully!","Mail sent successfully") 
                else:
                    messagebox.showerror("Customer Exists","Customer named "+get_cus_name(int(cphn))[0][0]+" already exists with same phone number")
        except:
            messagebox.showerror("Invalid Input","Invalid input")

def backb():
    framex.destroy()
    framez.pack()
    back.destroy()

def next():
    global centry,option3,option4,framex,back,bagitem,cnam
    bagitem=list(bag.get(0,END))
    token = True
    for t in bag_p:
        
        y = getitem(t[0])
        w = y[4]
        u = w - int(t[1])
        if u<0:
           token = False
           break

    if bagitem==[]:
        messagebox.showerror("Invalid Input","Enter Valid Input")
    
    elif token==False:
        messagebox.showerror("Out Of Stock","Stocks running low")

    else:
        framez.pack_forget()


        framex=LabelFrame(window2,padx=100,pady=100)
        framex.pack()
        back=Button(framex,text="<<",command=backb)
        back.place(x=0,y=0)
        Label4=Label(framex,text="Enter Customer Phone no.",font=('Times',10,"bold"))
        Label4.pack()
        option3=Entry(framex,width=50)
        option3.pack(padx=50)
        Buttons=Button(framex,text="🔍",command=ser)
        Buttons.place(x=355,y=20)
        Label3=Label(framex,text="Enter Customer Name",font=('Times',10,"bold"))
        Label3.pack()
        centry=Entry(framex,width=50)
        centry.pack()
        Label5=Label(framex,text="Enter Customer Email",font=('Times',10,"bold"))
        Label5.pack()
        option4=Entry(framex,width=50)
        option4.pack(padx=50)
        Buttong=Button(framex,text="Generate Bill",font=('Times',10,"bold"),command=gen_Bill)
        Buttong.place(x=150,y=150)
btnnxt=Button(framez,text="Proceed",command=next)
btnnxt.place(x=180,y=280)
Root.mainloop()
