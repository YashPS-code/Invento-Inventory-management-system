import random
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
from backend import*

cha="abcdefghijklmnopqrstuvwxyz012345678901234567890123456789"
l=[]

for i in range(6):
    seckey=(random.choice(cha))
    l.append(seckey)
j="".join(l)
o=random.randint(1000,9999)
aotp=str(o)

def send_msg(recepient,b):
    port = 465 
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login('inventoforinventory@gmail.com',"fquhostjnnvkilyt")
        subject="OTP for verification of invento manager account"
        message="Hi "+b+" OTP for verification of your invento account is "+aotp
        emailbody=f'Subject:{subject}\n\n{message}'
        server.sendmail('inventoforinventory@gmail.com',recepient,emailbody)
def skey(recepient1,c,d):
    port = 465 
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login('inventoforinventory@gmail.com',"fquhostjnnvkilyt")
        subject="NEW ACCOUNT REQUEST"
        message="Hi "+c+" There is a new account request from "+d+"\nThe security key is "+j+" Enter this key in the Add employee option"
        emailbody=f'Subject:{subject}\n\n{message}'
        server.sendmail('inventoforinventory@gmail.com',recepient1,emailbody)
sender="inventoforinventory@gmail.com"
def sendbill(cumail,cunam):
    body="Hi "+cunam +" ! "+" Kindly check the invoice for your purchase\nHope you had a great experience\nThank you"
    msg=MIMEMultipart()
    msg.attach(MIMEText(body,'plain'))

    msg['Subject']="Your Invoice"
    msg['From']="inventoforinventory@gmail.com"
    msg['To']=cumail
    try:
        inc = int(pur_sno()[0])+1
    except:
        inc=1
    filename=f"MASTER\\Invoices\\Invoice{inc}.pdf"
    filenameo=f"Invoice{inc}.pdf"
    attachment=open(filename,'rb')
    attachment_package=MIMEBase('application','octet-stream')
    attachment_package.set_payload((attachment).read())
    encoders.encode_base64(attachment_package)
    attachment_package.add_header('Content-Disposition',f'attachment; filename= {filenameo}')
    msg.attach(attachment_package)
    text=msg.as_string()


    with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp_server:
        smtp_server.login(sender,"fquhostjnnvkilyt")
        smtp_server.sendmail(sender,cumail,text)


        