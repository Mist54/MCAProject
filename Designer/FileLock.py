# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FileLockIEfZrj.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(900, 600)
        Form.setMinimumSize(QSize(900, 600))
        Form.setMaximumSize(QSize(900, 600))
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Rockwell"])
        font.setPointSize(28)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.TxtChooseFile = QLineEdit(self.frame)
        self.TxtChooseFile.setObjectName(u"TxtChooseFile")
        self.TxtChooseFile.setMinimumSize(QSize(600, 25))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.TxtChooseFile)

        self.BtnChooseFile = QPushButton(self.frame)
        self.BtnChooseFile.setObjectName(u"BtnChooseFile")
        self.BtnChooseFile.setMinimumSize(QSize(0, 27))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.BtnChooseFile)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Rockwell"])
        font1.setPointSize(14)
        self.label.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.TxtPassword = QLineEdit(self.frame)
        self.TxtPassword.setObjectName(u"TxtPassword")
        self.TxtPassword.setMinimumSize(QSize(400, 0))
        self.TxtPassword.setFont(font1)
        self.TxtPassword.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.TxtPassword)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.formLayout_2.setItem(2, QFormLayout.FieldRole, self.horizontalSpacer)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.TxtConfirmPassword = QLineEdit(self.frame)
        self.TxtConfirmPassword.setObjectName(u"TxtConfirmPassword")
        self.TxtConfirmPassword.setMinimumSize(QSize(400, 0))
        self.TxtConfirmPassword.setFont(font1)
        self.TxtConfirmPassword.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.TxtConfirmPassword)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setFamilies([u"Rockwell Condensed"])
        font2.setPointSize(12)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.label_4)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.BtnSubmit = QPushButton(self.frame)
        self.BtnSubmit.setObjectName(u"BtnSubmit")
        self.BtnSubmit.setMinimumSize(QSize(0, 25))

        self.horizontalLayout.addWidget(self.BtnSubmit)

        self.BtnExtract = QPushButton(self.frame)
        self.BtnExtract.setObjectName(u"BtnExtract")
        self.BtnExtract.setMinimumSize(QSize(0, 25))

        self.horizontalLayout.addWidget(self.BtnExtract)

        self.BtnClose = QPushButton(self.frame)
        self.BtnClose.setObjectName(u"BtnClose")
        self.BtnClose.setMinimumSize(QSize(0, 25))

        self.horizontalLayout.addWidget(self.BtnClose)

        self.BtnMainMenu = QPushButton(self.frame)
        self.BtnMainMenu.setObjectName(u"BtnMainMenu")
        self.BtnMainMenu.setMinimumSize(QSize(0, 25))

        self.horizontalLayout.addWidget(self.BtnMainMenu)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"File Locking System", None))
        self.TxtChooseFile.setPlaceholderText(QCoreApplication.translate("Form", u"Choose your File Location", None))
        self.BtnChooseFile.setText(QCoreApplication.translate("Form", u"Select your file ", None))
        self.label.setText(QCoreApplication.translate("Form", u"Enter Your Password ", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Confirm Your Password", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Make Sure to rememeber your password and store it in safe place ", None))
        self.BtnSubmit.setText(QCoreApplication.translate("Form", u"Submit", None))
        self.BtnExtract.setText(QCoreApplication.translate("Form", u"Extract", None))
        self.BtnClose.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.BtnMainMenu.setText(QCoreApplication.translate("Form", u"Main Menu", None))
    # retranslateUi

