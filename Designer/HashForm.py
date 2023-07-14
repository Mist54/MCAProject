# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HashForm.ui'
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
                               QLabel, QPushButton, QSizePolicy, QSpacerItem,
                               QSplitter, QTextEdit, QVBoxLayout, QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(955, 804)
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer_5 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.Header_Label = QLabel(Form)
        self.Header_Label.setObjectName(u"Header_Label")
        font = QFont()
        font.setFamilies([u"Rockwell"])
        font.setPointSize(26)
        font.setBold(True)
        self.Header_Label.setFont(font)
        self.Header_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.Header_Label)

        self.verticalSpacer_4 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(150, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Encrypt_Label = QLabel(self.frame)
        self.Encrypt_Label.setObjectName(u"Encrypt_Label")
        font1 = QFont()
        font1.setFamilies([u"Rockwell"])
        font1.setPointSize(18)
        self.Encrypt_Label.setFont(font1)
        self.Encrypt_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Encrypt_Label)

        self.Encrypt_Text = QTextEdit(self.frame)
        self.Encrypt_Text.setObjectName(u"Encrypt_Text")

        self.verticalLayout.addWidget(self.Encrypt_Text)

        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.Hash_Text = QTextEdit(self.frame)
        self.Hash_Text.setObjectName(u"Hash_Text")

        self.verticalLayout_2.addWidget(self.Hash_Text)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.MD5_Encrypt = QPushButton(self.frame)
        self.MD5_Encrypt.setObjectName(u"MD5_Encrypt")
        self.MD5_Encrypt.setMinimumSize(QSize(120, 30))
        font2 = QFont()
        font2.setFamilies([u"Rockwell"])
        font2.setPointSize(10)
        self.MD5_Encrypt.setFont(font2)
        self.MD5_Encrypt.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.MD5_Encrypt)

        self.SHA_3 = QPushButton(self.frame)
        self.SHA_3.setObjectName(u"SHA_3")
        self.SHA_3.setMinimumSize(QSize(120, 30))
        self.SHA_3.setFont(font2)
        self.SHA_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.SHA_3)

        self.Blake_2 = QPushButton(self.frame)
        self.Blake_2.setObjectName(u"Blake_2")
        self.Blake_2.setMinimumSize(QSize(120, 30))
        self.Blake_2.setFont(font2)
        self.Blake_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.Blake_2)

        self.SHA_256 = QPushButton(self.frame)
        self.SHA_256.setObjectName(u"SHA_256")
        self.SHA_256.setMinimumSize(QSize(120, 30))
        self.SHA_256.setFont(font2)
        self.SHA_256.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.SHA_256)

        self.Btn_Clear = QPushButton(self.frame)
        self.Btn_Clear.setObjectName(u"Btn_Clear")
        self.Btn_Clear.setMinimumSize(QSize(120, 30))
        self.Btn_Clear.setFont(font2)
        self.Btn_Clear.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.Btn_Clear)

        self.Btn_MainMenu = QPushButton(self.frame)
        self.Btn_MainMenu.setObjectName(u"Btn_MainMenu")
        self.Btn_MainMenu.setMinimumSize(QSize(120, 30))
        self.Btn_MainMenu.setFont(font2)
        self.Btn_MainMenu.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.Btn_MainMenu)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout_4.addWidget(self.frame)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_2)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignCenter)
        self.formLayout.setContentsMargins(200, -1, -1, -1)
        self.splitter = QSplitter(self.frame_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.splitter)

        self.Hash_Identify = QLabel(self.frame_2)
        self.Hash_Identify.setObjectName(u"Hash_Identify")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.Hash_Identify)

        self.verticalLayout_4.addWidget(self.frame_2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Header_Label.setText(QCoreApplication.translate("Form", u"Encrpyption System", None))
        self.Encrypt_Label.setText(QCoreApplication.translate("Form", u"Enter the text : ", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Hashed Text :", None))
        self.MD5_Encrypt.setText(QCoreApplication.translate("Form", u"MD5 Encryption ", None))
        self.SHA_3.setText(QCoreApplication.translate("Form", u"SHA -3 ", None))
        self.Blake_2.setText(QCoreApplication.translate("Form", u"Blake-2 ", None))
        self.SHA_256.setText(QCoreApplication.translate("Form", u"SHA 256", None))
        self.Btn_Clear.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.Btn_MainMenu.setText(QCoreApplication.translate("Form", u"Main Menu", None))
        self.Hash_Identify.setText("")
    # retranslateUi
