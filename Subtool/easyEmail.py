#!/usr/bin/env python3
# -*- enconding:utf-8

# [ 3th party libraries ]
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from subprocess import Popen, PIPE
from email import encoders
import smtplib, ssl

Popen('python -m smtpd -c DebuggingServer -n localhost:465', shell = True, stderr = PIPE)

class Email:
	'''
	Email session for email-sending.
	'''

	def __init__(self, email: str, password: str, port = 587, prov = "smtp.gmail.com"):
		'''
email = Email(email: str, password: str, port: int, prov: str):
	- email: 	Your email.
	- password: Your email password.
	- port: 	Port to localhost (leave unchanged)
	- prov: 	The email service API (default is Gmail)
		'''

		self.context = ssl.create_default_context()
		self.email = email

		server = smtplib.SMTP(prov, port, timeout = 10)
		server.starttls(context=self.context)
		server.ehlo()

		server.login(email, password)
		self.server = server


	def send(self, to: str, subject: str, text:str , attach = []):
		'''
email.send(to: str, subject: str, text: str, attach: list):
	- to: 		Who will recieve the email.
	- subject: 	The email subject.
	- text: 	The email content. (currently PlainText only).
	- attach:	Array with the path for the file(s). (list or tuple ONLY).
		'''

		if type(attach) not in [list, tuple]:
			attach = [attach]

		message = MIMEMultipart()
		message["Subject"], message["From"], message["To"] = subject, self.email, to

		plain = MIMEText(text, "plain")
		message.attach(plain)

		if len(attach) > 0:
			for attachment in attach:
				if type(attachment) != str or not attachment: continue

				filename = attachment
				fattachment = open(filename, "rb")
				part = MIMEBase('application', 'octet-stream')
				part.set_payload((fattachment).read())
				encoders.encode_base64(part)
				part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
				message.attach(part)

		self.server.sendmail(self.email, to, message.as_string())
