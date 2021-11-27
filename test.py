#!/usr/bin/python
import sys
import smtplib, ssl
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.application import MIMEApplication

smtp_server = 'smtp.gmail.com'
smtp_port = 587
#Replace with your own gmail account
gmail = 'scharf.frontrow@gmail.com'
password = 'nutflush'

message = MIMEMultipart('mixed')
message['From'] = 'scharf.frontrow@gmail.com'
message['To'] = 'rscharf33@gmail.com'
# message['CC'] = 'contact@company.com'
message['Subject'] = 'Hello'

msg_content = '<h4>Hi There,<br> This is a testing message.</h4>\n'
body = MIMEText(msg_content, 'html')
message.attach(body)

attachmentPath = "results/pep.pdf"
try:
	with open(attachmentPath, "rb") as attachment:
		p = MIMEApplication(attachment.read(),_subtype="pdf")	
		p.add_header('Content-Disposition', "attachment; filename= %s" % attachmentPath.split("\\")[-1]) 
		message.attach(p)
except Exception as e:
	print(str(e))

msg_full = message.as_string()

context = ssl.create_default_context()

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("scharf.frontrow@gmail.com", "nutflush")
server.sendmail("scharf.frontrow@gmail.com", "rscharf33@gmail.com", msg_full)
server.quit()

# with smtplib.SMTP(smtp_server, smtp_port) as server:
# 	server.ehlo()  
# 	server.starttls(context=context)
# 	server.ehlo()
# 	server.login(gmail, password)
# 	server.sendmail(gmail, "rscharf33@gmail.com", msg_full)
# 	server.quit()

print("email sent out successfully")

sys.exit(1)


print("hi")
# rscharf33, scharf.frontrow
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("scharf.frontrow@gmail.com", "nutflush")
server.sendmail("scharf.frontrow@gmail.com", "rscharf33@gmail.com", "sup")
server.quit()
# msg = email.EmailMessage()
