# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ttsfEsDhO.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTextBrowser, QTextEdit, QVBoxLayout,
    QWidget)

from pyqtgraph import PlotWidget
import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(643, 534)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:0.228823, y1:0.506, x2:0.446, y2:0.602227, stop:0 rgba(104, 8, 100, 255), stop:1 rgba(249, 158, 251, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ttsContainer = QWidget(self.centralwidget)
        self.ttsContainer.setObjectName(u"ttsContainer")
        self.ttsContainer.setMaximumSize(QSize(16777215, 150))
        self.ttsContainer.setStyleSheet(u"background-color: rgba(0, 0, 0, 100);")
        self.verticalLayout = QVBoxLayout(self.ttsContainer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.ttsContainer)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Latin Modern Mono Caps"])
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignTop)

        self.widget = QWidget(self.ttsContainer)
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

        self.languageChoiceTTS = QSpinBox(self.widget)
        self.languageChoiceTTS.setObjectName(u"languageChoiceTTS")
        self.languageChoiceTTS.setMinimum(1)
        self.languageChoiceTTS.setMaximum(6)
        self.languageChoiceTTS.setSingleStep(1)
        self.languageChoiceTTS.setStepType(QAbstractSpinBox.DefaultStepType)

        self.horizontalLayout_2.addWidget(self.languageChoiceTTS)

        self.voiceChoice = QSpinBox(self.widget)
        self.voiceChoice.setObjectName(u"voiceChoice")
        self.voiceChoice.setMinimum(1)
        self.voiceChoice.setMaximum(3)

        self.horizontalLayout_2.addWidget(self.voiceChoice)

        self.userInput = QTextEdit(self.widget)
        self.userInput.setObjectName(u"userInput")
        self.userInput.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);")

        self.horizontalLayout_2.addWidget(self.userInput)

        self.playTTSbtn = QPushButton(self.widget)
        self.playTTSbtn.setObjectName(u"playTTSbtn")
        self.playTTSbtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/Bold/play.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.playTTSbtn.setIcon(icon)
        self.playTTSbtn.setIconSize(QSize(32, 24))

        self.horizontalLayout_2.addWidget(self.playTTSbtn)


        self.verticalLayout.addWidget(self.widget)

        self.voiceViewer = PlotWidget(self.ttsContainer)
        self.voiceViewer.setObjectName(u"voiceViewer")
        self.voiceViewer.setMaximumSize(QSize(16777215, 145))

        self.verticalLayout.addWidget(self.voiceViewer)


        self.verticalLayout_2.addWidget(self.ttsContainer)

        self.sttContainer = QWidget(self.centralwidget)
        self.sttContainer.setObjectName(u"sttContainer")
        self.sttContainer.setStyleSheet(u"background-color: rgba(0, 0, 0, 100);")
        self.verticalLayout_3 = QVBoxLayout(self.sttContainer)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.sttContainer)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_3.addWidget(self.label_3)

        self.widget_3 = QWidget(self.sttContainer)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.sttChoice = QSpinBox(self.widget_3)
        self.sttChoice.setObjectName(u"sttChoice")
        self.sttChoice.setMinimum(1)
        self.sttChoice.setMaximum(1)

        self.horizontalLayout_3.addWidget(self.sttChoice)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.languageChoiceSTT = QSpinBox(self.widget_3)
        self.languageChoiceSTT.setObjectName(u"languageChoiceSTT")
        self.languageChoiceSTT.setMinimum(1)
        self.languageChoiceSTT.setMaximum(5)
        self.languageChoiceSTT.setSingleStep(1)
        self.languageChoiceSTT.setStepType(QAbstractSpinBox.DefaultStepType)

        self.horizontalLayout_3.addWidget(self.languageChoiceSTT)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.recSTTbtn = QPushButton(self.widget_3)
        self.recSTTbtn.setObjectName(u"recSTTbtn")
        self.recSTTbtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/Bold/mic.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.recSTTbtn.setIcon(icon1)
        self.recSTTbtn.setIconSize(QSize(32, 24))

        self.horizontalLayout_3.addWidget(self.recSTTbtn)

        self.stopRecSTTbtn = QPushButton(self.widget_3)
        self.stopRecSTTbtn.setObjectName(u"stopRecSTTbtn")
        self.stopRecSTTbtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/Bold/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.stopRecSTTbtn.setIcon(icon2)
        self.stopRecSTTbtn.setIconSize(QSize(32, 24))

        self.horizontalLayout_3.addWidget(self.stopRecSTTbtn)


        self.verticalLayout_3.addWidget(self.widget_3)

        self.sttTextBrowser = QTextBrowser(self.sttContainer)
        self.sttTextBrowser.setObjectName(u"sttTextBrowser")
        self.sttTextBrowser.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);")

        self.verticalLayout_3.addWidget(self.sttTextBrowser)


        self.verticalLayout_2.addWidget(self.sttContainer)

        self.stsContainer = QWidget(self.centralwidget)
        self.stsContainer.setObjectName(u"stsContainer")
        self.stsContainer.setStyleSheet(u"background-color: rgba(0, 0, 0, 100);")
        self.verticalLayout_4 = QVBoxLayout(self.stsContainer)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.stsContainer)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.verticalLayout_4.addWidget(self.label_5)

        self.widget_4 = QWidget(self.stsContainer)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.widget_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.stsChoice = QSpinBox(self.widget_4)
        self.stsChoice.setObjectName(u"stsChoice")
        self.stsChoice.setMinimum(1)
        self.stsChoice.setMaximum(4)

        self.horizontalLayout_4.addWidget(self.stsChoice)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.language1ChoiceSTS = QSpinBox(self.widget_4)
        self.language1ChoiceSTS.setObjectName(u"language1ChoiceSTS")
        self.language1ChoiceSTS.setMinimum(1)
        self.language1ChoiceSTS.setMaximum(5)
        self.language1ChoiceSTS.setSingleStep(1)
        self.language1ChoiceSTS.setStepType(QAbstractSpinBox.DefaultStepType)

        self.horizontalLayout_4.addWidget(self.language1ChoiceSTS)

        self.label_7 = QLabel(self.widget_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout_4.addWidget(self.label_7, 0, Qt.AlignHCenter)

        self.language2ChoiceSTS = QSpinBox(self.widget_4)
        self.language2ChoiceSTS.setObjectName(u"language2ChoiceSTS")
        self.language2ChoiceSTS.setMinimum(1)
        self.language2ChoiceSTS.setMaximum(6)

        self.horizontalLayout_4.addWidget(self.language2ChoiceSTS)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.recSTSbtn = QPushButton(self.widget_4)
        self.recSTSbtn.setObjectName(u"recSTSbtn")
        self.recSTSbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.recSTSbtn.setIcon(icon1)
        self.recSTSbtn.setIconSize(QSize(32, 24))

        self.horizontalLayout_4.addWidget(self.recSTSbtn)

        self.stopRecSTSbtn = QPushButton(self.widget_4)
        self.stopRecSTSbtn.setObjectName(u"stopRecSTSbtn")
        self.stopRecSTSbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.stopRecSTSbtn.setIcon(icon2)
        self.stopRecSTSbtn.setIconSize(QSize(32, 24))

        self.horizontalLayout_4.addWidget(self.stopRecSTSbtn)

        self.playSTSbtn = QPushButton(self.widget_4)
        self.playSTSbtn.setObjectName(u"playSTSbtn")
        self.playSTSbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.playSTSbtn.setIcon(icon)
        self.playSTSbtn.setIconSize(QSize(32, 24))

        self.horizontalLayout_4.addWidget(self.playSTSbtn)


        self.verticalLayout_4.addWidget(self.widget_4)

        self.widget_2 = QWidget(self.stsContainer)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stsText1Browser = QTextBrowser(self.widget_2)
        self.stsText1Browser.setObjectName(u"stsText1Browser")
        self.stsText1Browser.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);")

        self.horizontalLayout.addWidget(self.stsText1Browser)

        self.stsText2Browser = QTextBrowser(self.widget_2)
        self.stsText2Browser.setObjectName(u"stsText2Browser")
        font2 = QFont()
        font2.setBold(False)
        self.stsText2Browser.setFont(font2)
        self.stsText2Browser.setStyleSheet(u"background-color: rgba(255, 255, 255, 100);")

        self.horizontalLayout.addWidget(self.stsText2Browser)


        self.verticalLayout_4.addWidget(self.widget_2)


        self.verticalLayout_2.addWidget(self.stsContainer)

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
        self.languageChoiceTTS.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Language 1: </span><span style=\" font-size:10pt; color:#ffffff;\">fr-FR</span></p><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Language 2:</span><span style=\" font-size:10pt; color:#ffffff;\"> en-US</span></p><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Language 3:</span><span style=\" font-size:10pt; color:#ffffff;\"> en-GB</span></p><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Language 4:</span><span style=\" font-size:10pt; color:#ffffff;\"> de-DE</span></p><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Language 5:</span><span style=\" font-size:10pt; color:#ffffff;\"> es-ES</span></p><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Language 6:</span><span style=\" font-size:10pt; color:#ffffff;\"> it-IT</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.languageChoiceTTS.setSuffix("")
        self.languageChoiceTTS.setPrefix(QCoreApplication.translate("MainWindow", u"Language ", None))
