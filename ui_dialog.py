# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogxRUFVV.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(253, 186)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"border: 3px solid white;\n"
"border-color: rgba(255, 255, 255, 0);\n"
"border-right-color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignLeft)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Group 1", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p>+ ADJOVI Alb\u00e9ric</p><p>+ A\u00cfZANNON Merveille</p><p>+ BONOU Habib</p><p>+ KIKI Esther</p><p>+ MONTCHO Marcolin</p><p align=\"justify\">+ ZINSOU Karl</p></body></html>", None))
    # retranslateUi

