import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


smtp_ssl_host="smtp.gmail.com"
smtp_ssl_port=int(587) #465
USERNAME="xyz@gmail.com"
PASSWORD="abcdef4s"  #this is the password which i have generated for this python app. its not the gmail password of this account.
sender=USERNAME
targets="abc@gmail.com" #for multiple use ["abc@xyz.com","ab@xy.com"]

text="hello! how r u?"
msg=MIMEMultipart()
msg["Subject"]="HELLO"
msg["from"]=sender
msg["to"]=targets
msg.attach(MIMEText(text))

server=smtplib.SMTP(smtp_ssl_host,smtp_ssl_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(USERNAME,PASSWORD)
server.sendmail(sender,targets,msg.as_string())

server.quit()
