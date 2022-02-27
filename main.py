#!/usr/bin/env python3
from collections import defaultdict
import sys
import os

from pandas import DataFrame, read_table
from defaultlist import defaultlist
from appdirs import user_cache_dir
from markdown import markdown
from string import Template

from ui import QFileDialog, QTableWidgetItem, QUrl, Ui_MainWindow, QApplication, QMainWindow, QFile

# [ Basic settlement ]
cache = user_cache_dir("Carrier Pigeon")
try: os.mkdir(cache)
except: pass

services = defaultdict(lambda: ("localhost", 456),

{
	"Gmail":      ("smtp.gmail.com", 465),
	"Hotmail":    ("smtp.office365.com", 587),
	"YahooMail":  ("smtp.mail.yahoo.com", 456),
	"Protonmail": ("Use Other” option", 0),
})

# [ Qt class ]
class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.smtpTarget = ("smtp.gmail.com", 465)
		self.theDatabase = defaultlist()
		self.ignoreChanges = False
		self.theSelected = 0

		self.RenderPreview()
		self.toCsv(None)
		self.NewSmtp(1)
		
		self.ui.Input.textChanged.connect(self.RenderPreview)
		self.ui.Preview.setUrl(QUrl("file://" + cache + os.sep +  "preview.html"))
		self.ui.Table.cellClicked.connect(self.select)
		self.ui.Table.itemChanged.connect(self.RenderPreview)
		self.ui.Table.itemChanged.connect(self.toCsv)
		self.ui.Load.pressed.connect(self.Load)
		self.ui.Save.pressed.connect(self.Save)

		self.ui.EmailService.currentIndexChanged.connect(self.NewSmtp)
	
	def NewSmtp(self, index):
		self.ui.CustomService.setReadOnly(self.ui.EmailService.currentText() != "Other")
		self.ui.CustomService.setText(services[self.ui.EmailService.currentText()][0]+":"+str(services[self.ui.EmailService.currentText()][1]))
		self.smtpTarget = tuple(self.ui.EmailService.currentText().split(":"))

	def select(self, row, column):
		self.theSelected = row - 1
		self.RenderPreview()

	def Load(self):
		self.loadCsvData(QFileDialog.getOpenFileName(self, "Select a table file", os.path.expanduser("~"), filter = "(*.csv);;(*.ods);;(*.xlsx);;(*.dbf)")[0])
		self.updateData()
	
	def Save(self):
		self.toCsv(10)
		n = QFileDialog.getSaveFileName(self, "Save csv file", os.path.expanduser("~"), filter = "(*.csv)")[0]
		if not n.endswith(".csv"): n += ".csv"
		DataFrame(self.theDatabase).to_csv(n, index = False)

	def RenderPreview(self):
		with open(cache + os.sep + "preview.html", "w") as buffer:
			buffer.write(markdown(self.Replace(self.ui.Input.toPlainText(), self.theSelected)))
		self.ui.Preview.reload()
	
	def Replace(self, text: str, which: int):
		return Template(text.replace('\n', '  \n')).safe_substitute(self.theDatabase[which])

	def loadCsvData(self, file):
		temp = read_table(file, sep=",", skip_blank_lines = True, dtype=str, na_filter = False)
		temp.drop(temp.filter(regex="Unname"),axis=1, inplace=True)
		temp = temp.to_dict("records")
		
		default = defaultlist(lambda: {key:'' for key in temp[0].keys()})
		default += [defaultdict(lambda: '', element) for element in temp]
		
		self.theDatabase = default
		return

	def updateData(self):
		try:
			self.ui.Table.clear()
			self.ignoreChanges = True
			for key in range(len(self.theDatabase[0])):
					self.ui.Table.setItem(0, key, QTableWidgetItem(str(tuple(self.theDatabase[0].keys())[key])))
			
			for row in range(len(self.theDatabase)):
				for column in range(len(self.theDatabase[row])):
					self.ui.Table.setItem(row+1, column, QTableWidgetItem(str(self.theDatabase[row][tuple(self.theDatabase[row].keys())[column]])))
			self.ignoreChanges = False
		except: pass

	def toCsv(self, item):
		if self.ignoreChanges: return
		temp = []
		for row in range(self.ui.Table.rowCount()):
			temp.append([(self.ui.Table.item(row, column).text() if self.ui.Table.item(row, column) else "") for column in range(self.ui.Table.columnCount())])
		self.theDatabase = self.Struct(temp)
	
	def Struct(self, data) -> list:
		if len(data) < 2:
			return data
		return [{data[0][column]:row[column] for column in range(len(row))} for row in data[1:]]

if __name__ == "__main__":
	app = QApplication(sys.argv)

	window = MainWindow()
	window.show()

	sys.exit(app.exec())