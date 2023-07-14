# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FileCompressyCnedW.ui'
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
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(878, 480)
        Form.setMinimumSize(QSize(640, 480))
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Rockwell"])
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.ChooseFile = QLineEdit(self.frame)
        self.ChooseFile.setObjectName(u"ChooseFile")
        self.ChooseFile.setMinimumSize(QSize(700, 25))
        self.ChooseFile.setMaximumSize(QSize(16777215, 16777215))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.ChooseFile)

        self.BtnFileChoose = QPushButton(self.frame)
        self.BtnFileChoose.setObjectName(u"BtnFileChoose")
        self.BtnFileChoose.setMaximumSize(QSize(200, 16777215))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.BtnFileChoose)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.RdZip = QRadioButton(self.frame)
        self.RdZip.setObjectName(u"RdZip")
        self.RdZip.setChecked(True)

        self.horizontalLayout.addWidget(self.RdZip)

        self.RdRAR = QRadioButton(self.frame)
        self.RdRAR.setObjectName(u"RdRAR")

        self.horizontalLayout.addWidget(self.RdRAR)

        self.RdBzip = QRadioButton(self.frame)
        self.RdBzip.setObjectName(u"RdBzip")

        self.horizontalLayout.addWidget(self.RdBzip)

        self.Rd7z = QRadioButton(self.frame)
        self.Rd7z.setObjectName(u"Rd7z")

        self.horizontalLayout.addWidget(self.Rd7z)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.BtnCompress = QPushButton(self.frame)
        self.BtnCompress.setObjectName(u"BtnCompress")

        self.horizontalLayout_2.addWidget(self.BtnCompress)

        self.BtnDecompress = QPushButton(self.frame)
        self.BtnDecompress.setObjectName(u"BtnDecompress")

        self.horizontalLayout_2.addWidget(self.BtnDecompress)

        self.BtnMainMenu = QPushButton(self.frame)
        self.BtnMainMenu.setObjectName(u"BtnMainMenu")

        self.horizontalLayout_2.addWidget(self.BtnMainMenu)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"File Compression and Decompression ", None))
        self.BtnFileChoose.setText(QCoreApplication.translate("Form", u"Choose File", None))
        self.RdZip.setText(QCoreApplication.translate("Form", u"Zip Compression", None))
        self.RdRAR.setText(QCoreApplication.translate("Form", u"TAR Compression", None))
        self.RdBzip.setText(QCoreApplication.translate("Form", u"BZip Compression", None))
        self.Rd7z.setText(QCoreApplication.translate("Form", u"7z Compression ", None))
        self.BtnCompress.setText(QCoreApplication.translate("Form", u"Compress", None))
        self.BtnDecompress.setText(QCoreApplication.translate("Form", u"Decompress", None))
        self.BtnMainMenu.setText(QCoreApplication.translate("Form", u"MainMenu", None))
    # retranslateUi

