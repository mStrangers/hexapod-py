# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(587, 560)
        MainWindow.setMinimumSize(QSize(500, 560))
        icon = QIcon()
        icon.addFile(u"res/hexapod-logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.button_Refresh = QPushButton(self.tab)
        self.button_Refresh.setObjectName(u"button_Refresh")
        icon1 = QIcon()
        icon1.addFile(u"res/arrows-rotate-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_Refresh.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.button_Refresh)

        self.comboBox_Interface = QComboBox(self.tab)
        self.comboBox_Interface.setObjectName(u"comboBox_Interface")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_Interface.sizePolicy().hasHeightForWidth())
        self.comboBox_Interface.setSizePolicy(sizePolicy)
        self.comboBox_Interface.setMinimumSize(QSize(100, 0))
        self.comboBox_Interface.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_5.addWidget(self.comboBox_Interface)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.label_LocalIP = QLabel(self.tab)
        self.label_LocalIP.setObjectName(u"label_LocalIP")
        self.label_LocalIP.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.horizontalLayout_5.addWidget(self.label_LocalIP)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_targetIP = QLabel(self.tab)
        self.label_targetIP.setObjectName(u"label_targetIP")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_targetIP.sizePolicy().hasHeightForWidth())
        self.label_targetIP.setSizePolicy(sizePolicy1)
        self.label_targetIP.setMinimumSize(QSize(0, 0))
        self.label_targetIP.setBaseSize(QSize(0, 0))

        self.horizontalLayout_7.addWidget(self.label_targetIP)

        self.lineEdit_TcpClientTargetIP = QLineEdit(self.tab)
        self.lineEdit_TcpClientTargetIP.setObjectName(u"lineEdit_TcpClientTargetIP")
        self.lineEdit_TcpClientTargetIP.setMinimumSize(QSize(150, 0))
        self.lineEdit_TcpClientTargetIP.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_7.addWidget(self.lineEdit_TcpClientTargetIP)

        self.label_targetPort = QLabel(self.tab)
        self.label_targetPort.setObjectName(u"label_targetPort")
        sizePolicy1.setHeightForWidth(self.label_targetPort.sizePolicy().hasHeightForWidth())
        self.label_targetPort.setSizePolicy(sizePolicy1)
        self.label_targetPort.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_7.addWidget(self.label_targetPort)

        self.lineEdit_TcpClientTargetPort = QLineEdit(self.tab)
        self.lineEdit_TcpClientTargetPort.setObjectName(u"lineEdit_TcpClientTargetPort")
        self.lineEdit_TcpClientTargetPort.setMinimumSize(QSize(80, 0))
        self.lineEdit_TcpClientTargetPort.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_7.addWidget(self.lineEdit_TcpClientTargetPort)

        self.buttonTcpConnect = QPushButton(self.tab)
        self.buttonTcpConnect.setObjectName(u"buttonTcpConnect")

        self.horizontalLayout_7.addWidget(self.buttonTcpConnect)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.lineEditBtMac = QLineEdit(self.tab_2)
        self.lineEditBtMac.setObjectName(u"lineEditBtMac")
        sizePolicy.setHeightForWidth(self.lineEditBtMac.sizePolicy().hasHeightForWidth())
        self.lineEditBtMac.setSizePolicy(sizePolicy)
        self.lineEditBtMac.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_4.addWidget(self.lineEditBtMac)

        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.lineEditBtPort = QLineEdit(self.tab_2)
        self.lineEditBtPort.setObjectName(u"lineEditBtPort")
        self.lineEditBtPort.setMinimumSize(QSize(80, 0))
        self.lineEditBtPort.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_4.addWidget(self.lineEditBtPort)

        self.buttonBtConnect = QPushButton(self.tab_2)
        self.buttonBtConnect.setObjectName(u"buttonBtConnect")

        self.horizontalLayout_4.addWidget(self.buttonBtConnect)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.groupBox_Control = QGroupBox(self.centralWidget)
        self.groupBox_Control.setObjectName(u"groupBox_Control")
        font = QFont()
        font.setBold(False)
        self.groupBox_Control.setFont(font)
        self.groupBox_Control.setAlignment(Qt.AlignCenter)
        self.groupBox_Control.setFlat(False)
        self.horizontalLayout = QHBoxLayout(self.groupBox_Control)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(12)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pushButton_Twist = QPushButton(self.groupBox_Control)
        self.pushButton_Twist.setObjectName(u"pushButton_Twist")
        self.pushButton_Twist.setMinimumSize(QSize(50, 50))
        self.pushButton_Twist.setMaximumSize(QSize(50, 50))
        icon2 = QIcon()
        icon2.addFile(u"res/arrow-twist-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Twist.setIcon(icon2)
        self.pushButton_Twist.setIconSize(QSize(32, 32))
        self.pushButton_Twist.setCheckable(False)

        self.gridLayout_3.addWidget(self.pushButton_Twist, 3, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.groupBox_Control)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setEnabled(False)
        self.pushButton_7.setFlat(True)

        self.gridLayout_3.addWidget(self.pushButton_7, 0, 0, 1, 2)

        self.buttonLayDown = QPushButton(self.groupBox_Control)
        self.buttonLayDown.setObjectName(u"buttonLayDown")
        self.buttonLayDown.setEnabled(True)
        self.buttonLayDown.setMinimumSize(QSize(100, 40))
        self.buttonLayDown.setMaximumSize(QSize(100, 40))
        self.buttonLayDown.setAutoFillBackground(False)
        self.buttonLayDown.setAutoDefault(False)
        self.buttonLayDown.setFlat(False)

        self.gridLayout_3.addWidget(self.buttonLayDown, 5, 0, 1, 2)

        self.pushButton_RotateZ = QPushButton(self.groupBox_Control)
        self.pushButton_RotateZ.setObjectName(u"pushButton_RotateZ")
        self.pushButton_RotateZ.setMinimumSize(QSize(50, 50))
        self.pushButton_RotateZ.setMaximumSize(QSize(50, 50))
        icon3 = QIcon()
        icon3.addFile(u"res/arrow-circle-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_RotateZ.setIcon(icon3)
        self.pushButton_RotateZ.setIconSize(QSize(32, 32))
        self.pushButton_RotateZ.setCheckable(False)

        self.gridLayout_3.addWidget(self.pushButton_RotateZ, 4, 0, 1, 1)

        self.buttonClimbBackward = QPushButton(self.groupBox_Control)
        self.buttonClimbBackward.setObjectName(u"buttonClimbBackward")
        self.buttonClimbBackward.setMinimumSize(QSize(50, 50))
        self.buttonClimbBackward.setMaximumSize(QSize(50, 50))
        icon4 = QIcon()
        icon4.addFile(u"res/climb-down-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonClimbBackward.setIcon(icon4)
        self.buttonClimbBackward.setIconSize(QSize(32, 32))
        self.buttonClimbBackward.setCheckable(False)

        self.gridLayout_3.addWidget(self.buttonClimbBackward, 4, 1, 1, 1)

        self.buttonClimbForward = QPushButton(self.groupBox_Control)
        self.buttonClimbForward.setObjectName(u"buttonClimbForward")
        self.buttonClimbForward.setMinimumSize(QSize(50, 50))
        self.buttonClimbForward.setMaximumSize(QSize(50, 50))
        icon5 = QIcon()
        icon5.addFile(u"res/climb-up-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonClimbForward.setIcon(icon5)
        self.buttonClimbForward.setIconSize(QSize(32, 32))
        self.buttonClimbForward.setCheckable(False)

        self.gridLayout_3.addWidget(self.buttonClimbForward, 2, 1, 1, 1)

        self.pushButton_RotateX = QPushButton(self.groupBox_Control)
        self.pushButton_RotateX.setObjectName(u"pushButton_RotateX")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_RotateX.sizePolicy().hasHeightForWidth())
        self.pushButton_RotateX.setSizePolicy(sizePolicy2)
        self.pushButton_RotateX.setMinimumSize(QSize(50, 50))
        self.pushButton_RotateX.setMaximumSize(QSize(50, 50))
        icon6 = QIcon()
        icon6.addFile(u"res/arrow-up-down-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_RotateX.setIcon(icon6)
        self.pushButton_RotateX.setIconSize(QSize(32, 32))
        self.pushButton_RotateX.setCheckable(False)

        self.gridLayout_3.addWidget(self.pushButton_RotateX, 3, 0, 1, 1)

        self.pushButton_RotateY = QPushButton(self.groupBox_Control)
        self.pushButton_RotateY.setObjectName(u"pushButton_RotateY")
        self.pushButton_RotateY.setMinimumSize(QSize(50, 50))
        self.pushButton_RotateY.setMaximumSize(QSize(50, 50))
        icon7 = QIcon()
        icon7.addFile(u"res/arrow-left-right-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_RotateY.setIcon(icon7)
        self.pushButton_RotateY.setIconSize(QSize(32, 32))
        self.pushButton_RotateY.setCheckable(False)

        self.gridLayout_3.addWidget(self.pushButton_RotateY, 2, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(12)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonShiftRight = QPushButton(self.groupBox_Control)
        self.buttonShiftRight.setObjectName(u"buttonShiftRight")
        sizePolicy2.setHeightForWidth(self.buttonShiftRight.sizePolicy().hasHeightForWidth())
        self.buttonShiftRight.setSizePolicy(sizePolicy2)
        self.buttonShiftRight.setMinimumSize(QSize(50, 50))
        self.buttonShiftRight.setMaximumSize(QSize(50, 50))
        icon8 = QIcon()
        icon8.addFile(u"res/arrow-right-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonShiftRight.setIcon(icon8)
        self.buttonShiftRight.setCheckable(False)

        self.gridLayout.addWidget(self.buttonShiftRight, 3, 3, 1, 1)

        self.buttonTurnLeft = QPushButton(self.groupBox_Control)
        self.buttonTurnLeft.setObjectName(u"buttonTurnLeft")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.buttonTurnLeft.sizePolicy().hasHeightForWidth())
        self.buttonTurnLeft.setSizePolicy(sizePolicy3)
        self.buttonTurnLeft.setMinimumSize(QSize(40, 150))
        icon9 = QIcon()
        icon9.addFile(u"res/arrow-turn-left-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonTurnLeft.setIcon(icon9)
        self.buttonTurnLeft.setIconSize(QSize(24, 64))
        self.buttonTurnLeft.setCheckable(False)

        self.gridLayout.addWidget(self.buttonTurnLeft, 2, 0, 3, 1)

        self.buttonBackward = QPushButton(self.groupBox_Control)
        self.buttonBackward.setObjectName(u"buttonBackward")
        sizePolicy2.setHeightForWidth(self.buttonBackward.sizePolicy().hasHeightForWidth())
        self.buttonBackward.setSizePolicy(sizePolicy2)
        self.buttonBackward.setMinimumSize(QSize(50, 50))
        self.buttonBackward.setMaximumSize(QSize(50, 50))
        icon10 = QIcon()
        icon10.addFile(u"res/arrow-down-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonBackward.setIcon(icon10)
        self.buttonBackward.setCheckable(False)

        self.gridLayout.addWidget(self.buttonBackward, 4, 2, 1, 1)

        self.buttonRight135 = QPushButton(self.groupBox_Control)
        self.buttonRight135.setObjectName(u"buttonRight135")
        sizePolicy2.setHeightForWidth(self.buttonRight135.sizePolicy().hasHeightForWidth())
        self.buttonRight135.setSizePolicy(sizePolicy2)
        self.buttonRight135.setMinimumSize(QSize(50, 50))
        self.buttonRight135.setMaximumSize(QSize(50, 50))
        icon11 = QIcon()
        icon11.addFile(u"res/arrow-down-right-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonRight135.setIcon(icon11)
        self.buttonRight135.setCheckable(False)

        self.gridLayout.addWidget(self.buttonRight135, 4, 3, 1, 1)

        self.buttonLeft135 = QPushButton(self.groupBox_Control)
        self.buttonLeft135.setObjectName(u"buttonLeft135")
        sizePolicy2.setHeightForWidth(self.buttonLeft135.sizePolicy().hasHeightForWidth())
        self.buttonLeft135.setSizePolicy(sizePolicy2)
        self.buttonLeft135.setMinimumSize(QSize(50, 50))
        self.buttonLeft135.setMaximumSize(QSize(50, 50))
        icon12 = QIcon()
        icon12.addFile(u"res/arrow-down-left-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonLeft135.setIcon(icon12)
        self.buttonLeft135.setCheckable(False)

        self.gridLayout.addWidget(self.buttonLeft135, 4, 1, 1, 1)

        self.buttonTurnRight = QPushButton(self.groupBox_Control)
        self.buttonTurnRight.setObjectName(u"buttonTurnRight")
        self.buttonTurnRight.setMinimumSize(QSize(40, 150))
        icon13 = QIcon()
        icon13.addFile(u"res/arrow-turn-right-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonTurnRight.setIcon(icon13)
        self.buttonTurnRight.setIconSize(QSize(24, 64))
        self.buttonTurnRight.setCheckable(False)

        self.gridLayout.addWidget(self.buttonTurnRight, 2, 4, 3, 1)

        self.buttonRight45 = QPushButton(self.groupBox_Control)
        self.buttonRight45.setObjectName(u"buttonRight45")
        self.buttonRight45.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.buttonRight45.sizePolicy().hasHeightForWidth())
        self.buttonRight45.setSizePolicy(sizePolicy2)
        self.buttonRight45.setMinimumSize(QSize(50, 50))
        self.buttonRight45.setMaximumSize(QSize(50, 50))
        icon14 = QIcon()
        icon14.addFile(u"res/arrow-up-right-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonRight45.setIcon(icon14)
        self.buttonRight45.setCheckable(False)

        self.gridLayout.addWidget(self.buttonRight45, 2, 3, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.buttonFastForward = QPushButton(self.groupBox_Control)
        self.buttonFastForward.setObjectName(u"buttonFastForward")
        self.buttonFastForward.setMinimumSize(QSize(150, 40))
        self.buttonFastForward.setMaximumSize(QSize(150, 16777215))
        icon15 = QIcon()
        icon15.addFile(u"res/arrow-up-up-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonFastForward.setIcon(icon15)
        self.buttonFastForward.setIconSize(QSize(24, 24))
        self.buttonFastForward.setCheckable(False)
        self.buttonFastForward.setChecked(False)
        self.buttonFastForward.setFlat(False)

        self.horizontalLayout_2.addWidget(self.buttonFastForward)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 3)

        self.buttonStandby = QPushButton(self.groupBox_Control)
        self.buttonStandby.setObjectName(u"buttonStandby")
        sizePolicy2.setHeightForWidth(self.buttonStandby.sizePolicy().hasHeightForWidth())
        self.buttonStandby.setSizePolicy(sizePolicy2)
        self.buttonStandby.setMinimumSize(QSize(50, 50))
        self.buttonStandby.setMaximumSize(QSize(50, 50))
        icon16 = QIcon()
        icon16.addFile(u"res/pause-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonStandby.setIcon(icon16)
        self.buttonStandby.setCheckable(False)
        self.buttonStandby.setChecked(False)

        self.gridLayout.addWidget(self.buttonStandby, 3, 2, 1, 1)

        self.buttonShiftLeft = QPushButton(self.groupBox_Control)
        self.buttonShiftLeft.setObjectName(u"buttonShiftLeft")
        sizePolicy2.setHeightForWidth(self.buttonShiftLeft.sizePolicy().hasHeightForWidth())
        self.buttonShiftLeft.setSizePolicy(sizePolicy2)
        self.buttonShiftLeft.setMinimumSize(QSize(50, 50))
        self.buttonShiftLeft.setMaximumSize(QSize(50, 50))
        icon17 = QIcon()
        icon17.addFile(u"res/arrow-left-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonShiftLeft.setIcon(icon17)
        self.buttonShiftLeft.setCheckable(False)

        self.gridLayout.addWidget(self.buttonShiftLeft, 3, 1, 1, 1)

        self.buttonLeft45 = QPushButton(self.groupBox_Control)
        self.buttonLeft45.setObjectName(u"buttonLeft45")
        sizePolicy2.setHeightForWidth(self.buttonLeft45.sizePolicy().hasHeightForWidth())
        self.buttonLeft45.setSizePolicy(sizePolicy2)
        self.buttonLeft45.setMinimumSize(QSize(50, 50))
        self.buttonLeft45.setMaximumSize(QSize(50, 50))
        icon18 = QIcon()
        icon18.addFile(u"res/arrow-up-left-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonLeft45.setIcon(icon18)
        self.buttonLeft45.setCheckable(False)

        self.gridLayout.addWidget(self.buttonLeft45, 2, 1, 1, 1)

        self.buttonForward = QPushButton(self.groupBox_Control)
        self.buttonForward.setObjectName(u"buttonForward")
        sizePolicy2.setHeightForWidth(self.buttonForward.sizePolicy().hasHeightForWidth())
        self.buttonForward.setSizePolicy(sizePolicy2)
        self.buttonForward.setMinimumSize(QSize(50, 50))
        self.buttonForward.setMaximumSize(QSize(50, 50))
        icon19 = QIcon()
        icon19.addFile(u"res/arrow-up-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonForward.setIcon(icon19)
        self.buttonForward.setCheckable(False)

        self.gridLayout.addWidget(self.buttonForward, 2, 2, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.buttonFastBackward = QPushButton(self.groupBox_Control)
        self.buttonFastBackward.setObjectName(u"buttonFastBackward")
        self.buttonFastBackward.setMinimumSize(QSize(0, 40))
        self.buttonFastBackward.setMaximumSize(QSize(150, 16777215))
        icon20 = QIcon()
        icon20.addFile(u"res/arrow-down-down-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.buttonFastBackward.setIcon(icon20)
        self.buttonFastBackward.setIconSize(QSize(24, 24))
        self.buttonFastBackward.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.buttonFastBackward)


        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 1, 1, 3)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.groupBox_Control)

        self.groupBox = QGroupBox(self.centralWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textBrowserMessage = QTextBrowser(self.groupBox)
        self.textBrowserMessage.setObjectName(u"textBrowserMessage")

        self.verticalLayout_2.addWidget(self.textBrowserMessage)


        self.verticalLayout.addWidget(self.groupBox)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 587, 19))
        MainWindow.setMenuBar(self.menuBar)
        self.status_bar = QStatusBar(MainWindow)
        self.status_bar.setObjectName(u"status_bar")
        MainWindow.setStatusBar(self.status_bar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.buttonLayDown.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Hexapod", None))
        self.button_Refresh.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"IP: ", None))
        self.label_LocalIP.setText(QCoreApplication.translate("MainWindow", u"255.255.255.255", None))
        self.label_targetIP.setText(QCoreApplication.translate("MainWindow", u"Robot IP:", None))
        self.label_targetPort.setText(QCoreApplication.translate("MainWindow", u"Port:", None))
        self.buttonTcpConnect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"WiFi", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Robot MAC:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Port:", None))
        self.buttonBtConnect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Bluetooth", None))
        self.groupBox_Control.setTitle(QCoreApplication.translate("MainWindow", u"Control", None))
        self.pushButton_Twist.setText("")
        self.pushButton_7.setText("")
        self.buttonLayDown.setText(QCoreApplication.translate("MainWindow", u"LayDown", None))
        self.pushButton_RotateZ.setText("")
        self.buttonClimbBackward.setText("")
        self.buttonClimbForward.setText("")
        self.pushButton_RotateX.setText("")
        self.pushButton_RotateY.setText("")
        self.buttonShiftRight.setText("")
        self.buttonTurnLeft.setText("")
        self.buttonBackward.setText("")
        self.buttonRight135.setText("")
        self.buttonLeft135.setText("")
        self.buttonTurnRight.setText("")
        self.buttonRight45.setText("")
        self.buttonFastForward.setText("")
        self.buttonStandby.setText("")
        self.buttonShiftLeft.setText("")
        self.buttonLeft45.setText("")
        self.buttonForward.setText("")
        self.buttonFastBackward.setText("")
        self.groupBox.setTitle("")
    # retranslateUi

