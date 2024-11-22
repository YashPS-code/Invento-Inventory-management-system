from tkinter import *
from PIL import ImageTk,Image

def Calculator():
    
    calc=Tk()      
    calc.title("Invento Calc")
    calc.iconbitmap("MASTER\\shopping-basket.ico")

    inp= Entry(calc ,width=35,borderwidth=5)

    inp.grid(row=0,column=0,columnspan=3, padx=10, pady=10)




    def click(number):
        can = inp.get()
        inp.delete(0,END)
        inp.insert(0,str(can) + str(number))

    
    def key_press(event):
        click(str(event.char))
        
    def clear():
        inp.delete(0,END)

    def add():
        
        firstnum=inp.get()
        global f_num
        global math
        math="add"        
        f_num=float(firstnum)
        inp.delete(0,END)

    def equal():
        secnum=inp.get()
        inp.delete(0,END)
        if math=="add":
            inp.insert(0,f_num+float(secnum))
        if math=="sub":
            inp.insert(0,f_num-float(secnum))
        if math=="multiply":
            inp.insert(0,f_num*float(secnum))
        if math=="divide":
            inp.insert(0,f_num/float(secnum))
    def mul():
        firstnum=inp.get()
        global f_num
        global math
        math="multiply"
        f_num=float(firstnum)
        inp.delete(0,END)
    def div():
        firstnum=inp.get()
        global f_num
        global math
        math="divide" 
        f_num=float(firstnum)
        inp.delete(0,END)

    def sub():
        firstnum=inp.get()
        global f_num
        global math
        math="sub"
        
        f_num=float(firstnum)
        inp.delete(0,END)


    but1=Button(calc,text="1",height=2,width=3,command=lambda:click(1),padx=40,pady=20)
    but2=Button(calc,text="2",height=2,width=3,command=lambda:click(2),padx=40,pady=20)
    but3=Button(calc,text="3",height=2,width=3,command=lambda:click(3),padx=40,pady=20)
    but4=Button(calc,text="4",height=2,width=3,command=lambda:click(4),padx=40,pady=20)
    but5=Button(calc,text="5",height=2,width=3,command=lambda:click(5),padx=40,pady=20)
    but6=Button(calc,text="6",height=2,width=3,command=lambda:click(6),padx=40,pady=20)
    but7=Button(calc,text="7",height=2,width=3,command=lambda:click(7),padx=40,pady=20)
    but8=Button(calc,text="8",height=2,width=3,command=lambda:click(8),padx=40,pady=20)
    but9=Button(calc,text="9",height=2,width=3,command=lambda:click(9),padx=40,pady=20)
    but_equal=Button(calc,text="=",height=7,width=3,command=equal,padx=40,pady=20)
    but0=Button(calc,text="0",height=2,width=3,command=lambda:click(0),padx=40,pady=20)
    but_add=Button(calc,text="+",height=2,width=3,command=add,padx=40,pady=20)
    but_sub=Button(calc,text="-",height=2,width=3,command=sub,padx=40,pady=20)
    but_multiply=Button(calc,text="*",height=2,width=3,command=mul,padx=40,pady=20)
    but_divide=Button(calc,text="/",height=2,width=3,command=div,padx=40,pady=20)
    but_clear=Button(calc,text="AC",height=2,width=3,command=clear,padx=40,pady=20)
    but_period=Button(calc,text=".",height=2,width=3,command=lambda:click("."),padx=40,pady=20)

    
    but1.grid(row=3, column=2)
    but2.grid(row=3, column=1)
    but3.grid(row=3, column=0)
    
    but4.grid(row=2, column=2)
    but5.grid(row=2, column=1)
    but6.grid(row=2, column=0)

    but7.grid(row=1, column=2)
    but8.grid(row=1, column=1)
    but9.grid(row=1, column=0)
   
    but_equal.grid(row=4, column=0, rowspan=2)
    but0.grid(row=4, column=1)
    but_add.grid(row=5, column=1)
    but_sub.grid(row=5, column=2)
    but_multiply.grid(row=6,column=1)
    but_divide.grid(row=6,column=2)
    
    but_clear.grid(row=6, column=0)
    but_period.grid(row=4,column=2)
    
    for i in range(10):
        calc.bind(str(i),key_press)
    getnum=eval(inp.get)
    inp.insert(getnum)

    calc.mainloop()
