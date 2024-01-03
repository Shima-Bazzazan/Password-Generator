# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenuBar,
    QPlainTextEdit, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(487, 367)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 209, 179);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Dosis ExtraBold"])
        font.setPointSize(20)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"color: rgb(50, 50, 50);\n"
"border-radius: 15px\n"
"")

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 2)

        self.btn_generate = QPushButton(self.centralwidget)
        self.btn_generate.setObjectName(u"btn_generate")
        sizePolicy1.setHeightForWidth(self.btn_generate.sizePolicy().hasHeightForWidth())
        self.btn_generate.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Dosis ExtraBold"])
        font1.setPointSize(15)
        font1.setBold(True)
        self.btn_generate.setFont(font1)
        self.btn_generate.setStyleSheet(u"border-radius: 20px ;\n"
"color: rgb(255, 147, 75);\n"
"background-color: rgb(50, 50, 50);")

        self.gridLayout.addWidget(self.btn_generate, 6, 1, 1, 1)

        self.rb_super = QRadioButton(self.centralwidget)
        self.rb_super.setObjectName(u"rb_super")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.rb_super.sizePolicy().hasHeightForWidth())
        self.rb_super.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"Dosis ExtraBold"])
        font2.setPointSize(13)
        self.rb_super.setFont(font2)
        self.rb_super.setStyleSheet(u"color: rgb(50, 50, 50);\n"
"border-radius: 15px\n"
"")

        self.gridLayout.addWidget(self.rb_super, 7, 0, 1, 1)

        self.btn_result = QPlainTextEdit(self.centralwidget)
        self.btn_result.setObjectName(u"btn_result")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Ignored)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_result.sizePolicy().hasHeightForWidth())
        self.btn_result.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setFamilies([u"Dosis ExtraBold"])
        font3.setPointSize(15)
        self.btn_result.setFont(font3)
        self.btn_result.setStyleSheet(u"border-radius: 20px ;\n"
"color: rgb(255, 147, 75);\n"
"background-color: rgb(50, 50, 50);")

        self.gridLayout.addWidget(self.btn_result, 4, 1, 1, 1)

        self.rb_standard = QRadioButton(self.centralwidget)
        self.rb_standard.setObjectName(u"rb_standard")
        sizePolicy2.setHeightForWidth(self.rb_standard.sizePolicy().hasHeightForWidth())
        self.rb_standard.setSizePolicy(sizePolicy2)
        self.rb_standard.setFont(font2)
        self.rb_standard.setStyleSheet(u"color: rgb(50, 50, 50);\n"
"border-radius: 15px\n"
"")

        self.gridLayout.addWidget(self.rb_standard, 5, 0, 1, 1)

        self.rb_extra = QRadioButton(self.centralwidget)
        self.rb_extra.setObjectName(u"rb_extra")
        sizePolicy2.setHeightForWidth(self.rb_extra.sizePolicy().hasHeightForWidth())
        self.rb_extra.setSizePolicy(sizePolicy2)
        self.rb_extra.setFont(font2)
        self.rb_extra.setStyleSheet(u"color: rgb(50, 50, 50);\n"
"border-radius: 15px\n"
"")

        self.gridLayout.addWidget(self.rb_extra, 6, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy4)
        self.pushButton_3.setStyleSheet(u"border-radius: 10px;")

        self.gridLayout.addWidget(self.pushButton_3, 3, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.passwordgenerator = QMenuBar(MainWindow)
        self.passwordgenerator.setObjectName(u"passwordgenerator")
        self.passwordgenerator.setGeometry(QRect(0, 0, 487, 22))
        MainWindow.setMenuBar(self.passwordgenerator)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password-Generator", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Random Password Generator", None))
        self.btn_generate.setText(QCoreApplication.translate("MainWindow", u"\u200c\u200c\n"
"Generate\n"
"\u200c", None))
        self.rb_super.setText(QCoreApplication.translate("MainWindow", u"Super Strong", None))
        self.btn_result.setPlainText("")
        self.rb_standard.setText(QCoreApplication.translate("MainWindow", u"Standard", None))
        self.rb_extra.setText(QCoreApplication.translate("MainWindow", u"Extra Strong", None))
        self.pushButton_3.setText("")
    # retranslateUi

