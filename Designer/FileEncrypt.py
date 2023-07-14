# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FileEncrypt.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSplitter, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(957, 717)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_4 = QSpacerItem(20, 102, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.HeaderLabel = QLabel(Form)
        self.HeaderLabel.setObjectName(u"HeaderLabel")
        font = QFont()
        font.setFamilies([u"Rockwell"])
        font.setPointSize(28)
        font.setBold(True)
        self.HeaderLabel.setFont(font)
        self.HeaderLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.HeaderLabel)

        self.verticalSpacer = QSpacerItem(20, 103, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(self.frame)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.FileSelect = QLineEdit(self.splitter)
        self.FileSelect.setObjectName(u"FileSelect")
        self.FileSelect.setMinimumSize(QSize(30, 0))
        self.splitter.addWidget(self.FileSelect)
        self.BtnChooseFile = QPushButton(self.splitter)
        self.BtnChooseFile.setObjectName(u"BtnChooseFile")
        self.BtnChooseFile.setMaximumSize(QSize(200, 16777215))
        self.splitter.addWidget(self.BtnChooseFile)

        self.verticalLayout.addWidget(self.splitter)

        self.splitter_2 = QSplitter(self.frame)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.FileSave = QLineEdit(self.splitter_2)
        self.FileSave.setObjectName(u"FileSave")
        self.FileSave.setMinimumSize(QSize(30, 0))
        self.splitter_2.addWidget(self.FileSave)
        self.BtnSaveFile = QPushButton(self.splitter_2)
        self.BtnSaveFile.setObjectName(u"BtnSaveFile")
        self.BtnSaveFile.setMaximumSize(QSize(200, 16777215))
        self.splitter_2.addWidget(self.BtnSaveFile)

        self.verticalLayout.addWidget(self.splitter_2)

        self.HashKey = QLineEdit(self.frame)
        self.HashKey.setObjectName(u"HashKey")
        self.HashKey.setMinimumSize(QSize(40, 0))

        self.verticalLayout.addWidget(self.HashKey)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Rockwell Condensed"])
        font1.setPointSize(12)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.BtnEncrypt = QPushButton(self.frame)
        self.BtnEncrypt.setObjectName(u"BtnEncrypt")
        self.BtnEncrypt.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.BtnEncrypt)

        self.BtnDecrypt = QPushButton(self.frame)
        self.BtnDecrypt.setObjectName(u"BtnDecrypt")
        self.BtnDecrypt.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.BtnDecrypt)

        self.BtnClear = QPushButton(self.frame)
        self.BtnClear.setObjectName(u"BtnClear")
        self.BtnClear.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.BtnClear)

        self.BtnMainMenu = QPushButton(self.frame)
        self.BtnMainMenu.setObjectName(u"BtnMainMenu")
        self.BtnMainMenu.setMaximumSize(QSize(200, 16777215))

        self.horizontalLayout.addWidget(self.BtnMainMenu)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.frame)

        self.verticalSpacer_2 = QSpacerItem(37, 102, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.verticalSpacer_3 = QSpacerItem(20, 102, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.HeaderLabel.setText(QCoreApplication.translate("Form", u"File Encryption and Decryption  ", None))
        self.FileSelect.setPlaceholderText(QCoreApplication.translate("Form", u"Choose file path", None))
        self.BtnChooseFile.setText(QCoreApplication.translate("Form", u"Choose File", None))
        self.FileSave.setPlaceholderText(QCoreApplication.translate("Form", u"Choose file Save Path", None))
        self.BtnSaveFile.setText(QCoreApplication.translate("Form", u"Save File ", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#ff0000;\">Make Sure that Your Hash Key is safe and secure this will be used for decryption of file </span></p></body></html>", None))
        self.BtnEncrypt.setText(QCoreApplication.translate("Form", u"Encrypt", None))
        self.BtnDecrypt.setText(QCoreApplication.translate("Form", u"Decrypt", None))
        self.BtnClear.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.BtnMainMenu.setText(QCoreApplication.translate("Form", u"Main Menu", None))
    # retranslateUi

