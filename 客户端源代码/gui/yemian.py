# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow - untitled 5VYhsMk.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import apprcc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1250, 855)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1200, 750))
        MainWindow.setStyleSheet(u"")
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_10 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_12 = QFrame(self.centralwidget)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(5)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy1)
        self.verticalLayout_6 = QVBoxLayout(self.frame_12)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.frame_12)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(30)
        sizePolicy2.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_16 = QVBoxLayout(self.tab)
        self.verticalLayout_16.setSpacing(4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_11 = QScrollArea(self.tab)
        self.scrollArea_11.setObjectName(u"scrollArea_11")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(50)
        sizePolicy3.setHeightForWidth(self.scrollArea_11.sizePolicy().hasHeightForWidth())
        self.scrollArea_11.setSizePolicy(sizePolicy3)
        self.scrollArea_11.setMouseTracking(False)
        self.scrollArea_11.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.scrollArea_11.setLayoutDirection(Qt.LeftToRight)
        self.scrollArea_11.setInputMethodHints(Qt.ImhNone)
        self.scrollArea_11.setFrameShape(QFrame.NoFrame)
        self.scrollArea_11.setMidLineWidth(0)
        self.scrollArea_11.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_11.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_11.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea_11.setWidgetResizable(True)
        self.scrollArea_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.scrollAreaWidgetContents_11 = QWidget()
        self.scrollAreaWidgetContents_11.setObjectName(u"scrollAreaWidgetContents_11")
        self.scrollAreaWidgetContents_11.setGeometry(QRect(0, 0, 870, 624))
        self.gridLayout_8 = QGridLayout(self.scrollAreaWidgetContents_11)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.scrollArea_11.setWidget(self.scrollAreaWidgetContents_11)

        self.verticalLayout_16.addWidget(self.scrollArea_11)

        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_39 = QVBoxLayout(self.tab_3)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.widget_39 = QWidget(self.tab_3)
        self.widget_39.setObjectName(u"widget_39")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_39)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.gf_search = QLineEdit(self.widget_39)
        self.gf_search.setObjectName(u"gf_search")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.gf_search.sizePolicy().hasHeightForWidth())
        self.gf_search.setSizePolicy(sizePolicy4)
        self.gf_search.setMinimumSize(QSize(200, 0))
        self.gf_search.setCursorPosition(0)

        self.horizontalLayout_15.addWidget(self.gf_search)

        self.gf_shuaixuan = QComboBox(self.widget_39)
        self.gf_shuaixuan.addItem("")
        self.gf_shuaixuan.addItem("")
        self.gf_shuaixuan.addItem("")
        self.gf_shuaixuan.addItem("")
        self.gf_shuaixuan.addItem("")
        self.gf_shuaixuan.addItem("")
        self.gf_shuaixuan.setObjectName(u"gf_shuaixuan")

        self.horizontalLayout_15.addWidget(self.gf_shuaixuan)

        self.label_19 = QLabel(self.widget_39)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_15.addWidget(self.label_19)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_7)

        self.gf_pailie = QComboBox(self.widget_39)
        self.gf_pailie.addItem("")
        self.gf_pailie.addItem("")
        self.gf_pailie.addItem("")
        self.gf_pailie.setObjectName(u"gf_pailie")

        self.horizontalLayout_15.addWidget(self.gf_pailie)


        self.verticalLayout_39.addWidget(self.widget_39)

        self.scrollArea_5 = QScrollArea(self.tab_3)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        sizePolicy3.setHeightForWidth(self.scrollArea_5.sizePolicy().hasHeightForWidth())
        self.scrollArea_5.setSizePolicy(sizePolicy3)
        self.scrollArea_5.setMouseTracking(False)
        self.scrollArea_5.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.scrollArea_5.setLayoutDirection(Qt.LeftToRight)
        self.scrollArea_5.setInputMethodHints(Qt.ImhNone)
        self.scrollArea_5.setFrameShape(QFrame.NoFrame)
        self.scrollArea_5.setMidLineWidth(0)
        self.scrollArea_5.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_5.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 870, 574))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_39.addWidget(self.scrollArea_5)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.verticalLayout_81 = QVBoxLayout(self.tab_7)
        self.verticalLayout_81.setSpacing(0)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.verticalLayout_81.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.tab_7)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_37 = QHBoxLayout(self.page)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.frame_90 = QFrame(self.page)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMinimumSize(QSize(510, 410))
        self.frame_90.setMaximumSize(QSize(510, 410))
        self.verticalLayout_83 = QVBoxLayout(self.frame_90)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.widget_91 = QWidget(self.frame_90)
        self.widget_91.setObjectName(u"widget_91")
        self.horizontalLayout_40 = QHBoxLayout(self.widget_91)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_114 = QLabel(self.widget_91)
        self.label_114.setObjectName(u"label_114")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(70)
        sizePolicy5.setVerticalStretch(70)
        sizePolicy5.setHeightForWidth(self.label_114.sizePolicy().hasHeightForWidth())
        self.label_114.setSizePolicy(sizePolicy5)
        self.label_114.setMinimumSize(QSize(70, 70))
        self.label_114.setMaximumSize(QSize(70, 70))
        self.label_114.setPixmap(QPixmap(u":/pic/pic/Glass_JE4_BE2.png"))

        self.horizontalLayout_40.addWidget(self.label_114)


        self.verticalLayout_83.addWidget(self.widget_91)

        self.label_93 = QLabel(self.frame_90)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setStyleSheet(u"font-size:30px;\n"
"font-weight:500;")
        self.label_93.setAlignment(Qt.AlignCenter)

        self.verticalLayout_83.addWidget(self.label_93)

        self.label_95 = QLabel(self.frame_90)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setStyleSheet(u"font-size:20px;\n"
"font-weight:450;")
        self.label_95.setAlignment(Qt.AlignCenter)

        self.verticalLayout_83.addWidget(self.label_95)

        self.lineEdit_7 = QLineEdit(self.frame_90)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.verticalLayout_83.addWidget(self.lineEdit_7)

        self.lineEdit_9 = QLineEdit(self.frame_90)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setEchoMode(QLineEdit.Password)

        self.verticalLayout_83.addWidget(self.lineEdit_9)

        self.checkBox = QCheckBox(self.frame_90)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_83.addWidget(self.checkBox)

        self.widget_89 = QWidget(self.frame_90)
        self.widget_89.setObjectName(u"widget_89")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_89)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, -1, 0, -1)
        self.pushButton_2 = QPushButton(self.widget_89)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_21.addWidget(self.pushButton_2)

        self.horizontalSpacer_16 = QSpacerItem(246, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_16)

        self.pushButton_20 = QPushButton(self.widget_89)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.horizontalLayout_21.addWidget(self.pushButton_20)


        self.verticalLayout_83.addWidget(self.widget_89)


        self.horizontalLayout_37.addWidget(self.frame_90)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_38 = QHBoxLayout(self.page_2)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.frame_92 = QFrame(self.page_2)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setMinimumSize(QSize(510, 410))
        self.frame_92.setMaximumSize(QSize(510, 410))
        self.verticalLayout_84 = QVBoxLayout(self.frame_92)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.widget_108 = QWidget(self.frame_92)
        self.widget_108.setObjectName(u"widget_108")
        self.horizontalLayout_41 = QHBoxLayout(self.widget_108)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_115 = QLabel(self.widget_108)
        self.label_115.setObjectName(u"label_115")
        sizePolicy5.setHeightForWidth(self.label_115.sizePolicy().hasHeightForWidth())
        self.label_115.setSizePolicy(sizePolicy5)
        self.label_115.setMinimumSize(QSize(70, 70))
        self.label_115.setMaximumSize(QSize(70, 70))
        self.label_115.setPixmap(QPixmap(u":/pic/pic/Glass_JE4_BE2.png"))

        self.horizontalLayout_41.addWidget(self.label_115)


        self.verticalLayout_84.addWidget(self.widget_108)

        self.label_94 = QLabel(self.frame_92)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setAlignment(Qt.AlignCenter)

        self.verticalLayout_84.addWidget(self.label_94)

        self.lineEdit_11 = QLineEdit(self.frame_92)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.verticalLayout_84.addWidget(self.lineEdit_11)

        self.lineEdit_8 = QLineEdit(self.frame_92)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.verticalLayout_84.addWidget(self.lineEdit_8)

        self.lineEdit_10 = QLineEdit(self.frame_92)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setEchoMode(QLineEdit.Normal)

        self.verticalLayout_84.addWidget(self.lineEdit_10)

        self.widget_94 = QWidget(self.frame_92)
        self.widget_94.setObjectName(u"widget_94")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_94)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, -1, 0, -1)
        self.pushButton_21 = QPushButton(self.widget_94)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.horizontalLayout_22.addWidget(self.pushButton_21)

        self.horizontalSpacer_17 = QSpacerItem(310, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_17)

        self.pushButton_22 = QPushButton(self.widget_94)
        self.pushButton_22.setObjectName(u"pushButton_22")

        self.horizontalLayout_22.addWidget(self.pushButton_22)


        self.verticalLayout_84.addWidget(self.widget_94)


        self.horizontalLayout_38.addWidget(self.frame_92)

        self.stackedWidget.addWidget(self.page_2)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.horizontalLayout_50 = QHBoxLayout(self.page_4)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.scrollArea_2 = QScrollArea(self.page_4)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 850, 604))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.scrollAreaWidgetContents_2)
        self.frame.setObjectName(u"frame")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(5)
        sizePolicy6.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy6)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_38 = QLabel(self.widget)
        self.label_38.setObjectName(u"label_38")
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy7.setHorizontalStretch(200)
        sizePolicy7.setVerticalStretch(200)
        sizePolicy7.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy7)
        self.label_38.setMaximumSize(QSize(125, 125))
        self.label_38.setStyleSheet(u"")
        self.label_38.setPixmap(QPixmap(u":/pic/pic/Pink_Stained_Glass_JE3_BE3.png"))

        self.gridLayout_2.addWidget(self.label_38, 0, 0, 1, 1)


        self.horizontalLayout_46.addWidget(self.widget)

        self.widget_12 = QWidget(self.frame)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(10)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy8)
        self.verticalLayout_2 = QVBoxLayout(self.widget_12)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_14 = QWidget(self.widget_12)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_49 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_39 = QLabel(self.widget_14)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_49.addWidget(self.label_39)


        self.verticalLayout_2.addWidget(self.widget_14)

        self.widget_15 = QWidget(self.widget_12)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_47 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_42 = QLabel(self.widget_15)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_47.addWidget(self.label_42)


        self.verticalLayout_2.addWidget(self.widget_15)

        self.widget_13 = QWidget(self.widget_12)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout = QHBoxLayout(self.widget_13)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_15 = QPushButton(self.widget_13)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.horizontalLayout.addWidget(self.pushButton_15)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_12)


        self.verticalLayout_2.addWidget(self.widget_13)


        self.horizontalLayout_46.addWidget(self.widget_12)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(7)
        sizePolicy9.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy9)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget_4 = QTabWidget(self.frame_2)
        self.tabWidget_4.setObjectName(u"tabWidget_4")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.gridLayout_9 = QGridLayout(self.tab_12)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.tabWidget_4.addTab(self.tab_12, "")
        self.tab_16 = QWidget()
        self.tab_16.setObjectName(u"tab_16")
        self.verticalLayout_10 = QVBoxLayout(self.tab_16)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.groupBox_11 = QGroupBox(self.tab_16)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.verticalLayout_95 = QVBoxLayout(self.groupBox_11)
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.widget_121 = QWidget(self.groupBox_11)
        self.widget_121.setObjectName(u"widget_121")
        self.horizontalLayout_73 = QHBoxLayout(self.widget_121)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.label_156 = QLabel(self.widget_121)
        self.label_156.setObjectName(u"label_156")

        self.horizontalLayout_73.addWidget(self.label_156)

        self.horizontalSpacer_46 = QSpacerItem(509, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_73.addItem(self.horizontalSpacer_46)

        self.comboBox_27 = QComboBox(self.widget_121)
        self.comboBox_27.addItem("")
        self.comboBox_27.addItem("")
        self.comboBox_27.setObjectName(u"comboBox_27")

        self.horizontalLayout_73.addWidget(self.comboBox_27)


        self.verticalLayout_95.addWidget(self.widget_121)

        self.widget_123 = QWidget(self.groupBox_11)
        self.widget_123.setObjectName(u"widget_123")
        self.horizontalLayout_75 = QHBoxLayout(self.widget_123)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.label_158 = QLabel(self.widget_123)
        self.label_158.setObjectName(u"label_158")

        self.horizontalLayout_75.addWidget(self.label_158)

        self.horizontalSpacer_48 = QSpacerItem(509, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_75.addItem(self.horizontalSpacer_48)

        self.pushButton_49 = QPushButton(self.widget_123)
        self.pushButton_49.setObjectName(u"pushButton_49")

        self.horizontalLayout_75.addWidget(self.pushButton_49)


        self.verticalLayout_95.addWidget(self.widget_123)


        self.verticalLayout_10.addWidget(self.groupBox_11)

        self.tabWidget_4.addTab(self.tab_16, "")

        self.verticalLayout_3.addWidget(self.tabWidget_4)


        self.verticalLayout.addWidget(self.frame_2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_50.addWidget(self.scrollArea_2)

        self.stackedWidget.addWidget(self.page_4)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout = QGridLayout(self.page_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_91 = QFrame(self.page_3)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setMinimumSize(QSize(510, 410))
        self.frame_91.setMaximumSize(QSize(510, 410))
        self.verticalLayout_85 = QVBoxLayout(self.frame_91)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.widget_92 = QWidget(self.frame_91)
        self.widget_92.setObjectName(u"widget_92")
        self.horizontalLayout_42 = QHBoxLayout(self.widget_92)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_116 = QLabel(self.widget_92)
        self.label_116.setObjectName(u"label_116")
        sizePolicy5.setHeightForWidth(self.label_116.sizePolicy().hasHeightForWidth())
        self.label_116.setSizePolicy(sizePolicy5)
        self.label_116.setMinimumSize(QSize(70, 70))
        self.label_116.setMaximumSize(QSize(70, 70))
        self.label_116.setPixmap(QPixmap(u":/pic/pic/Glass_JE4_BE2.png"))

        self.horizontalLayout_42.addWidget(self.label_116)


        self.verticalLayout_85.addWidget(self.widget_92)

        self.label_96 = QLabel(self.frame_91)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setStyleSheet(u"font-size:30px;\n"
"font-weight:500;")
        self.label_96.setAlignment(Qt.AlignCenter)

        self.verticalLayout_85.addWidget(self.label_96)

        self.label_97 = QLabel(self.frame_91)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setStyleSheet(u"font-size:15px;\n"
"font-weight:450;")
        self.label_97.setAlignment(Qt.AlignCenter)

        self.verticalLayout_85.addWidget(self.label_97)

        self.lineEdit_14 = QLineEdit(self.frame_91)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setEchoMode(QLineEdit.Normal)
        self.lineEdit_14.setReadOnly(True)

        self.verticalLayout_85.addWidget(self.lineEdit_14)

        self.label_15 = QLabel(self.frame_91)
        self.label_15.setObjectName(u"label_15")
        sizePolicy10 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy10)
        self.label_15.setStyleSheet(u"color:#ff4757;")

        self.verticalLayout_85.addWidget(self.label_15)

        self.widget_90 = QWidget(self.frame_91)
        self.widget_90.setObjectName(u"widget_90")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_90)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, -1, 0, -1)
        self.pushButton_3 = QPushButton(self.widget_90)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_23.addWidget(self.pushButton_3)

        self.horizontalSpacer_18 = QSpacerItem(246, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_18)

        self.pushButton_23 = QPushButton(self.widget_90)
        self.pushButton_23.setObjectName(u"pushButton_23")

        self.horizontalLayout_23.addWidget(self.pushButton_23)


        self.verticalLayout_85.addWidget(self.widget_90)


        self.gridLayout.addWidget(self.frame_91, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout_81.addWidget(self.stackedWidget)

        self.tabWidget.addTab(self.tab_7, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_82 = QVBoxLayout(self.tab_6)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_82.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_10 = QScrollArea(self.tab_6)
        self.scrollArea_10.setObjectName(u"scrollArea_10")
        self.scrollArea_10.setWidgetResizable(True)
        self.scrollAreaWidgetContents_10 = QWidget()
        self.scrollAreaWidgetContents_10.setObjectName(u"scrollAreaWidgetContents_10")
        self.scrollAreaWidgetContents_10.setGeometry(QRect(0, 0, 868, 622))
        sizePolicy11 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.scrollAreaWidgetContents_10.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_10.setSizePolicy(sizePolicy11)
        self.verticalLayout_87 = QVBoxLayout(self.scrollAreaWidgetContents_10)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.groupBox_6 = QGroupBox(self.scrollAreaWidgetContents_10)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_88 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.widget_102 = QWidget(self.groupBox_6)
        self.widget_102.setObjectName(u"widget_102")
        self.horizontalLayout_31 = QHBoxLayout(self.widget_102)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_104 = QLabel(self.widget_102)
        self.label_104.setObjectName(u"label_104")

        self.horizontalLayout_31.addWidget(self.label_104)

        self.horizontalSpacer_25 = QSpacerItem(509, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_25)

        self.comboBox_19 = QComboBox(self.widget_102)
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.setObjectName(u"comboBox_19")

        self.horizontalLayout_31.addWidget(self.comboBox_19)


        self.verticalLayout_88.addWidget(self.widget_102)

        self.widget_103 = QWidget(self.groupBox_6)
        self.widget_103.setObjectName(u"widget_103")
        self.horizontalLayout_33 = QHBoxLayout(self.widget_103)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_106 = QLabel(self.widget_103)
        self.label_106.setObjectName(u"label_106")

        self.horizontalLayout_33.addWidget(self.label_106)

        self.horizontalSpacer_27 = QSpacerItem(509, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_27)

        self.lineEdit = QLineEdit(self.widget_103)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_33.addWidget(self.lineEdit)

        self.label_14 = QLabel(self.widget_103)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_33.addWidget(self.label_14)


        self.verticalLayout_88.addWidget(self.widget_103)

        self.widget_104 = QWidget(self.groupBox_6)
        self.widget_104.setObjectName(u"widget_104")
        self.horizontalLayout_32 = QHBoxLayout(self.widget_104)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_105 = QLabel(self.widget_104)
        self.label_105.setObjectName(u"label_105")

        self.horizontalLayout_32.addWidget(self.label_105)

        self.horizontalSpacer_26 = QSpacerItem(509, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_26)

        self.pushButton_8 = QPushButton(self.widget_104)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_32.addWidget(self.pushButton_8)


        self.verticalLayout_88.addWidget(self.widget_104)


        self.verticalLayout_87.addWidget(self.groupBox_6)

        self.groupBox_8 = QGroupBox(self.scrollAreaWidgetContents_10)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_91 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.label_109 = QLabel(self.groupBox_8)
        self.label_109.setObjectName(u"label_109")

        self.verticalLayout_91.addWidget(self.label_109)

        self.label_110 = QLabel(self.groupBox_8)
        self.label_110.setObjectName(u"label_110")

        self.verticalLayout_91.addWidget(self.label_110)

        self.widget_107 = QWidget(self.groupBox_8)
        self.widget_107.setObjectName(u"widget_107")
        self.horizontalLayout_36 = QHBoxLayout(self.widget_107)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.label_111 = QLabel(self.widget_107)
        self.label_111.setObjectName(u"label_111")
        sizePolicy12 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy12.setHorizontalStretch(1)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.label_111.sizePolicy().hasHeightForWidth())
        self.label_111.setSizePolicy(sizePolicy12)

        self.horizontalLayout_36.addWidget(self.label_111)

        self.label_112 = QLabel(self.widget_107)
        self.label_112.setObjectName(u"label_112")
        sizePolicy1.setHeightForWidth(self.label_112.sizePolicy().hasHeightForWidth())
        self.label_112.setSizePolicy(sizePolicy1)

        self.horizontalLayout_36.addWidget(self.label_112)


        self.verticalLayout_91.addWidget(self.widget_107)

        self.widget_109 = QWidget(self.groupBox_8)
        self.widget_109.setObjectName(u"widget_109")
        self.horizontalLayout_39 = QHBoxLayout(self.widget_109)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_113 = QLabel(self.widget_109)
        self.label_113.setObjectName(u"label_113")
        sizePolicy12.setHeightForWidth(self.label_113.sizePolicy().hasHeightForWidth())
        self.label_113.setSizePolicy(sizePolicy12)

        self.horizontalLayout_39.addWidget(self.label_113)

        self.label_117 = QLabel(self.widget_109)
        self.label_117.setObjectName(u"label_117")
        sizePolicy1.setHeightForWidth(self.label_117.sizePolicy().hasHeightForWidth())
        self.label_117.setSizePolicy(sizePolicy1)

        self.horizontalLayout_39.addWidget(self.label_117)


        self.verticalLayout_91.addWidget(self.widget_109)

        self.widget_110 = QWidget(self.groupBox_8)
        self.widget_110.setObjectName(u"widget_110")
        self.horizontalLayout_45 = QHBoxLayout(self.widget_110)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_118 = QLabel(self.widget_110)
        self.label_118.setObjectName(u"label_118")
        sizePolicy12.setHeightForWidth(self.label_118.sizePolicy().hasHeightForWidth())
        self.label_118.setSizePolicy(sizePolicy12)

        self.horizontalLayout_45.addWidget(self.label_118)

        self.pushButton_5 = QPushButton(self.widget_110)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.horizontalLayout_45.addWidget(self.pushButton_5)


        self.verticalLayout_91.addWidget(self.widget_110)


        self.verticalLayout_87.addWidget(self.groupBox_8)

        self.scrollArea_10.setWidget(self.scrollAreaWidgetContents_10)

        self.verticalLayout_82.addWidget(self.scrollArea_10)

        self.tabWidget.addTab(self.tab_6, "")

        self.verticalLayout_6.addWidget(self.tabWidget)

        self.widget_2 = QWidget(self.frame_12)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy13 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(1)
        sizePolicy13.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy13)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 9, -1, 9)
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"font-size : 22px;")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.pushButton_4 = QPushButton(self.widget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_6 = QPushButton(self.widget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_3.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.widget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_3.addWidget(self.pushButton_7)

        self.horizontalSpacer_2 = QSpacerItem(50, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_6.addWidget(self.widget_2)

        self.scrollArea_3 = QScrollArea(self.frame_12)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        sizePolicy14 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(5)
        sizePolicy14.setHeightForWidth(self.scrollArea_3.sizePolicy().hasHeightForWidth())
        self.scrollArea_3.setSizePolicy(sizePolicy14)
        self.scrollArea_3.setFrameShape(QFrame.NoFrame)
        self.scrollArea_3.setLineWidth(0)
        self.scrollArea_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 876, 109))
        self.horizontalLayout_4 = QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 0, 9, 0)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_6.addWidget(self.scrollArea_3)


        self.horizontalLayout_10.addWidget(self.frame_12)

        self.frame_23 = QFrame(self.centralwidget)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy15 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy15.setHorizontalStretch(2)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy15)
        self.verticalLayout_8 = QVBoxLayout(self.frame_23)
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_21 = QWidget(self.frame_23)
        self.widget_21.setObjectName(u"widget_21")
        sizePolicy13.setHeightForWidth(self.widget_21.sizePolicy().hasHeightForWidth())
        self.widget_21.setSizePolicy(sizePolicy13)
        self.horizontalLayout_9 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 4)
        self.horizontalSpacer_6 = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)

        self.pushButton_14 = QPushButton(self.widget_21)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy16 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy16.setHorizontalStretch(0)
        sizePolicy16.setVerticalStretch(0)
        sizePolicy16.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy16)
        self.pushButton_14.setMinimumSize(QSize(24, 24))
        self.pushButton_14.setMaximumSize(QSize(24, 24))
        self.pushButton_14.setStyleSheet(u"QPushButton{background:#6DDF6D;border-radius:5px;border:none;}QPushButton:hover{background:green;}")

        self.horizontalLayout_9.addWidget(self.pushButton_14)

        self.pushButton_13 = QPushButton(self.widget_21)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy16.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy16)
        self.pushButton_13.setMinimumSize(QSize(24, 24))
        self.pushButton_13.setMaximumSize(QSize(24, 24))
        self.pushButton_13.setStyleSheet(u"QPushButton{background:#F7D674;border-radius:5px;border:none;}QPushButton:hover{background:yellow;}")

        self.horizontalLayout_9.addWidget(self.pushButton_13)

        self.pushButton_12 = QPushButton(self.widget_21)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy16.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy16)
        self.pushButton_12.setMinimumSize(QSize(24, 24))
        self.pushButton_12.setMaximumSize(QSize(24, 24))
        self.pushButton_12.setStyleSheet(u"QPushButton{background:#F76677;border-radius:5px;border:none;}QPushButton:hover{background:red;}")

        self.horizontalLayout_9.addWidget(self.pushButton_12)


        self.verticalLayout_8.addWidget(self.widget_21)

        self.stackedWidget_2 = QStackedWidget(self.frame_23)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        sizePolicy17 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy17.setHorizontalStretch(0)
        sizePolicy17.setVerticalStretch(50)
        sizePolicy17.setHeightForWidth(self.stackedWidget_2.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2.setSizePolicy(sizePolicy17)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_93 = QVBoxLayout(self.page_6)
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.verticalLayout_93.setContentsMargins(5, 0, -1, -1)
        self.scrollArea = QScrollArea(self.page_6)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy18 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy18.setHorizontalStretch(0)
        sizePolicy18.setVerticalStretch(40)
        sizePolicy18.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy18)
        self.scrollArea.setBaseSize(QSize(0, 0))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 318, 1161))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.widget_18 = QWidget(self.scrollAreaWidgetContents)
        self.widget_18.setObjectName(u"widget_18")
        sizePolicy11.setHeightForWidth(self.widget_18.sizePolicy().hasHeightForWidth())
        self.widget_18.setSizePolicy(sizePolicy11)
        self.widget_18.setMinimumSize(QSize(300, 250))
        self.widget_18.setMaximumSize(QSize(16777215, 350))
        self.widget_18.setStyleSheet(u"")
        self.horizontalLayout_43 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.widget_18)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setPixmap(QPixmap(u":/pic/pic/Yellow_Stained_Glass_JE3_BE3.png"))

        self.horizontalLayout_43.addWidget(self.label_37)


        self.verticalLayout_9.addWidget(self.widget_18)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 37))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 20))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_3)

        self.widget_3 = QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 35))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label_16 = QLabel(self.widget_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(20, 20))
        self.label_16.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.label_16)

        self.label_17 = QLabel(self.widget_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(20, 20))
        self.label_17.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.label_17)

        self.label_18 = QLabel(self.widget_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(20, 20))
        self.label_18.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.label_18)

        self.label_29 = QLabel(self.widget_3)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(20, 20))
        self.label_29.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.label_29)

        self.label_30 = QLabel(self.widget_3)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(20, 20))
        self.label_30.setMaximumSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.label_30)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_30)


        self.verticalLayout_9.addWidget(self.widget_3)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 20))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_4)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 20))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_5)

        self.pushButton = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        sizePolicy19 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy19.setHorizontalStretch(0)
        sizePolicy19.setVerticalStretch(0)
        sizePolicy19.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy19)
        self.pushButton.setMinimumSize(QSize(0, 40))

        self.verticalLayout_9.addWidget(self.pushButton)

        self.widget_4 = QWidget(self.scrollAreaWidgetContents)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy11.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy11)
        self.widget_4.setMinimumSize(QSize(0, 70))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_11 = QPushButton(self.widget_4)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy20 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy20.setHorizontalStretch(5)
        sizePolicy20.setVerticalStretch(0)
        sizePolicy20.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy20)
        self.pushButton_11.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_5.addWidget(self.pushButton_11)

        self.pushButton_9 = QPushButton(self.widget_4)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy10.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy10)
        self.pushButton_9.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_5.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.widget_4)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy21 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy21.setHorizontalStretch(0)
        sizePolicy21.setVerticalStretch(0)
        sizePolicy21.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy21)
        self.pushButton_10.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_5.addWidget(self.pushButton_10)


        self.verticalLayout_9.addWidget(self.widget_4)

        self.verticalSpacer_6 = QSpacerItem(5, 20, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_6)

        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy11.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy11)
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_5 = QWidget(self.groupBox)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.widget_5)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.label_7 = QLabel(self.widget_5)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.horizontalSlider = QSlider(self.widget_5)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        sizePolicy22 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy22.setHorizontalStretch(1)
        sizePolicy22.setVerticalStretch(0)
        sizePolicy22.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy22)
        self.horizontalSlider.setMaximum(200)
        self.horizontalSlider.setPageStep(100)
        self.horizontalSlider.setSliderPosition(100)
        self.horizontalSlider.setTracking(True)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider.setTickInterval(0)

        self.horizontalLayout_6.addWidget(self.horizontalSlider)

        self.label_8 = QLabel(self.widget_5)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_6.addWidget(self.label_8)


        self.verticalLayout_4.addWidget(self.widget_5)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.widget_7 = QWidget(self.groupBox)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_8 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_12 = QLabel(self.widget_7)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_8.addWidget(self.label_12)

        self.label_13 = QLabel(self.widget_7)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_8.addWidget(self.label_13)

        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.comboBox_2 = QComboBox(self.widget_7)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy23 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy23.setHorizontalStretch(10)
        sizePolicy23.setVerticalStretch(0)
        sizePolicy23.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy23)

        self.horizontalLayout_8.addWidget(self.comboBox_2)


        self.verticalLayout_4.addWidget(self.widget_7)

        self.verticalSpacer_5 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.widget_6 = QWidget(self.groupBox)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_7 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_9 = QLabel(self.widget_6)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_7.addWidget(self.label_9)

        self.label_10 = QLabel(self.widget_6)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_7.addWidget(self.label_10)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.horizontalSlider_2 = QSlider(self.widget_6)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        sizePolicy22.setHeightForWidth(self.horizontalSlider_2.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_2.setSizePolicy(sizePolicy22)
        self.horizontalSlider_2.setMaximum(100)
        self.horizontalSlider_2.setPageStep(100)
        self.horizontalSlider_2.setValue(50)
        self.horizontalSlider_2.setSliderPosition(50)
        self.horizontalSlider_2.setTracking(True)
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)
        self.horizontalSlider_2.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_2.setTickInterval(0)

        self.horizontalLayout_7.addWidget(self.horizontalSlider_2)

        self.label_11 = QLabel(self.widget_6)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_7.addWidget(self.label_11)


        self.verticalLayout_4.addWidget(self.widget_6)

        self.verticalSpacer_74 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.verticalSpacer_74)

        self.widget_96 = QWidget(self.groupBox)
        self.widget_96.setObjectName(u"widget_96")
        self.widget_96.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_44 = QHBoxLayout(self.widget_96)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_120 = QLabel(self.widget_96)
        self.label_120.setObjectName(u"label_120")

        self.horizontalLayout_44.addWidget(self.label_120)

        self.label_121 = QLabel(self.widget_96)
        self.label_121.setObjectName(u"label_121")

        self.horizontalLayout_44.addWidget(self.label_121)

        self.horizontalSpacer_31 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_31)

        self.checkBox_3 = QCheckBox(self.widget_96)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.horizontalLayout_44.addWidget(self.checkBox_3)


        self.verticalLayout_4.addWidget(self.widget_96)


        self.verticalLayout_9.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 250))
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.widget_8 = QWidget(self.groupBox_2)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_11 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_21 = QLabel(self.widget_8)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_11.addWidget(self.label_21)

        self.label_22 = QLabel(self.widget_8)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_11.addWidget(self.label_22)

        self.horizontalSpacer_8 = QSpacerItem(45, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_8)

        self.horizontalSlider_5 = QSlider(self.widget_8)
        self.horizontalSlider_5.setObjectName(u"horizontalSlider_5")
        sizePolicy22.setHeightForWidth(self.horizontalSlider_5.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_5.setSizePolicy(sizePolicy22)
        self.horizontalSlider_5.setMaximum(100)
        self.horizontalSlider_5.setPageStep(100)
        self.horizontalSlider_5.setSliderPosition(50)
        self.horizontalSlider_5.setTracking(True)
        self.horizontalSlider_5.setOrientation(Qt.Horizontal)
        self.horizontalSlider_5.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_5.setTickInterval(0)

        self.horizontalLayout_11.addWidget(self.horizontalSlider_5)

        self.label_23 = QLabel(self.widget_8)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_11.addWidget(self.label_23)


        self.verticalLayout_5.addWidget(self.widget_8)

        self.verticalSpacer_16 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_5.addItem(self.verticalSpacer_16)

        self.widget_10 = QWidget(self.groupBox_2)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_13 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_26 = QLabel(self.widget_10)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_13.addWidget(self.label_26)

        self.label_27 = QLabel(self.widget_10)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_13.addWidget(self.label_27)

        self.horizontalSpacer_10 = QSpacerItem(35, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_10)

        self.horizontalSlider_6 = QSlider(self.widget_10)
        self.horizontalSlider_6.setObjectName(u"horizontalSlider_6")
        sizePolicy22.setHeightForWidth(self.horizontalSlider_6.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_6.setSizePolicy(sizePolicy22)
        self.horizontalSlider_6.setMaximum(100)
        self.horizontalSlider_6.setPageStep(100)
        self.horizontalSlider_6.setSliderPosition(50)
        self.horizontalSlider_6.setTracking(True)
        self.horizontalSlider_6.setOrientation(Qt.Horizontal)
        self.horizontalSlider_6.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_6.setTickInterval(0)

        self.horizontalLayout_13.addWidget(self.horizontalSlider_6)

        self.label_28 = QLabel(self.widget_10)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_13.addWidget(self.label_28)


        self.verticalLayout_5.addWidget(self.widget_10)

        self.verticalSpacer_17 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_5.addItem(self.verticalSpacer_17)

        self.widget_9 = QWidget(self.groupBox_2)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_12 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_24 = QLabel(self.widget_9)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_12.addWidget(self.label_24)

        self.label_25 = QLabel(self.widget_9)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_12.addWidget(self.label_25)

        self.horizontalSpacer_9 = QSpacerItem(35, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_9)

        self.horizontalSlider_7 = QSlider(self.widget_9)
        self.horizontalSlider_7.setObjectName(u"horizontalSlider_7")
        sizePolicy22.setHeightForWidth(self.horizontalSlider_7.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_7.setSizePolicy(sizePolicy22)
        self.horizontalSlider_7.setMaximum(100)
        self.horizontalSlider_7.setPageStep(100)
        self.horizontalSlider_7.setSliderPosition(50)
        self.horizontalSlider_7.setTracking(True)
        self.horizontalSlider_7.setOrientation(Qt.Horizontal)
        self.horizontalSlider_7.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_7.setTickInterval(0)

        self.horizontalLayout_12.addWidget(self.horizontalSlider_7)

        self.label_31 = QLabel(self.widget_9)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_12.addWidget(self.label_31)


        self.verticalLayout_5.addWidget(self.widget_9)

        self.verticalSpacer_9 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_5.addItem(self.verticalSpacer_9)

        self.widget_11 = QWidget(self.groupBox_2)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_14 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_32 = QLabel(self.widget_11)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_14.addWidget(self.label_32)

        self.label_33 = QLabel(self.widget_11)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_14.addWidget(self.label_33)

        self.horizontalSpacer_11 = QSpacerItem(22, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_11)

        self.horizontalSlider_8 = QSlider(self.widget_11)
        self.horizontalSlider_8.setObjectName(u"horizontalSlider_8")
        sizePolicy22.setHeightForWidth(self.horizontalSlider_8.sizePolicy().hasHeightForWidth())
        self.horizontalSlider_8.setSizePolicy(sizePolicy22)
        self.horizontalSlider_8.setMaximum(100)
        self.horizontalSlider_8.setPageStep(100)
        self.horizontalSlider_8.setSliderPosition(50)
        self.horizontalSlider_8.setTracking(True)
        self.horizontalSlider_8.setOrientation(Qt.Horizontal)
        self.horizontalSlider_8.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_8.setTickInterval(0)

        self.horizontalLayout_14.addWidget(self.horizontalSlider_8)

        self.label_34 = QLabel(self.widget_11)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_14.addWidget(self.label_34)


        self.verticalLayout_5.addWidget(self.widget_11)

        self.verticalSpacer_7 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_5.addItem(self.verticalSpacer_7)


        self.verticalLayout_9.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 0))
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")

        self.verticalLayout_9.addWidget(self.groupBox_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_93.addWidget(self.scrollArea)

        self.stackedWidget_2.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.stackedWidget_2.addWidget(self.page_7)

        self.verticalLayout_8.addWidget(self.stackedWidget_2)


        self.horizontalLayout_10.addWidget(self.frame_23)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1250, 23))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.pushButton_14.clicked.connect(MainWindow.showMinimized)
        self.pushButton_13.clicked.connect(MainWindow.showMaximized)
        self.pushButton_12.clicked.connect(MainWindow.hide)
        self.horizontalSlider.sliderMoved.connect(self.label_8.setNum)
        self.horizontalSlider_2.sliderMoved.connect(self.label_11.setNum)
        self.horizontalSlider_5.sliderMoved.connect(self.label_23.setNum)
        self.horizontalSlider_6.sliderMoved.connect(self.label_28.setNum)
        self.horizontalSlider_7.sliderMoved.connect(self.label_31.setNum)
        self.horizontalSlider_8.sliderMoved.connect(self.label_34.setNum)
        self.horizontalSlider.valueChanged.connect(self.label_8.setNum)
        self.horizontalSlider_2.valueChanged.connect(self.label_11.setNum)
        self.horizontalSlider_5.valueChanged.connect(self.label_23.setNum)
        self.horizontalSlider_6.valueChanged.connect(self.label_28.setNum)
        self.horizontalSlider_7.valueChanged.connect(self.label_31.setNum)
        self.horizontalSlider_8.valueChanged.connect(self.label_34.setNum)
        self.checkBox_3.clicked.connect(self.groupBox_2.setVisible)

        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(whatsthis)
        self.tab.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u672c\u5730", None))
        self.gf_search.setInputMask("")
        self.gf_search.setText("")
        self.gf_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        self.gf_shuaixuan.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5168\u90e8", None))
        self.gf_shuaixuan.setItemText(1, QCoreApplication.translate("MainWindow", u"\u6e38\u620f", None))
        self.gf_shuaixuan.setItemText(2, QCoreApplication.translate("MainWindow", u"\u52a8\u6f2b", None))
        self.gf_shuaixuan.setItemText(3, QCoreApplication.translate("MainWindow", u"\u79d1\u6280", None))
        self.gf_shuaixuan.setItemText(4, QCoreApplication.translate("MainWindow", u"\u98ce\u666f", None))
        self.gf_shuaixuan.setItemText(5, QCoreApplication.translate("MainWindow", u"\u653f\u6cbb", None))

        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u6b63\u5728\u52a0\u8f7d,\u8bf7\u7a0d\u540e......", None))
        self.gf_pailie.setItemText(0, QCoreApplication.translate("MainWindow", u"\u65f6\u95f4", None))
        self.gf_pailie.setItemText(1, QCoreApplication.translate("MainWindow", u"\u540d\u79f0", None))
        self.gf_pailie.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5927\u5c0f", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u5de5\u574a", None))
        self.label_114.setText("")
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5165", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u60a8\u7684Glass\u8d26\u53f7", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7535\u5b50\u90ae\u4ef6", None))
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u5bc6\u7801", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u521b\u5efa\u8d26\u53f7", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5165", None))
        self.label_115.setText("")
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"\u521b\u5efa\u60a8\u7684 Glass \u8d26\u53f7", None))
        self.lineEdit_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7535\u5b50\u90ae\u4ef6", None))
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5165\u73b0\u6709\u8d26\u53f7", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u6b65", None))
        self.label_38.setText("")
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"user_name", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u518c\u65f6\u95f4:", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"\u6211\u559c\u6b22", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"\u5b89\u5168", None))
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u767b\u5165", None))
        self.comboBox_27.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5426", None))
        self.comboBox_27.setItemText(1, QCoreApplication.translate("MainWindow", u"\u662f", None))

        self.label_158.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u767b\u5f55", None))
        self.pushButton_49.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_16), QCoreApplication.translate("MainWindow", u"\u4e2a\u4eba\u8bbe\u7f6e", None))
        self.label_116.setText("")
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"\u9a8c\u8bc1\u60a8\u7684\u90ae\u7bb1", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u60a8\u572810\u5206\u949f\u5185\u4f7f\u7528\u4ee5\u4e0b\u5185\u5bb9\u4f5c\u4e3a\u90ae\u4ef6\u4e3b\u9898,\u53d1\u9001\u81f3team@sjbsjb.xyz", None))
        self.lineEdit_14.setText("")
        self.lineEdit_14.setPlaceholderText("")
        self.label_15.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u8fd4\u56de", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"\u6211\u5df2\u53d1\u9001", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"\u6211", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u58c1\u7eb8", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u673a\u542f\u52a8:", None))
        self.comboBox_19.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5f00\u673a\u81ea\u542f", None))
        self.comboBox_19.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4e0d\u81ea\u542f", None))

        self.label_106.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4e00\u58c1\u7eb8\u5faa\u73af\u65f6\u95f4:(\u56de\u8f66\u5e94\u7528)", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u6beb\u79d2", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"\u684c\u9762\u5ba0\u7269:", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542f", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Glass Wallpaper", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"\u7531SJBSJB233\u5236\u4f5c", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"\u8054\u7cfb\u6211\u4eec: ", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"support@sjbsjb.xyz", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"\u5b98\u7f51: ", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"https://glass.sjbsjb.xyz", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"Glass\u534f\u8bae\u53ca\u5f00\u6e90\u8bb8\u53ef: ", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u64ad\u653e\u5217\u8868(5)", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u5165", None))
        self.pushButton_14.setText("")
        self.pushButton_13.setText("")
        self.pushButton_12.setText("")
        self.label_37.setText("")
        self.label.setText("")
        self.label_3.setText("")
        self.label_16.setText("")
        self.label_17.setText("")
        self.label_18.setText("")
        self.label_29.setText("")
        self.label_30.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u8ba2\u9605", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u559c\u6b22", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u8bc4\u5206", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u4e3e\u62a5", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u5c5e\u6027", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u56fe", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u64ad\u653e\u901f\u5ea6", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u56fe", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u5bf9\u9f50\u65b9\u5f0f", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u8986\u76d6", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u81ea\u7531", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5c45\u4e2d", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"\u5de6\u4e0a", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"\u5de6\u4e2d", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u56fe", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u4f4d\u56fe\u50cf\u7f6e", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"\u56fe", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"\u9ad8\u7ea7\u9009\u9879", None))
        self.checkBox_3.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u9ad8\u7ea7\u9009\u9879", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u56fe", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u4eae\u5ea6", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u56fe", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u5bf9\u6bd4\u5ea6", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u56fe", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u9971\u548c\u5ea6", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u56fe", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u8272\u8c03\u504f\u79fb", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"MOD", None))
    # retranslateUi

