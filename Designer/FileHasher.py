# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FileHasher.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSplitter, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(950, 711)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 51, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.Title = QLabel(Form)
        self.Title.setObjectName(u"Title")
        font = QFont()
        font.setFamilies([u"Rockwell"])
        font.setPointSize(26)
        font.setBold(True)
        self.Title.setFont(font)
        self.Title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Title)

        self.verticalSpacer = QSpacerItem(20, 51, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.splitter = QSplitter(self.frame)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.File_Path = QLineEdit(self.splitter)
        self.File_Path.setObjectName(u"File_Path")
        self.File_Path.setMinimumSize(QSize(0, 30))
        self.File_Path.setMaximumSize(QSize(700, 16777215))
        self.splitter.addWidget(self.File_Path)
        self.BtnFile = QPushButton(self.splitter)
        self.BtnFile.setObjectName(u"BtnFile")
        self.BtnFile.setMaximumSize(QSize(200, 16777215))
        self.splitter.addWidget(self.BtnFile)

        self.verticalLayout_2.addWidget(self.splitter)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Rockwell"])
        font1.setPointSize(14)
        self.label.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 0))
        self.lineEdit_3.setMaximumSize(QSize(700, 16777215))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.formLayout.setItem(1, QFormLayout.LabelRole, self.horizontalSpacer)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.lineEdit_4 = QLineEdit(self.frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 0))
        self.lineEdit_4.setMaximumSize(QSize(700, 16777215))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.formLayout.setItem(3, QFormLayout.LabelRole, self.horizontalSpacer_2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_5 = QLineEdit(self.frame)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(0, 0))
        self.lineEdit_5.setMaximumSize(QSize(700, 16777215))

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_5)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.formLayout.setItem(5, QFormLayout.LabelRole, self.horizontalSpacer_3)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_6 = QLineEdit(self.frame)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(0, 0))
        self.lineEdit_6.setMaximumSize(QSize(700, 16777215))

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lineEdit_6)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.formLayout.setItem(7, QFormLayout.LabelRole, self.horizontalSpacer_4)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_5)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(700, 16777215))

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.lineEdit)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_6)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label_7)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.formLayout.setItem(9, QFormLayout.LabelRole, self.horizontalSpacer_5)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.formLayout.setItem(11, QFormLayout.LabelRole, self.horizontalSpacer_6)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.formLayout.setItem(13, QFormLayout.LabelRole, self.horizontalSpacer_7)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(700, 16777215))

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.lineEdit_2)

        self.lineEdit_7 = QLineEdit(self.frame)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMaximumSize(QSize(700, 16777215))

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.lineEdit_7)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(200, -1, 200, -1)
        self.BtSubmit = QPushButton(self.frame)
        self.BtSubmit.setObjectName(u"BtSubmit")
        self.BtSubmit.setMinimumSize(QSize(0, 30))
        self.BtSubmit.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout.addWidget(self.BtSubmit)

        self.BtnMainMenu = QPushButton(self.frame)
        self.BtnMainMenu.setObjectName(u"BtnMainMenu")
        self.BtnMainMenu.setMinimumSize(QSize(0, 30))
        self.BtnMainMenu.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout.addWidget(self.BtnMainMenu)

        self.BtnClear = QPushButton(self.frame)
        self.BtnClear.setObjectName(u"BtnClear")
        self.BtnClear.setMinimumSize(QSize(0, 30))
        self.BtnClear.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout.addWidget(self.BtnClear)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.frame)

        self.verticalSpacer_3 = QSpacerItem(20, 51, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.verticalSpacer_5 = QSpacerItem(20, 51, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Title.setText(QCoreApplication.translate("Form", u"File Hasher ", None))
        self.BtnFile.setText(QCoreApplication.translate("Form", u"Choose File ", None))
        self.label.setText(QCoreApplication.translate("Form", u"MD5 Hash Value ", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"SHA256  Hash Value ", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Blake 2 Hash Value ", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"SHA 3 Hash Value ", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"SHA 512", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"CRC 32", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"SHA 224", None))
        self.BtSubmit.setText(QCoreApplication.translate("Form", u"Submit", None))
        self.BtnMainMenu.setText(QCoreApplication.translate("Form", u"Main menu", None))
        self.BtnClear.setText(QCoreApplication.translate("Form", u"Clear", None))
    # retranslateUi

