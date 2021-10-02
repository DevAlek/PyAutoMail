import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from uic import Ui_MainWindow, QFileDialog
from PySide6.QtCore import QFile
from re import fullmatch

from Subtool.email_sender import Email as Email
from Subtool.tsv_to_dict import tsv_to_dict
from Subtool.docs import docx_replacer
from time import sleep

with open("manual.html") as file:
    manual_text = file.read()

def isValidEmail(email: str) -> bool:
    return bool(fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email))

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.attachSave = ''
        self.database = None
        self.attach = ''

        self.outputTSV = self.ui.CheckReplace
        self.outputREPLACE = self.ui.ManualButton
        self.outputMANUAL = self.ui.CheckTSV

        self.ui.TheErrorPlace.hide()
        self.ui.OutputSection.hide()
        self.ui.Sep.hide()
        self.ui.Email.editingFinished.connect(self.checkEmail)
        self.outputMANUAL.pressed.connect(self.showManual)

        self.outputTSV.pressed.connect(self.showTSV)
        self.outputREPLACE.pressed.connect(self.showREPLACE)

        self.ui.Attach.pressed.connect(self.openAttach)
        self.ui.TSV.pressed.connect(self.openTSV)

        self.ui.Confirm.accepted.connect(self.sendEmails) #unica linha decente

    def openAttach(self):
        file = QFileDialog.getOpenFileName(self, 'Select a file to attach in the email')[0]
        self.attach = file #real ou fake

    def sendEmails(self):
        if self.database == None: return self.error("You didn't load a tsv file!")
        self.ui.Output.setText('')
        try: login = Email(self.ui.Email.text(), self.ui.Password.text())
        except: return self.error("Unable to login.")

        # plain text part
        self.attachSave = self.attach
        for people in self.database:
            print(people)
            self.ui.Output.setText(self.ui.Output.toPlainText()+'\n'+f'Sending to {people[self.ui.TSVEmail.text()]}')
            config = ','.join([f'{"".join(e for e in key if e.isalnum())} = """ {people[key]} """' for key in people])
            text_part = eval(f"""self.ui.EmailText.toPlainText().format({config})""")

            # attach part
            if self.attachSave.endswith('.docx'):
                docx_replacer(self.attachSave, config, people[self.ui.TSVEmail.text()])
                self.attach = people[self.ui.TSVEmail.text()] + '.docx'
            try: login.send_text(self.ui.Subject.text(), text_part, people[self.ui.TSVEmail.text()], self.attach)
            except Exception as ex: self.error(f"Failed to send email to {people[self.ui.TSVEmail.text()]}: {ex}")

    def showREPLACE(self):
        if self.database == None: return self.error("You didn't load a tsv file!")

        config = ','.join([f'{"".join(e for e in key if e.isalnum())} = """ {self.database[0][key]} """' for key in self.database[0]])
        send = eval(f"""self.ui.EmailText.toPlainText().format({config})""")

        self.ui.Output.setText(send)

    def showTSV(self):
        if self.database == None: return self.error("You didn't load a tsv file!")
        self.ui.Output.setText('→ '+'\n\n → '.join(['\n· '.join([f'{"".join(e for e in data if e.isalnum())}: {people[data]}' for data in people]) for people in self.database]))

    def openTSV(self):
        file = QFileDialog.getOpenFileName(self, 'Select the spreadsheet (.tsv file)')[0]
        if not file.endswith('.tsv'): return self.error("The file extension must be .tsv!")
        if not file: return
        self.database = tsv_to_dict(file)

    def showManual(self):
        self.ui.Output.setHtml(manual_text)

    def error(self, error: str):
        self.ui.TheErrorPlace.show()
        self.ui.Error.setText("<b>Error: </b>" + error)

    def checkEmail(self):
        if not self.ui.Email.text().split(): return
        if not isValidEmail(self.ui.Email.text()):
            self.error("Invalid email!")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
