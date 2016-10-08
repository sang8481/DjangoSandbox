import getpass
import telnetlib
import socket
import base64
import sys

HOST = socket.gethostbyname('cuvic.cnu.ac.kr')
user = input("Enter your e-mail account : ")
password = getpass.getpass()

try:
	tn = telnetlib.Telnet(HOST, 25)
except IOError :
	print("Telnet connection failed")
	sys.exit()

host_name = "cnu.ac.kr"
mail_from = user + "@" + host_name
mail_to = input("Enter recieve e-mail account : ");

tn.write(b"EHLO " + mail_from.encode() + b"\r\n")
tn.write(b"AUTH LOGIN\r\n")

tn.write(base64.b64encode(user.encode()) + b"\r\n")
tn.write(base64.b64encode(password.encode()) + b"\r\n")

tn.write(b"MAIL FROM: " + mail_from.encode() + b"\r\n")
tn.write(b"RCPT TO:"+ mail_to.encode() + b"\r\n")
tn.write(b"DATA\r\n")

subject = input("Enter e-mail subject : ")
tn.write(b"SUBJECT: " + subject.encode() + b"\r\n")
tn.write(b"FROM: " + mail_from.encode() + b"\r\n")
tn.write(b"TO: " + mail_to.encode() + b"\r\n")

body = input("Enter e-mail body : ")
tn.write(body.encode() + b"\r\n")
tn.write(b".\r\n")
tn.write(b"QUIT\r\n")

print (tn.read_all())
