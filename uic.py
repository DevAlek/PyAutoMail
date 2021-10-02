# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowGyUxea.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QSize, QCoreApplication, Qt, QMetaObject
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(908, 429)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(2545254, 16777215))
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
        self.Attach.setFlat(False)

        self.Files.addWidget(self.Attach)

        self.TSV = QPushButton(self.centralwidget)
        self.TSV.setObjectName(u"TSV")

        self.Files.addWidget(self.TSV)


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


        self.EmailCfg.addLayout(self.SubjectField)

        self.EmailText = QTextEdit(self.centralwidget)
        self.EmailText.setObjectName(u"EmailText")

        self.EmailCfg.addWidget(self.EmailText)

        self.TSVCONFIG = QHBoxLayout()
        self.TSVCONFIG.setObjectName(u"TSVCONFIG")
        self.LabelTSV = QLabel(self.centralwidget)
        self.LabelTSV.setObjectName(u"LabelTSV")

        self.TSVCONFIG.addWidget(self.LabelTSV)

        self.TSVEmail = QLineEdit(self.centralwidget)
        self.TSVEmail.setObjectName(u"TSVEmail")

        self.TSVCONFIG.addWidget(self.TSVEmail)


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
        self.Output = QTextEdit(self.OutputSection)
        self.Output.setObjectName(u"Output")
        self.Output.setReadOnly(True)

        self.CheckSection.addWidget(self.Output)

        self.Buttons = QHBoxLayout()
        self.Buttons.setObjectName(u"Buttons")
        self.CheckReplace = QPushButton(self.OutputSection)
        self.CheckReplace.setObjectName(u"CheckReplace")

        self.Buttons.addWidget(self.CheckReplace)

        self.ManualButton = QPushButton(self.OutputSection)
        self.ManualButton.setObjectName(u"ManualButton")

        self.Buttons.addWidget(self.ManualButton)

        self.CheckTSV = QPushButton(self.OutputSection)
        self.CheckTSV.setObjectName(u"CheckTSV")

        self.Buttons.addWidget(self.CheckTSV)


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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AutoEmail", None))
        MainWindow.setProperty("Man", "")
        self.Error.setMarkdown("")
        self.Error.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.CloseError.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.zP.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.Password.setText("")
        self.zK.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.Attach.setText(QCoreApplication.translate("MainWindow", u"Attach File", None))
        self.TSV.setText(QCoreApplication.translate("MainWindow", u"DataBank (.tsv file)", None))
        self.SubjectT.setText(QCoreApplication.translate("MainWindow", u"Email Subject", None))
        self.EmailText.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email text here. We also accept html scripts and the replace commands works here too.", None))
        self.LabelTSV.setText(QCoreApplication.translate("MainWindow", u"TSV column for email", None))
        self.Show.setText(QCoreApplication.translate("MainWindow", u"Show output section", None))
        self.Output.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Output will be shown here!", None))
        self.Output.setProperty("Manual", "")
        self.CheckReplace.setText(QCoreApplication.translate("MainWindow", u"Check TSV DataSlots", None))
        self.ManualButton.setText(QCoreApplication.translate("MainWindow", u"Check Replace Output", None))
        self.CheckTSV.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
    # retranslateUi