#if QT_CONFIG(tooltip)
        self.voiceChoice.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Voice 1:</span><span style=\" font-size:10pt; color:#ffffff;\"> Female</span></p><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Voice 2:</span><span style=\" font-size:10pt; color:#ffffff;\"> Male</span></p><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Voice 3:</span><span style=\" font-size:10pt; color:#ffffff;\"> Robot</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.voiceChoice.setPrefix(QCoreApplication.translate("MainWindow", u"Voice ", None))
#if QT_CONFIG(tooltip)
        self.userInput.setToolTip(QCoreApplication.translate("MainWindow", u"Your Text", None))
#endif // QT_CONFIG(tooltip)
        self.userInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your Input", None))
#if QT_CONFIG(tooltip)
        self.playTTSbtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Play</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.playTTSbtn.setText("")
#if QT_CONFIG(tooltip)
        self.voiceViewer.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Visualizer</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Speech to Text App", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Input", None))
#if QT_CONFIG(tooltip)
        self.sttChoice.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">STT 1:</span><span style=\" font-size:10pt; color:#ffffff;\"> speech_recognition [Python Package | online]</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.sttChoice.setPrefix(QCoreApplication.translate("MainWindow", u"STT ", None))
#if QT_CONFIG(tooltip)
        self.languageChoiceSTT.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Language 1: </span><span style=\" font-size:10pt; color:#ffffff;\">fr-FR</span></p><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Language 2:</span><span style=\" font-size:10pt; color:#ffffff;\"> en-US</span></p><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Language 3:</span><span style=\" font-size:10pt; color:#ffffff;\"> en-GB</span></p><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Language 4:</span><span style=\" font-size:10pt; color:#ffffff;\"> de-DE</span></p><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Language 5:</span><span style=\" font-size:10pt; color:#ffffff;\"> es-ES</span></p><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Language 6:</span><span style=\" font-size:10pt; color:#ffffff;\"> it-IT</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.languageChoiceSTT.setSuffix("")
        self.languageChoiceSTT.setPrefix(QCoreApplication.translate("MainWindow", u"Language ", None))
