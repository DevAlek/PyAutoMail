# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pymailxoUMYs.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1029, 462)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(2545254, 16777215))
        MainWindow.setAcceptDrops(True)
        icon = QIcon()
        icon.addFile(u"../PyAutoMail/pyautomail.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setMaximumSize(QSize(2545254, 16777215))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Layout = QVBoxLayout()
        self.Layout.setObjectName(u"Layout")
        self.TheErrorPlace = QFrame(self.centralwidget)
        self.TheErrorPlace.setObjectName(u"TheErrorPlace")
        self.TheErrorPlace.setMaximumSize(QSize(16777215, 40))
        self.ErrorPlace = QHBoxLayout(self.TheErrorPlace)
        self.ErrorPlace.setObjectName(u"ErrorPlace")
        self.Error = QTextEdit(self.TheErrorPlace)
        self.Error.setObjectName(u"Error")
        self.Error.setMaximumSize(QSize(16777215, 30))
        self.Error.setStyleSheet(u"background-color: rgba(255, 0, 4, 100);\n"
"border-color: rgb(255, 0, 4);")
        self.Error.setReadOnly(True)

        self.ErrorPlace.addWidget(self.Error)

        self.CloseError = QPushButton(self.TheErrorPlace)
        self.CloseError.setObjectName(u"CloseError")
        self.CloseError.setStyleSheet(u"background-color: rgba(255, 0, 4, 100);\n"
"border-color: rgb(255, 0, 4);")

        self.ErrorPlace.addWidget(self.CloseError)


        self.Layout.addWidget(self.TheErrorPlace)

        self.Align = QHBoxLayout()
        self.Align.setObjectName(u"Align")
        self.Align.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.Main = QVBoxLayout()
        self.Main.setObjectName(u"Main")
        self.Form = QHBoxLayout()
        self.Form.setObjectName(u"Form")
        self.Login = QFormLayout()
        self.Login.setObjectName(u"Login")
        self.zP = QLabel(self.centralwidget)
        self.zP.setObjectName(u"zP")

        self.Login.setWidget(1, QFormLayout.LabelRole, self.zP)

        self.Email = QLineEdit(self.centralwidget)
        self.Email.setObjectName(u"Email")

        self.Login.setWidget(0, QFormLayout.FieldRole, self.Email)

        self.Password = QLineEdit(self.centralwidget)
        self.Password.setObjectName(u"Password")
        self.Password.setEchoMode(QLineEdit.Password)

        self.Login.setWidget(1, QFormLayout.FieldRole, self.Password)

        self.zK = QLabel(self.centralwidget)
        self.zK.setObjectName(u"zK")

        self.Login.setWidget(0, QFormLayout.LabelRole, self.zK)


        self.Form.addLayout(self.Login)

        self.Files = QVBoxLayout()
        self.Files.setObjectName(u"Files")
        self.Attach = QPushButton(self.centralwidget)
        self.Attach.setObjectName(u"Attach")
        self.Attach.setMouseTracking(False)
        self.Attach.setAcceptDrops(True)
        self.Attach.setFlat(False)

        self.Files.addWidget(self.Attach)


        self.Form.addLayout(self.Files)


        self.Main.addLayout(self.Form)

        self.EmailCfg = QVBoxLayout()
        self.EmailCfg.setObjectName(u"EmailCfg")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.EmailCfg.addWidget(self.line)

        self.SubjectField = QFormLayout()
        self.SubjectField.setObjectName(u"SubjectField")
        self.SubjectT = QLabel(self.centralwidget)
        self.SubjectT.setObjectName(u"SubjectT")

        self.SubjectField.setWidget(0, QFormLayout.LabelRole, self.SubjectT)

        self.Subject = QLineEdit(self.centralwidget)
        self.Subject.setObjectName(u"Subject")

        self.SubjectField.setWidget(0, QFormLayout.FieldRole, self.Subject)

        self.destinationLabel = QLabel(self.centralwidget)
        self.destinationLabel.setObjectName(u"destinationLabel")

        self.SubjectField.setWidget(1, QFormLayout.LabelRole, self.destinationLabel)

        self.Destination = QLineEdit(self.centralwidget)
        self.Destination.setObjectName(u"Destination")

        self.SubjectField.setWidget(1, QFormLayout.FieldRole, self.Destination)


        self.EmailCfg.addLayout(self.SubjectField)

        self.EmailText = QTextEdit(self.centralwidget)
        self.EmailText.setObjectName(u"EmailText")

        self.EmailCfg.addWidget(self.EmailText)

        self.Attachments_2 = QFrame(self.centralwidget)
        self.Attachments_2.setObjectName(u"Attachments_2")
        self.Attachments = QHBoxLayout(self.Attachments_2)
        self.Attachments.setObjectName(u"Attachments")
        self.Attachment1 = QPushButton(self.Attachments_2)
        self.Attachment1.setObjectName(u"Attachment1")

        self.Attachments.addWidget(self.Attachment1)

        self.Attachment2 = QPushButton(self.Attachments_2)
        self.Attachment2.setObjectName(u"Attachment2")

        self.Attachments.addWidget(self.Attachment2)

        self.Attachment3 = QPushButton(self.Attachments_2)
        self.Attachment3.setObjectName(u"Attachment3")

        self.Attachments.addWidget(self.Attachment3)

        self.Attachment4 = QPushButton(self.Attachments_2)
        self.Attachment4.setObjectName(u"Attachment4")

        self.Attachments.addWidget(self.Attachment4)

        self.Attachment5 = QPushButton(self.Attachments_2)
        self.Attachment5.setObjectName(u"Attachment5")

        self.Attachments.addWidget(self.Attachment5)


        self.EmailCfg.addWidget(self.Attachments_2)

        self.TSVCONFIG = QHBoxLayout()
        self.TSVCONFIG.setObjectName(u"TSVCONFIG")

        self.EmailCfg.addLayout(self.TSVCONFIG)


        self.Main.addLayout(self.EmailCfg)

        self.Footer = QHBoxLayout()
        self.Footer.setObjectName(u"Footer")
        self.Show = QCheckBox(self.centralwidget)
        self.Show.setObjectName(u"Show")

        self.Footer.addWidget(self.Show)

        self.Confirm = QDialogButtonBox(self.centralwidget)
        self.Confirm.setObjectName(u"Confirm")
        self.Confirm.setLayoutDirection(Qt.LeftToRight)
        self.Confirm.setOrientation(Qt.Horizontal)
        self.Confirm.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.Confirm.setCenterButtons(False)

        self.Footer.addWidget(self.Confirm)


        self.Main.addLayout(self.Footer)


        self.Align.addLayout(self.Main)

        self.Sep = QFrame(self.centralwidget)
        self.Sep.setObjectName(u"Sep")
        self.Sep.setFrameShape(QFrame.VLine)
        self.Sep.setFrameShadow(QFrame.Sunken)

        self.Align.addWidget(self.Sep)

        self.OutputSection = QWidget(self.centralwidget)
        self.OutputSection.setObjectName(u"OutputSection")
        self.OutputSection.setEnabled(True)
        self.CheckSection = QVBoxLayout(self.OutputSection)
        self.CheckSection.setObjectName(u"CheckSection")
        self.APIarea = QHBoxLayout()
        self.APIarea.setObjectName(u"APIarea")
        self.LAPI = QLabel(self.OutputSection)
        self.LAPI.setObjectName(u"LAPI")

        self.APIarea.addWidget(self.LAPI)

        self.API = QLineEdit(self.OutputSection)
        self.API.setObjectName(u"API")

        self.APIarea.addWidget(self.API)

        self.LPORT = QLabel(self.OutputSection)
        self.LPORT.setObjectName(u"LPORT")

        self.APIarea.addWidget(self.LPORT)

        self.Port = QLineEdit(self.OutputSection)
        self.Port.setObjectName(u"Port")

        self.APIarea.addWidget(self.Port)


        self.CheckSection.addLayout(self.APIarea)

        self.Output = QTextEdit(self.OutputSection)
        self.Output.setObjectName(u"Output")
        self.Output.setReadOnly(True)

        self.CheckSection.addWidget(self.Output)

        self.Buttons = QHBoxLayout()
        self.Buttons.setObjectName(u"Buttons")
        self.Manual = QPushButton(self.OutputSection)
        self.Manual.setObjectName(u"Manual")

        self.Buttons.addWidget(self.Manual)


        self.CheckSection.addLayout(self.Buttons)


        self.Align.addWidget(self.OutputSection)


        self.Layout.addLayout(self.Align)


        self.gridLayout.addLayout(self.Layout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Show.toggled.connect(self.OutputSection.setVisible)
        self.Show.toggled.connect(self.Sep.setVisible)
        self.Confirm.rejected.connect(MainWindow.close)
        self.CloseError.pressed.connect(self.TheErrorPlace.hide)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PyEmail", None))
        MainWindow.setProperty("Man", "")
        self.Error.setMarkdown("")
        self.Error.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Noto Sans'; font-size:10pt;\"><br /></p></body></html>", None))
        self.CloseError.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.zP.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.Email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"my@email.com", None))
        self.Password.setText("")
        self.Password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"*************************", None))
        self.zK.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.Attach.setText(QCoreApplication.translate("MainWindow", u"Attach File", None))
        self.SubjectT.setText(QCoreApplication.translate("MainWindow", u"Email Subject", None))
        self.Subject.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Subject", None))
        self.destinationLabel.setText(QCoreApplication.translate("MainWindow", u"Destination: ", None))
        self.Destination.setPlaceholderText(QCoreApplication.translate("MainWindow", u"someone@somewhere.com", None))
        self.EmailText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email text here. We also accept html scripts and the replace commands works here too.", None))
        self.Attachment1.setText(QCoreApplication.translate("MainWindow", u"Attachment 1", None))
        self.Attachment2.setText(QCoreApplication.translate("MainWindow", u"Attachment 2", None))
        self.Attachment3.setText(QCoreApplication.translate("MainWindow", u"Attachment 3", None))
        self.Attachment4.setText(QCoreApplication.translate("MainWindow", u"Attachment 4", None))
        self.Attachment5.setText(QCoreApplication.translate("MainWindow", u"Attachment 5", None))
        self.Show.setText(QCoreApplication.translate("MainWindow", u"Show tools section", None))
        self.LAPI.setText(QCoreApplication.translate("MainWindow", u"Server API", None))
        self.API.setText(QCoreApplication.translate("MainWindow", u"smtp.gmail.com", None))
        self.LPORT.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.Port.setText(QCoreApplication.translate("MainWindow", u"587", None))
        self.Output.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Output will be shown here!", None))
        self.Output.setProperty("Manual", "")
        self.Manual.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
    # retranslateUi
