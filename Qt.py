#!/usr/bin/env python3
# -*- enconding:utf-8 -*-

# [ 3th party Libraries ]
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from os import remove
import sys

# [ The uic (graphical user interface) ]
from uic import Ui_MainWindow, QFileDialog

# [ Custom Libraries ]
from Subtool.func import tsvToDict, docxReplacer, isValidEmail
from Subtool.easyEmail import Email

# [ Load the manual ]
with open("manual.html") as file: manual_text = file.read()

# [ Qt class ]
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.buttons = [self.ui.Attachment1, self.ui.Attachment2, self.ui.Attachment3, self.ui.Attachment4, self.ui.Attachment5]
        self.database = None
        self.login = None
        self.attach = []

        # [ Hide optional sections ]
        self.ui.TheErrorPlace.hide()
        self.ui.OutputSection.hide()
        self.ui.Sep.hide()

        for b in self.buttons:
            b.hide()

        # [ Events ]
        self.ui.Email.editingFinished.connect(self.checkEmail)

        # [ Checking section ]
        self.ui.Manual.pressed.connect(self.showManual)

        # [ Open files ]
        self.ui.Attach.pressed.connect(self.openAttach)

        # [ Action ]
        self.ui.Confirm.accepted.connect(self.sendEmails)

        # [ Cancel an attachment ] (probabbly have a better way to do it but i dunno :( )
        self.ui.Attachment1.pressed.connect(self.remove1)
        self.ui.Attachment2.pressed.connect(self.remove2)
        self.ui.Attachment3.pressed.connect(self.remove3)
        self.ui.Attachment4.pressed.connect(self.remove4)
        self.ui.Attachment5.pressed.connect(self.remove5)


    # [ Open a new attachment ]
    def openAttach(self):
        if len(self.attach) >= 4: return self.error("Attachment limit reached.")
        file = QFileDialog.getOpenFileName(self, 'Select a file to attach in the email')[0]
        if not file: return
        self.attach.append(file)

        for button in self.buttons:
            button.hide()

        for attachment in range(len(self.attach)):
            self.buttons[attachment].setText(self.attach[attachment])
            self.buttons[attachment].show()

    def remove1(self):
        self.ui.Attachment1.hide()
        self.attach.remove(self.attach[0])

    def remove2(self):
        self.ui.Attachment2.hide()
        self.attach.remove(self.attach[1])

    def remove3(self):
        self.ui.Attachment3.hide()
        self.attach.remove(self.attach[2])

    def remove4(self):
        self.ui.Attachment4.hide()
        self.attach.remove(self.attach[3])

    def remove5(self):
        self.ui.Attachment5.hide()
        self.attach.remove(self.attach[4])

    def condicional(self):
        self.ui.Output.setText('In progress...')

    def sendEmails(self):
        if self.login == None:
            try: self.login = Email(self.ui.Email.text(), self.ui.Password.text(), self.ui.Port.text(), self.ui.API.text())
            except Exception as ex: return self.error(f"Unable to login. {ex}")

        self.ui.Output.setText('')

        try: self.login.send(self.ui.Destination.text(), self.ui.Subject.text(), text_part, self.attach)
        except Exception as ex: self.error(f"Failed to send email to {self.ui.Destination.text()}: {ex}")

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
