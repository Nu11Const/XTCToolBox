# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QCommandLinkButton,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QStatusBar, QWidget)
import main_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(859, 548)
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/img/img/watch.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionsh = QAction(MainWindow)
        self.actionsh.setObjectName(u"actionsh")
        icon1 = QIcon()
        icon1.addFile(u":/img/img/screenshot.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionsh.setIcon(icon1)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        icon2 = QIcon()
        icon2.addFile(u":/img/img/update.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action.setIcon(icon2)
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        icon3 = QIcon()
        icon3.addFile(u":/img/img/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_2.setIcon(icon3)
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        icon4 = QIcon()
        icon4.addFile(u":/img/img/about.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_3.setIcon(icon4)
        self.action_5 = QAction(MainWindow)
        self.action_5.setObjectName(u"action_5")
        self.action_7 = QAction(MainWindow)
        self.action_7.setObjectName(u"action_7")
        icon5 = QIcon()
        icon5.addFile(u":/img/img/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_7.setIcon(icon5)
        self.actionADB = QAction(MainWindow)
        self.actionADB.setObjectName(u"actionADB")
        icon6 = QIcon()
        icon6.addFile(u":/img/img/command.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionADB.setIcon(icon6)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_20 = QPushButton(self.centralwidget)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.gridLayout.addWidget(self.pushButton_20, 1, 4, 1, 1)

        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout.addWidget(self.pushButton_8, 1, 1, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidgetPage1 = QWidget()
        self.stackedWidgetPage1.setObjectName(u"stackedWidgetPage1")
        self.gridLayout_2 = QGridLayout(self.stackedWidgetPage1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_5 = QPushButton(self.stackedWidgetPage1)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_2.addWidget(self.pushButton_5, 1, 2, 1, 1)

        self.pushButton_6 = QPushButton(self.stackedWidgetPage1)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_2.addWidget(self.pushButton_6, 1, 3, 1, 1)

        self.pushButton_4 = QPushButton(self.stackedWidgetPage1)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_2.addWidget(self.pushButton_4, 1, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.stackedWidgetPage1)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_2.addWidget(self.pushButton_3, 1, 0, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.stackedWidgetPage1)
        self.commandLinkButton.setObjectName(u"commandLinkButton")

        self.gridLayout_2.addWidget(self.commandLinkButton, 2, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.stackedWidgetPage1)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.gridLayout_2.addWidget(self.pushButton_13, 1, 4, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.stackedWidgetPage1)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"MiSans"])
        font1.setPointSize(35)
        self.label.setFont(font1)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_4 = QLabel(self.stackedWidgetPage1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"image: url(:/img/img/watch.png);")

        self.horizontalLayout.addWidget(self.label_4)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 5)

        self.plainTextEdit = QPlainTextEdit(self.stackedWidgetPage1)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(15)
        self.plainTextEdit.setFont(font2)
        self.plainTextEdit.setTabChangesFocus(False)
        self.plainTextEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.plainTextEdit, 3, 0, 1, 5)

        self.stackedWidget.addWidget(self.stackedWidgetPage1)
        self.stackedWidgetPage2 = QWidget()
        self.stackedWidgetPage2.setObjectName(u"stackedWidgetPage2")
        self.gridLayout_3 = QGridLayout(self.stackedWidgetPage2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_11 = QPushButton(self.stackedWidgetPage2)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout_3.addWidget(self.pushButton_11, 3, 3, 1, 2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 3, 1, 1, 1)

        self.pushButton = QPushButton(self.stackedWidgetPage2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_3.addWidget(self.pushButton, 1, 4, 1, 1)

        self.label_5 = QLabel(self.stackedWidgetPage2)
        self.label_5.setObjectName(u"label_5")
        font3 = QFont()
        font3.setFamilies([u"Microsoft YaHei UI"])
        font3.setPointSize(15)
        self.label_5.setFont(font3)

        self.gridLayout_3.addWidget(self.label_5, 4, 0, 1, 1)

        self.comboBox = QComboBox(self.stackedWidgetPage2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_3.addWidget(self.comboBox, 1, 3, 1, 1)

        self.pushButton_2 = QPushButton(self.stackedWidgetPage2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_3.addWidget(self.pushButton_2, 1, 2, 1, 1)

        self.lineEdit = QLineEdit(self.stackedWidgetPage2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_3.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 6, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.stackedWidgetPage2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_3.addWidget(self.lineEdit_2, 3, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.stackedWidgetPage2)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout_3.addWidget(self.pushButton_10, 3, 2, 1, 1)

        self.label_3 = QLabel(self.stackedWidgetPage2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)

        self.label_2 = QLabel(self.stackedWidgetPage2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.stackedWidgetPage2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_3.addWidget(self.lineEdit_3, 5, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.stackedWidgetPage2)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.gridLayout_3.addWidget(self.pushButton_12, 5, 2, 1, 3)

        self.stackedWidget.addWidget(self.stackedWidgetPage2)
        self.stackedWidgetPage3 = QWidget()
        self.stackedWidgetPage3.setObjectName(u"stackedWidgetPage3")
        self.gridLayout_4 = QGridLayout(self.stackedWidgetPage3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 1, 2, 1, 1)

        self.spinBox_3 = QSpinBox(self.stackedWidgetPage3)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMaximum(1000)

        self.gridLayout_4.addWidget(self.spinBox_3, 2, 1, 1, 1)

        self.pushButton_16 = QPushButton(self.stackedWidgetPage3)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.gridLayout_4.addWidget(self.pushButton_16, 1, 4, 1, 1)

        self.pushButton_17 = QPushButton(self.stackedWidgetPage3)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.gridLayout_4.addWidget(self.pushButton_17, 2, 4, 1, 1)

        self.label_6 = QLabel(self.stackedWidgetPage3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)

        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)

        self.pushButton_14 = QPushButton(self.stackedWidgetPage3)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.gridLayout_4.addWidget(self.pushButton_14, 1, 3, 1, 1)

        self.label_7 = QLabel(self.stackedWidgetPage3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.gridLayout_4.addWidget(self.label_7, 2, 0, 1, 1)

        self.spinBox_2 = QSpinBox(self.stackedWidgetPage3)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximum(10000)

        self.gridLayout_4.addWidget(self.spinBox_2, 1, 1, 1, 1)

        self.pushButton_15 = QPushButton(self.stackedWidgetPage3)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.gridLayout_4.addWidget(self.pushButton_15, 2, 3, 1, 1)

        self.spinBox = QSpinBox(self.stackedWidgetPage3)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(10000)

        self.gridLayout_4.addWidget(self.spinBox, 1, 0, 1, 1)

        self.plainTextEdit_2 = QPlainTextEdit(self.stackedWidgetPage3)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        font4 = QFont()
        font4.setFamilies([u"Microsoft YaHei UI"])
        font4.setPointSize(12)
        self.plainTextEdit_2.setFont(font4)
        self.plainTextEdit_2.setReadOnly(True)

        self.gridLayout_4.addWidget(self.plainTextEdit_2, 3, 0, 1, 5)

        self.stackedWidget.addWidget(self.stackedWidgetPage3)
        self.stackedWidgetPage4 = QWidget()
        self.stackedWidgetPage4.setObjectName(u"stackedWidgetPage4")
        self.gridLayout_5 = QGridLayout(self.stackedWidgetPage4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_19 = QPushButton(self.stackedWidgetPage4)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.gridLayout_5.addWidget(self.pushButton_19, 2, 2, 1, 1)

        self.checkBox_2 = QCheckBox(self.stackedWidgetPage4)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_5.addWidget(self.checkBox_2, 3, 2, 1, 1)

        self.label_12 = QLabel(self.stackedWidgetPage4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)

        self.gridLayout_5.addWidget(self.label_12, 5, 0, 1, 1)

        self.label_11 = QLabel(self.stackedWidgetPage4)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 4, 0, 1, 6)

        self.checkBox_3 = QCheckBox(self.stackedWidgetPage4)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_5.addWidget(self.checkBox_3, 3, 4, 1, 1)

        self.spinBox_4 = QSpinBox(self.stackedWidgetPage4)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setMaximum(1000)

        self.gridLayout_5.addWidget(self.spinBox_4, 2, 0, 1, 1)

        self.pushButton_21 = QPushButton(self.stackedWidgetPage4)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.gridLayout_5.addWidget(self.pushButton_21, 1, 1, 1, 2)

        self.label_9 = QLabel(self.stackedWidgetPage4)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_5.addWidget(self.label_9, 2, 1, 1, 1)

        self.label_8 = QLabel(self.stackedWidgetPage4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)

        self.gridLayout_5.addWidget(self.label_8, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 7, 0, 1, 1)

        self.checkBox = QCheckBox(self.stackedWidgetPage4)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_5.addWidget(self.checkBox, 3, 0, 1, 1)

        self.plainTextEdit_3 = QPlainTextEdit(self.stackedWidgetPage4)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setFont(font4)
        self.plainTextEdit_3.setReadOnly(True)

        self.gridLayout_5.addWidget(self.plainTextEdit_3, 6, 0, 1, 6)

        self.checkBox_4 = QCheckBox(self.stackedWidgetPage4)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout_5.addWidget(self.checkBox_4, 3, 5, 1, 1)

        self.stackedWidget.addWidget(self.stackedWidgetPage4)
        self.stackedWidgetPage5 = QWidget()
        self.stackedWidgetPage5.setObjectName(u"stackedWidgetPage5")
        self.gridLayout_6 = QGridLayout(self.stackedWidgetPage5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_10 = QLabel(self.stackedWidgetPage5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.gridLayout_6.addWidget(self.label_10, 0, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.stackedWidgetPage5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_6.addWidget(self.lineEdit_4, 1, 1, 1, 1)

        self.pushButton_22 = QPushButton(self.stackedWidgetPage5)
        self.pushButton_22.setObjectName(u"pushButton_22")

        self.gridLayout_6.addWidget(self.pushButton_22, 1, 2, 1, 1)

        self.label_13 = QLabel(self.stackedWidgetPage5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)

        self.gridLayout_6.addWidget(self.label_13, 2, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_4, 4, 1, 1, 1)

        self.pushButton_23 = QPushButton(self.stackedWidgetPage5)
        self.pushButton_23.setObjectName(u"pushButton_23")

        self.gridLayout_6.addWidget(self.pushButton_23, 3, 2, 1, 1)

        self.lineEdit_5 = QLineEdit(self.stackedWidgetPage5)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_6.addWidget(self.lineEdit_5, 3, 1, 1, 1)

        self.stackedWidget.addWidget(self.stackedWidgetPage5)
        self.stackedWidgetPage6 = QWidget()
        self.stackedWidgetPage6.setObjectName(u"stackedWidgetPage6")
        self.gridLayout_7 = QGridLayout(self.stackedWidgetPage6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_5, 3, 0, 1, 1)

        self.spinBox_5 = QSpinBox(self.stackedWidgetPage6)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setMaximum(999999999)

        self.gridLayout_7.addWidget(self.spinBox_5, 1, 0, 1, 1)

        self.label_15 = QLabel(self.stackedWidgetPage6)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_7.addWidget(self.label_15, 1, 2, 1, 1)

        self.label_14 = QLabel(self.stackedWidgetPage6)
        self.label_14.setObjectName(u"label_14")
        font5 = QFont()
        font5.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font5.setPointSize(20)
        self.label_14.setFont(font5)

        self.gridLayout_7.addWidget(self.label_14, 0, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_6, 1, 1, 1, 1)

        self.commandLinkButton_2 = QCommandLinkButton(self.stackedWidgetPage6)
        self.commandLinkButton_2.setObjectName(u"commandLinkButton_2")

        self.gridLayout_7.addWidget(self.commandLinkButton_2, 2, 0, 1, 3)

        self.stackedWidget.addWidget(self.stackedWidgetPage6)
        self.stackedWidgetPage7 = QWidget()
        self.stackedWidgetPage7.setObjectName(u"stackedWidgetPage7")
        self.gridLayout_8 = QGridLayout(self.stackedWidgetPage7)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_17 = QLabel(self.stackedWidgetPage7)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)

        self.gridLayout_8.addWidget(self.label_17, 1, 0, 1, 1)

        self.label_16 = QLabel(self.stackedWidgetPage7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font5)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.label_16, 0, 0, 1, 4)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_6, 6, 0, 1, 1)

        self.pushButton_26 = QPushButton(self.stackedWidgetPage7)
        self.pushButton_26.setObjectName(u"pushButton_26")

        self.gridLayout_8.addWidget(self.pushButton_26, 5, 0, 1, 1)

        self.pushButton_28 = QPushButton(self.stackedWidgetPage7)
        self.pushButton_28.setObjectName(u"pushButton_28")

        self.gridLayout_8.addWidget(self.pushButton_28, 5, 3, 1, 1)

        self.pushButton_27 = QPushButton(self.stackedWidgetPage7)
        self.pushButton_27.setObjectName(u"pushButton_27")

        self.gridLayout_8.addWidget(self.pushButton_27, 5, 2, 1, 1)

        self.pushButton_29 = QPushButton(self.stackedWidgetPage7)
        self.pushButton_29.setObjectName(u"pushButton_29")

        self.gridLayout_8.addWidget(self.pushButton_29, 5, 1, 1, 1)

        self.label_18 = QLabel(self.stackedWidgetPage7)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font2)

        self.gridLayout_8.addWidget(self.label_18, 3, 0, 1, 1)

        self.pushButton_30 = QPushButton(self.stackedWidgetPage7)
        self.pushButton_30.setObjectName(u"pushButton_30")

        self.gridLayout_8.addWidget(self.pushButton_30, 2, 3, 1, 1)

        self.lineEdit_6 = QLineEdit(self.stackedWidgetPage7)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_8.addWidget(self.lineEdit_6, 2, 0, 1, 3)

        self.stackedWidget.addWidget(self.stackedWidgetPage7)
        self.stackedWidgetPage8 = QWidget()
        self.stackedWidgetPage8.setObjectName(u"stackedWidgetPage8")
        self.stackedWidget.addWidget(self.stackedWidgetPage8)

        self.gridLayout.addWidget(self.stackedWidget, 4, 0, 1, 9)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 7, 1, 1)

        self.pushButton_24 = QPushButton(self.centralwidget)
        self.pushButton_24.setObjectName(u"pushButton_24")

        self.gridLayout.addWidget(self.pushButton_24, 1, 5, 1, 1)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout.addWidget(self.pushButton_7, 1, 0, 1, 1)

        self.pushButton_18 = QPushButton(self.centralwidget)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.gridLayout.addWidget(self.pushButton_18, 1, 3, 1, 1)

        self.pushButton_9 = QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout.addWidget(self.pushButton_9, 1, 2, 1, 1)

        self.pushButton_25 = QPushButton(self.centralwidget)
        self.pushButton_25.setObjectName(u"pushButton_25")

        self.gridLayout.addWidget(self.pushButton_25, 1, 6, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 859, 25))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.actionsh)
        self.menu.addAction(self.actionADB)
        self.menu.addSeparator()
        self.menu.addAction(self.action_7)
        self.menu_2.addAction(self.action)
        self.menu_2.addAction(self.action_2)
        self.menu_2.addAction(self.action_3)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_5)

        self.retranslateUi(MainWindow)
        self.action_7.triggered.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"XTCToolBox Version 3.0", None))
        self.actionsh.setText(QCoreApplication.translate("MainWindow", u"\u622a\u5c4f", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u65b0", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.action_5.setText(QCoreApplication.translate("MainWindow", u"\u4f5c\u8005\u5b98\u7f51", None))
        self.action_7.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.actionADB.setText(QCoreApplication.translate("MainWindow", u"ADB\u7ec8\u7aef", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5\u65e0\u7ebf", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u8f6f\u4ef6\u7ba1\u7406", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u542f\u5230Bootloader", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u" \u91cd\u542f\u5230download(edl)\u6a21\u5f0f", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u542f\u5230Fastboot", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u6807\u51c6\u91cd\u542f", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u" \u5237\u65b0\u8fde\u63a5\u72b6\u6001", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"\u5173\u673a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"XTCToolBox", None))
        self.label_4.setText("")
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"\u672a\u8fde\u63a5\u8bbe\u5907", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u4f20\u8f93", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8\u5b89\u88c5", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u6587\u4ef6", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u666e\u901a", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u8986\u76d6", None))

        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165apk\u6587\u4ef6\u8def\u5f84", None))
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u8def\u5f84", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4f20\u6587\u4ef6", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5b89\u88c5APK", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u4f4d\u7f6e", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u5c4f\u5e55\u5206\u8fa8\u7387", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"DPI", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.plainTextEdit_2.setPlainText(QCoreApplication.translate("MainWindow", u"\u5f53\u524dDPI\u60c5\u51b5:\n"
"\n"
"\u5f53\u524d\u5206\u8fa8\u7387\u72b6\u6001:", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u62df\u65e0\u7ebf\u5145", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u7535\u6c60\u4fe1\u606f", None))
        self.label_11.setText("")
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u62dfUSB\u5145", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u7535\u6c60\u7535\u91cf", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u7535\u6c60\u6a21\u62df", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u62df\u672a\u5145\u7535", None))
        self.plainTextEdit_3.setPlainText(QCoreApplication.translate("MainWindow", u"ces", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u62df\u76f4\u6d41\u5145", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"IP\u8fde\u63a5", None))
        self.lineEdit_4.setInputMask("")
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u6709\u7ebf\u8f6c\u65e0\u7ebf", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5", None))
        self.lineEdit_5.setInputMask("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u79d2\u6570", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u5f55\u5c4f", None))
        self.commandLinkButton_2.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5f55\u5c4f", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6307\u5b9a\u6d3b\u52a8", None))
#if QT_CONFIG(whatsthis)
        self.label_16.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>XTC\u4e13\u7528\u5de5\u5177\u7bb1\uff0c\u5176\u4ed6\u624b\u8868\u4e0d\u8981\u5c1d\u8bd5</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"ToolBox", None))
        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u8f93\u5165\u6cd5\u9009\u62e9", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"\u547d\u4ee4\u884c", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u5f00\u53d1\u8005\u9009\u9879", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u81ea\u68c0", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u5176\u4ed6\u64cd\u4f5c", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"\u542f\u52a8", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"\u5f55\u5c4f", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u4e3b\u9875", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"\u7535\u6c60\u8bbe\u7f6e", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u8bbe\u7f6e", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"Tool", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

