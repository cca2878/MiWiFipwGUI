# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QRect, QMetaObject, QCoreApplication  # type: ignore
from PySide6.QtWidgets import QPushButton, QLineEdit, QLabel, QWidget, QTextEdit  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(427, 202)
        # 禁止更改大小
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 55, 16))
        self.snEdit = QLineEdit(self.centralwidget)
        self.snEdit.setObjectName(u"snEdit")
        self.snEdit.setGeometry(QRect(40, 20, 381, 20))

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 50, 411, 24))

        

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 80, 55, 16))
        self.pwEdit = QTextEdit(self.centralwidget)
        self.pwEdit.setObjectName(u"pwEdit")
        self.pwEdit.setGeometry(QRect(10, 100, 411, 71))
        self.pwEdit.setReadOnly(True)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 180, 411, 16))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MiWiFi_PW_Generater", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SN\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Result\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"For More Info, Pls Go to https://github.com/CCA2878/MiWiFipwGUI", None))
    # retranslateUi