#if QT_CONFIG(tooltip)
        self.recSTTbtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Record</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.recSTTbtn.setText("")
#if QT_CONFIG(tooltip)
        self.stopRecSTTbtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Stop recording, and Transcript</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.stopRecSTTbtn.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Speech to Speech App", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Input", None))
#if QT_CONFIG(tooltip)
        self.stsChoice.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">STS 1:</span><span style=\" font-size:10pt; color:#ffffff;\"> Coming Soon</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.stsChoice.setPrefix(QCoreApplication.translate("MainWindow", u"STS ", None))
#if QT_CONFIG(tooltip)
        self.language1ChoiceSTS.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Language 1: </span><span style=\" font-size:10pt; color:#ffffff;\">fr-FR</span></p><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Language 2:</span><span style=\" font-size:10pt; color:#ffffff;\"> en-US</span></p><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Language 3:</span><span style=\" font-size:10pt; color:#ffffff;\"> en-GB</span></p><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Language 4:</span><span style=\" font-size:10pt; color:#ffffff;\"> de-DE</span></p><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Language 5:</span><span style=\" font-size:10pt; color:#ffffff;\"> es-ES</span></p><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Language 6:</span><span style=\" font-size:10pt; color:#ffffff;\"> it-IT</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.language1ChoiceSTS.setSuffix("")
        self.language1ChoiceSTS.setPrefix(QCoreApplication.translate("MainWindow", u"Language ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.language2ChoiceSTS.setPrefix(QCoreApplication.translate("MainWindow", u"Language ", None))
#if QT_CONFIG(tooltip)
        self.recSTSbtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Record</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.recSTSbtn.setText("")
#if QT_CONFIG(tooltip)
        self.stopRecSTSbtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Stop Recording</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.stopRecSTSbtn.setText("")
#if QT_CONFIG(tooltip)
        self.playSTSbtn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Play</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.playSTSbtn.setText("")
        self.stsText1Browser.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Coming Soon", None))
        self.stsText2Browser.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Coming Soon", None))
    # retranslateUi

