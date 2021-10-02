from subprocess import Popen, PIPE
Popen('python -m smtpd -c DebuggingServer -n localhost:465', shell = True, stderr = PIPE)

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import smtplib, ssl

class Email:
	def __init__(self, email, password, port = 587):
		self.context = ssl.create_default_context()

		self.email = email
		self.password = password
		self.port = port

		server = smtplib.SMTP("smtp.gmail.com", port, timeout = 10)
		server.starttls(context=self.context)
		server.ehlo()  # Can be omitted

		server.login(email, password)
		self.server = server

	def send_text(self, subject, text, to, attach = ''):
		message = MIMEMultipart()
		message["Subject"], message["From"], message["To"] = subject, self.email, to

		plain = MIMEText(text, "plain")

		message.attach(plain)

		if attach != '':
			filename = attach
			attachment = open(filename, "rb")
			part = MIMEBase('application', 'octet-stream')
			part.set_payload((attachment).read())
			encoders.encode_base64(part)
			part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
			message.attach(part)

		self.server.sendmail(self.email, to, message.as_string())

	def send_html(self, text, html, subject, to):
		message = MIMEMultipart("alternative")
		message["Subject"], message["From"], message["To"] = subject, self.email, to

		plain = MIMEText(text, "plain")
		fancy = MIMEText(html, "html")

		message.attach(plain)
		message.attach(fancy)

		self.server.sendmail(self.email, to, message.as_string())
