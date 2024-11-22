import mysql.connector as s
from tkinter import messagebox
import datetime


db=s.connect(
    host='localhost',
    user='root',
    password='tiger',
    database='project')
myc=db.cursor()

def pur_sno():
    query = "SELECT MAX(order_id) FROM purchase"
    myc.execute(query)
    sno = myc.fetchone()
    return sno

def update_itemquan(name,current_stock):
    query ='UPDATE items SET current_stock=%s WHERE item_name = %s'
    values=(current_stock,name)
    myc.execute(query,values)
    db.commit()

def getitem(name):
    query = "SELECT * FROM items WHERE item_name = %s"
    myc.execute(query, (name,))
    item = myc.fetchone()
    return item

def phn_get(phone):
    qry=f"SELECT * FROM customers WHERE phone={phone}"
    myc.execute(qry)
    return myc.fetchall()


def get_all_items():
    query = "SELECT * FROM items "
    myc.execute(query)
    item = myc.fetchall()
    return item


def pur_insert(order_id,cust_name,phone,date,ref):
    query = "INSERT INTO purchase VALUES(%s,%s,%s,%s,%s)"
    values=(order_id,cust_name,phone,date,ref)
    myc.execute(query,values)
    db.commit()



def Add_cust(name,mobile_no,email):
    query='INSERT INTO customers (name,phone,email) VALUES(%s,%s,%s)'
    values=(name,mobile_no,email)
    myc.execute(query,values)
    db.commit()

def update_itemprice(name,price):
    query ='UPDATE items SET price=%s WHERE item_name = %s'
    values=(price,name)
    myc.execute(query,values)
    db.commit()

def delete_item(name):
    query = f"DELETE FROM items WHERE item_id = {name}"
    myc.execute(query)
    db.commit()

def Add_emp(name,phone_number,email,salary,designation):
    try:
        query='INSERT INTO employee (employee_name,phone_number,email,salary,designation) VALUES(%s,%s,%s,%s,%s)'
        values=(name,phone_number,email,salary,designation)
        myc.execute(query,values)
        db.commit()
    except:
        messagebox.showerror("Error","One or More columns are Empty")

def get_emp_desig():
    query="Select * from employee where designation='Manager'"
    myc.execute(query)
    res=myc.fetchone()
    return res

def delete_emp(name):
    query1 = f"DELETE FROM employee WHERE employee_id = {name}"
    myc.execute(query1)
    query2 = f"DELETE FROM login WHERE employee_id = {name}"
    myc.execute(query2)
    db.commit()
    
def emp_data():
    query="SELECT * FROM employee WHERE designation !='Manager'"
    myc.execute(query)
    return myc.fetchall()

def stock_data():
    query="SELECT * FROM items"
    myc.execute(query)
    db_result=myc.fetchall()
    return db_result

def tblview():
    query="SELECT item_name FROM items"
    myc.execute(query)
    db_result=myc.fetchall()
    return db_result
    
def add_item(id_,name,price,unit,qty):
    if type(123)==type(price) and type(123)==type(id_) and type(123)==type(qty):
        query="INSERT INTO items(item_id,item_name,price,unit,current_stock) VALUES(%s,%s,%s,%s,%s);"
        values=(id_,name,price,unit,qty)
        myc.execute(query,values)
        db.commit()
    else:
        messagebox.showerror("Invalid Input","Enter the correct values")

def check_purchase(id_,name,phone,d1,d2,d3):
    try:
        date=datetime.datetime(int(d1),int(d2),int(d3))
    except:
        date=datetime.datetime(2015,10,10)
    query="SELECT * FROM Purchase WHERE order_id = %s OR cust_name = %s OR phone = %s OR date = %s"
    values=(id_,name,phone,date)
    myc.execute(query,values)
    db_result=myc.fetchall()
    return db_result

def check_cust(name,phone,email):
    query="SELECT * FROM customers WHERE name = %s OR phone = %s OR email = %s"
    values=(name,phone,email)
    myc.execute(query,values)
    db_result=myc.fetchall()
    return db_result

def truncate_all():
    msg = messagebox.askokcancel("Warning","All your data will be lost Do you want to continue?")
    if msg ==1:
        tables=['customers','employee','items','login','purchase','tempac','tempbill']
        for i in tables:
            qry =f'truncate table {i}'
            myc.execute(qry)


def login_entry(username,password,designation):
    qry4="INSERT into login(uname,password,designation) VALUES(%s,%s,%s)"
    values=(username,password,designation)
    myc.execute(qry4,values)
    db.commit()

def get_cus_name(phn):
    qry=f"select name from customers where phone={phn}"
    myc.execute(qry)
    result=myc.fetchall()
    return(result)

def item_id():
    try:
        query = "SELECT MAX(item_id) FROM items"
        myc.execute(query)
        itemid = myc.fetchone()[0]
        itemid+=1
    except:
        itemid = 1
    return itemid