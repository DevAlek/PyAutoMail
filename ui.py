# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from PySide6.QtWebEngineWidgets import QWebEngineView


import qrc as Resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(791, 575)
        icon = QIcon()
        icon.addFile(u":/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionLoad_csv_file = QAction(MainWindow)
        self.actionLoad_csv_file.setObjectName(u"actionLoad_csv_file")
        self.actionSave_configurations = QAction(MainWindow)
        self.actionSave_configurations.setObjectName(u"actionSave_configurations")
        self.actionLoad_configurations = QAction(MainWindow)
        self.actionLoad_configurations.setObjectName(u"actionLoad_configurations")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Title = QLabel(self.centralwidget)
        self.Title.setObjectName(u"Title")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Title.sizePolicy().hasHeightForWidth())
        self.Title.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(28)
        self.Title.setFont(font)
        self.Title.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.Title, 0, 0, 1, 1)

        self.splitter_7 = QSplitter(self.centralwidget)
        self.splitter_7.setObjectName(u"splitter_7")
        self.splitter_7.setOrientation(Qt.Vertical)
        self.splitter_5 = QSplitter(self.splitter_7)
        self.splitter_5.setObjectName(u"splitter_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.splitter_5.sizePolicy().hasHeightForWidth())
        self.splitter_5.setSizePolicy(sizePolicy1)
        self.splitter_5.setOrientation(Qt.Vertical)
        self.splitter = QSplitter(self.splitter_5)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.scrollArea = QScrollArea(self.splitter)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 414, 314))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.splitter_3 = QSplitter(self.scrollAreaWidgetContents_4)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Vertical)
        self.scrollArea_3 = QScrollArea(self.splitter_3)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setFrameShape(QFrame.NoFrame)
        self.scrollArea_3.setFrameShadow(QFrame.Plain)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 382, 150))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.scrollAreaWidgetContents_6)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.formLayout_2 = QFormLayout(self.frame)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.LEmail = QLabel(self.frame)
        self.LEmail.setObjectName(u"LEmail")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.LEmail)

        self.Email = QLineEdit(self.frame)
        self.Email.setObjectName(u"Email")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.Email)

        self.LPassword = QLabel(self.frame)
        self.LPassword.setObjectName(u"LPassword")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.LPassword)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Password = QLineEdit(self.frame)
        self.Password.setObjectName(u"Password")
        self.Password.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.Password)

        self.ShowPassword = QPushButton(self.frame)
        self.ShowPassword.setObjectName(u"ShowPassword")
        icon1 = QIcon()
        iconThemeName = u"hint"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.ShowPassword.setIcon(icon1)
        self.ShowPassword.setCheckable(True)
        self.ShowPassword.setFlat(True)

        self.horizontalLayout_2.addWidget(self.ShowPassword)


        self.formLayout_2.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_2)

        self.LEmailService = QLabel(self.frame)
        self.LEmailService.setObjectName(u"LEmailService")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.LEmailService)

        self.EmailService = QComboBox(self.frame)
        self.EmailService.addItem("")
        self.EmailService.addItem("")
        self.EmailService.addItem("")
        self.EmailService.addItem("")
        self.EmailService.addItem("")
        self.EmailService.setObjectName(u"EmailService")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.EmailService)

        self.LCustomService = QLabel(self.frame)
        self.LCustomService.setObjectName(u"LCustomService")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.LCustomService)

        self.CustomService = QLineEdit(self.frame)
        self.CustomService.setObjectName(u"CustomService")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.CustomService)


        self.verticalLayout_2.addWidget(self.frame)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_6)
        self.splitter_3.addWidget(self.scrollArea_3)
        self.scrollArea_4 = QScrollArea(self.splitter_3)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setFrameShape(QFrame.NoFrame)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 396, 181))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents_7)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.LSubject = QLabel(self.scrollAreaWidgetContents_7)
        self.LSubject.setObjectName(u"LSubject")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.LSubject)

        self.Subject = QLineEdit(self.scrollAreaWidgetContents_7)
        self.Subject.setObjectName(u"Subject")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.Subject)


        self.verticalLayout_3.addLayout(self.formLayout)


        self.gridLayout.addLayout(self.verticalLayout_3, 2, 0, 1, 1)

        self.Input = QTextEdit(self.scrollAreaWidgetContents_7)
        self.Input.setObjectName(u"Input")

        self.gridLayout.addWidget(self.Input, 4, 0, 1, 1)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_7)
        self.splitter_3.addWidget(self.scrollArea_4)

        self.gridLayout_3.addWidget(self.splitter_3, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_4)
        self.splitter.addWidget(self.scrollArea)
        self.frame1 = QFrame(self.splitter)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setFrameShape(QFrame.NoFrame)
        self.frame1.setFrameShadow(QFrame.Plain)
        self.frame1.setLineWidth(0)
        self.gridLayout_2 = QGridLayout(self.frame1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.splitter_2 = QSplitter(self.frame1)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.scrollArea_2 = QScrollArea(self.splitter_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setFrameShadow(QFrame.Plain)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 337, 296))
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.splitter_6 = QSplitter(self.scrollAreaWidgetContents_5)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setOrientation(Qt.Vertical)
        self.horizontalLayoutWidget = QWidget(self.splitter_6)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Save = QPushButton(self.horizontalLayoutWidget)
        self.Save.setObjectName(u"Save")

        self.horizontalLayout.addWidget(self.Save)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.Load = QPushButton(self.horizontalLayoutWidget)
        self.Load.setObjectName(u"Load")

        self.horizontalLayout.addWidget(self.Load)

        self.splitter_6.addWidget(self.horizontalLayoutWidget)
        self.splitter_4 = QSplitter(self.splitter_6)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Vertical)
        self.Table = QTableWidget(self.splitter_4)
        if (self.Table.columnCount() < 25):
            self.Table.setColumnCount(25)
        __qtablewidgetitem = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(16, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(17, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(18, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(19, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(20, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(21, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(22, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(23, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.Table.setHorizontalHeaderItem(24, __qtablewidgetitem24)
        if (self.Table.rowCount() < 10):
            self.Table.setRowCount(10)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.Table.setVerticalHeaderItem(0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.Table.setVerticalHeaderItem(1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.Table.setVerticalHeaderItem(2, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.Table.setVerticalHeaderItem(3, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.Table.setVerticalHeaderItem(4, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.Table.setVerticalHeaderItem(5, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.Table.setVerticalHeaderItem(6, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.Table.setVerticalHeaderItem(7, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.Table.setVerticalHeaderItem(8, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.Table.setVerticalHeaderItem(9, __qtablewidgetitem34)
        self.Table.setObjectName(u"Table")
        self.splitter_4.addWidget(self.Table)
        self.Preview = QWebEngineView(self.splitter_4)
        self.Preview.setObjectName(u"Preview")
        self.Preview.setUrl(QUrl(u"file:///home/alek/.cache/Carrier Pigeon/preview.html"))
        self.splitter_4.addWidget(self.Preview)
        self.splitter_6.addWidget(self.splitter_4)

        self.gridLayout_5.addWidget(self.splitter_6, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_5)
        self.splitter_2.addWidget(self.scrollArea_2)

        self.gridLayout_2.addWidget(self.splitter_2, 0, 0, 1, 1)

        self.splitter.addWidget(self.frame1)
        self.splitter_5.addWidget(self.splitter)
        self.splitter_7.addWidget(self.splitter_5)
        self.Output = QTextEdit(self.splitter_7)
        self.Output.setObjectName(u"Output")
        self.Output.setReadOnly(True)
        self.splitter_7.addWidget(self.Output)

        self.gridLayout_4.addWidget(self.splitter_7, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Carrier Pigeon", None))
        self.actionLoad_csv_file.setText(QCoreApplication.translate("MainWindow", u"Load csv file", None))
        self.actionSave_configurations.setText(QCoreApplication.translate("MainWindow", u"Save configurations", None))
        self.actionLoad_configurations.setText(QCoreApplication.translate("MainWindow", u"Load configurations", None))
        self.Title.setText(QCoreApplication.translate("MainWindow", u"Carrier Pigeon", None))
        self.LEmail.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.Email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"username@domain.tld", None))
        self.LPassword.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.Password.setInputMask("")
        self.Password.setText("")
        self.Password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"********", None))
        self.ShowPassword.setText("")
        self.LEmailService.setText(QCoreApplication.translate("MainWindow", u"Email Service", None))
        self.EmailService.setItemText(0, QCoreApplication.translate("MainWindow", u"Gmail", None))
        self.EmailService.setItemText(1, QCoreApplication.translate("MainWindow", u"Hotmail", None))
        self.EmailService.setItemText(2, QCoreApplication.translate("MainWindow", u"YahooMail", None))
        self.EmailService.setItemText(3, QCoreApplication.translate("MainWindow", u"Protonmail", None))
        self.EmailService.setItemText(4, QCoreApplication.translate("MainWindow", u"Other", None))

        self.EmailService.setCurrentText(QCoreApplication.translate("MainWindow", u"Gmail", None))
        self.LCustomService.setText(QCoreApplication.translate("MainWindow", u"Other Service", None))
        self.CustomService.setPlaceholderText(QCoreApplication.translate("MainWindow", u"smtp.email.tld", None))
        self.LSubject.setText(QCoreApplication.translate("MainWindow", u"Email subject", None))
        self.Subject.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Title goes here!", None))
        self.Input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email content goes here!", None))
        self.Save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Table data", None))
        self.Load.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        ___qtablewidgetitem = self.Table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"a", None));
        ___qtablewidgetitem1 = self.Table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"b", None));
        ___qtablewidgetitem2 = self.Table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"c", None));
        ___qtablewidgetitem3 = self.Table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"d", None));
        ___qtablewidgetitem4 = self.Table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"e", None));
        ___qtablewidgetitem5 = self.Table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"f", None));
        ___qtablewidgetitem6 = self.Table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"g", None));
        ___qtablewidgetitem7 = self.Table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"h", None));
        ___qtablewidgetitem8 = self.Table.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"i", None));
        ___qtablewidgetitem9 = self.Table.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"j", None));
        ___qtablewidgetitem10 = self.Table.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"k", None));
        ___qtablewidgetitem11 = self.Table.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"l", None));
        ___qtablewidgetitem12 = self.Table.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"m", None));
        ___qtablewidgetitem13 = self.Table.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"o", None));
        ___qtablewidgetitem14 = self.Table.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"p", None));
        ___qtablewidgetitem15 = self.Table.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"q", None));
        ___qtablewidgetitem16 = self.Table.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"r", None));
        ___qtablewidgetitem17 = self.Table.horizontalHeaderItem(17)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"s", None));
        ___qtablewidgetitem18 = self.Table.horizontalHeaderItem(18)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"t", None));
        ___qtablewidgetitem19 = self.Table.horizontalHeaderItem(19)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"u", None));
        ___qtablewidgetitem20 = self.Table.horizontalHeaderItem(20)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"v", None));
        ___qtablewidgetitem21 = self.Table.horizontalHeaderItem(21)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"w", None));
        ___qtablewidgetitem22 = self.Table.horizontalHeaderItem(22)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"x", None));
        ___qtablewidgetitem23 = self.Table.horizontalHeaderItem(23)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem24 = self.Table.horizontalHeaderItem(24)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"z", None));
        ___qtablewidgetitem25 = self.Table.verticalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem26 = self.Table.verticalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem27 = self.Table.verticalHeaderItem(2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem28 = self.Table.verticalHeaderItem(3)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem29 = self.Table.verticalHeaderItem(4)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem30 = self.Table.verticalHeaderItem(5)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem31 = self.Table.verticalHeaderItem(6)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem32 = self.Table.verticalHeaderItem(7)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem33 = self.Table.verticalHeaderItem(8)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem34 = self.Table.verticalHeaderItem(9)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"10", None));
        self.Output.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The output will be shown here! (and at the terminal)", None))
    # retranslateUi

