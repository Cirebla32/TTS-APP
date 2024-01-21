# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ttsfVAnyS.ui'
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
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpinBox,
    QTextEdit, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(643, 168)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:0.228823, y1:0.506, x2:0.446, y2:0.602227, stop:0 rgba(104, 8, 100, 255), stop:1 rgba(249, 158, 251, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.centralContainer = QWidget(self.centralwidget)
        self.centralContainer.setObjectName(u"centralContainer")
        self.centralContainer.setMaximumSize(QSize(16777215, 150))
        self.centralContainer.setStyleSheet(u"background-color: rgba(0, 0, 0, 100);")
        self.verticalLayout = QVBoxLayout(self.centralContainer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralContainer)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Latin Modern Mono Caps"])
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignTop)

        self.widget = QWidget(self.centralContainer)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.openGLWidget = QOpenGLWidget(self.widget)
        self.openGLWidget.setObjectName(u"openGLWidget")

        self.horizontalLayout_2.addWidget(self.openGLWidget)

        self.ttsChoice = QSpinBox(self.widget)
        self.ttsChoice.setObjectName(u"ttsChoice")
        self.ttsChoice.setMinimum(1)
        self.ttsChoice.setMaximum(4)

        self.horizontalLayout_2.addWidget(self.ttsChoice)

        self.languageChoice = QSpinBox(self.widget)
        self.languageChoice.setObjectName(u"languageChoice")
        self.languageChoice.setMinimum(1)
        self.languageChoice.setMaximum(5)
        self.languageChoice.setSingleStep(1)
        self.languageChoice.setStepType(QAbstractSpinBox.DefaultStepType)

        self.horizontalLayout_2.addWidget(self.languageChoice)

        self.voiceChoice = QSpinBox(self.widget)
        self.voiceChoice.setObjectName(u"voiceChoice")
        self.voiceChoice.setMinimum(1)
        self.voiceChoice.setMaximum(3)

        self.horizontalLayout_2.addWidget(self.voiceChoice)

        self.userInput = QTextEdit(self.widget)
        self.userInput.setObjectName(u"userInput")
        self.userInput.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);")

        self.horizontalLayout_2.addWidget(self.userInput)

        self.playBtn = QPushButton(self.widget)
        self.playBtn.setObjectName(u"playBtn")
        self.playBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/Bold/play.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.playBtn.setIcon(icon)
        self.playBtn.setIconSize(QSize(32, 24))

        self.horizontalLayout_2.addWidget(self.playBtn)


        self.verticalLayout.addWidget(self.widget)

        self.voiceViewer = PlotWidget(self.centralContainer)
        self.voiceViewer.setObjectName(u"voiceViewer")
        self.voiceViewer.setMaximumSize(QSize(16777215, 145))

        self.verticalLayout.addWidget(self.voiceViewer)


        self.horizontalLayout.addWidget(self.centralContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Text to Speech App", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Input", None))
#if QT_CONFIG(tooltip)
        self.ttsChoice.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">TTS 1:</span><span style=\" font-size:10pt; color:#ffffff;\"> Pico2Wave [Linux command]</span></p><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">TTS 2:</span><span style=\" font-size:10pt; color:#ffffff;\"> Espeak [Linux command]</span></p><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">TTS 3:</span><span style=\" font-size:10pt; color:#ffffff;\"> Pyttsx [Python Package]</span></p><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">TTS 4:</span><span style=\" font-size:10pt; color:#ffffff;\"> Gtts [Google tts online | Python package]</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ttsChoice.setPrefix(QCoreApplication.translate("MainWindow", u"TTS ", None))
#if QT_CONFIG(tooltip)
        self.languageChoice.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Language 1:</span><span style=\" font-size:10pt; color:#ffffff;\"> fr-FR</span></p><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Language 2:</span><span style=\" font-size:10pt; color:#ffffff;\"> en-EN</span></p><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Language 3:</span><span style=\" font-size:10pt; color:#ffffff;\"> es-ES</span></p><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Language 4:</span><span style=\" font-size:10pt; color:#ffffff;\"> Al-AL</span></p><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Language 5:</span><span style=\" font-size:10pt; color:#ffffff;\"> lt-LT</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.languageChoice.setSuffix("")
        self.languageChoice.setPrefix(QCoreApplication.translate("MainWindow", u"Language ", None))
#if QT_CONFIG(tooltip)
        self.voiceChoice.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Voice 1:</span><span style=\" font-size:10pt; color:#ffffff;\"> Female</span></p><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Voice 2:</span><span style=\" font-size:10pt; color:#ffffff;\"> Male</span></p><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Voice 3:</span><span style=\" font-size:10pt; color:#ffffff;\"> Robot</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.voiceChoice.setPrefix(QCoreApplication.translate("MainWindow", u"Voice ", None))
#if QT_CONFIG(tooltip)
        self.userInput.setToolTip(QCoreApplication.translate("MainWindow", u"Your Text", None))
#endif // QT_CONFIG(tooltip)
        self.userInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your Input", None))
#if QT_CONFIG(tooltip)
        self.playBtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Play</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.playBtn.setText("")
#if QT_CONFIG(tooltip)
        self.voiceViewer.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Visualizer</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

