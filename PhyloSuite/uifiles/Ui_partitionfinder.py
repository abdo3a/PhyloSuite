# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Work\python\bioinfo_excercise\PhyloSuite\PhyloSuite\PhyloSuite\uifiles\partitionfinder.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PartitionFinder(object):
    def setupUi(self, PartitionFinder):
        PartitionFinder.setObjectName("PartitionFinder")
        PartitionFinder.resize(528, 531)
        self.gridLayout_9 = QtWidgets.QGridLayout(PartitionFinder)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.groupBox_6 = QtWidgets.QGroupBox(PartitionFinder)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_11 = QtWidgets.QLabel(self.groupBox_6)
        self.label_11.setObjectName("label_11")
        self.gridLayout_7.addWidget(self.label_11, 0, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_6)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_7.addWidget(self.progressBar, 1, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_6)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/picture/resourses/Eye_Care_Services-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_7.addWidget(self.pushButton_9, 2, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_6, 3, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(PartitionFinder)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_5)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/picture/resourses/gears.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_8.addWidget(self.pushButton_7, 0, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_5)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/picture/resourses/terminal-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_8.addWidget(self.pushButton_8, 0, 1, 1, 1)
        self.pushButton_5 = ArrowPushButton(self.groupBox_5)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/picture/resourses/if_start_60207.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_8.addWidget(self.pushButton_5, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_5)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/picture/resourses/if_Delete_1493279.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_8.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.gridLayout_8.setColumnStretch(0, 1)
        self.gridLayout_8.setColumnStretch(1, 1)
        self.gridLayout_9.addWidget(self.groupBox_5, 2, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(PartitionFinder)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineEdit = InputQLineEdit(self.groupBox_4)
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit.setText("")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(30, 26))
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 26))
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.lineEdit_2 = InputQLineEdit(self.groupBox_4)
        self.lineEdit_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(30, 26))
        self.pushButton_4.setMaximumSize(QtCore.QSize(30, 26))
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setOpenExternalLinks(True)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout.addWidget(self.label_14)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_12 = ClickedLableGif(self.groupBox_4)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout.addWidget(self.label_12)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 3)
        self.gridLayout_9.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(PartitionFinder)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(2, 4, 2, 2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_6.setContentsMargins(5, 2, 2, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_6.addWidget(self.comboBox, 0, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.toolButton = QtWidgets.QToolButton(self.groupBox_2)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/picture/resourses/interface-controls-text-wrap-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon5)
        self.toolButton.setCheckable(True)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout_4.addWidget(self.toolButton, 0, 3, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_4.addWidget(self.textEdit, 1, 0, 1, 4)
        spacerItem1 = QtWidgets.QSpacerItem(123, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 1, 1, 1)
        self.toolButton_cvt = QtWidgets.QToolButton(self.groupBox_2)
        self.toolButton_cvt.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/picture/resourses/converter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_cvt.setIcon(icon6)
        self.toolButton_cvt.setObjectName("toolButton_cvt")
        self.gridLayout_4.addWidget(self.toolButton_cvt, 0, 2, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_2, 0, 2, 5, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 1, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_6.addWidget(self.comboBox_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 2, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout_6.addWidget(self.comboBox_3, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_6.addWidget(self.label_5, 3, 0, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout_6.addWidget(self.comboBox_4, 3, 1, 1, 1)
        self.pushButton_cmd1 = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_cmd1.sizePolicy().hasHeightForWidth())
        self.pushButton_cmd1.setSizePolicy(sizePolicy)
        self.pushButton_cmd1.setIcon(icon2)
        self.pushButton_cmd1.setObjectName("pushButton_cmd1")
        self.gridLayout_6.addWidget(self.pushButton_cmd1, 4, 0, 1, 2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setContentsMargins(5, 2, 2, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_6.sizePolicy().hasHeightForWidth())
        self.comboBox_6.setSizePolicy(sizePolicy)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_6, 0, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(230, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem2, 0, 0, 1, 1)
        self.toolButton_2 = QtWidgets.QToolButton(self.groupBox_3)
        self.toolButton_2.setIcon(icon5)
        self.toolButton_2.setCheckable(True)
        self.toolButton_2.setObjectName("toolButton_2")
        self.gridLayout_5.addWidget(self.toolButton_2, 0, 1, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit_2.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout_5.addWidget(self.textEdit_2, 1, 0, 1, 2)
        self.gridLayout_3.addWidget(self.groupBox_3, 0, 2, 5, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)
        self.comboBox_8 = QtWidgets.QComboBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_8.sizePolicy().hasHeightForWidth())
        self.comboBox_8.setSizePolicy(sizePolicy)
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_8, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 2, 0, 1, 1)
        self.comboBox_7 = QtWidgets.QComboBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_7.sizePolicy().hasHeightForWidth())
        self.comboBox_7.setSizePolicy(sizePolicy)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_7, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 3, 0, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_5.sizePolicy().hasHeightForWidth())
        self.comboBox_5.setSizePolicy(sizePolicy)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_5, 3, 1, 1, 1)
        self.pushButton_cmd2 = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_cmd2.sizePolicy().hasHeightForWidth())
        self.pushButton_cmd2.setSizePolicy(sizePolicy)
        self.pushButton_cmd2.setIcon(icon2)
        self.pushButton_cmd2.setObjectName("pushButton_cmd2")
        self.gridLayout_3.addWidget(self.pushButton_cmd2, 4, 0, 1, 2)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox, 1, 0, 1, 1)

        self.retranslateUi(PartitionFinder)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(PartitionFinder)
        PartitionFinder.setTabOrder(self.pushButton_5, self.lineEdit_2)
        PartitionFinder.setTabOrder(self.lineEdit_2, self.tabWidget)
        PartitionFinder.setTabOrder(self.tabWidget, self.pushButton_7)
        PartitionFinder.setTabOrder(self.pushButton_7, self.pushButton_4)
        PartitionFinder.setTabOrder(self.pushButton_4, self.lineEdit)
        PartitionFinder.setTabOrder(self.lineEdit, self.pushButton_8)
        PartitionFinder.setTabOrder(self.pushButton_8, self.pushButton_3)
        PartitionFinder.setTabOrder(self.pushButton_3, self.pushButton_2)
        PartitionFinder.setTabOrder(self.pushButton_2, self.pushButton_9)
        PartitionFinder.setTabOrder(self.pushButton_9, self.comboBox)
        PartitionFinder.setTabOrder(self.comboBox, self.textEdit)
        PartitionFinder.setTabOrder(self.textEdit, self.comboBox_2)
        PartitionFinder.setTabOrder(self.comboBox_2, self.comboBox_3)
        PartitionFinder.setTabOrder(self.comboBox_3, self.comboBox_4)
        PartitionFinder.setTabOrder(self.comboBox_4, self.pushButton_cmd1)
        PartitionFinder.setTabOrder(self.pushButton_cmd1, self.comboBox_6)
        PartitionFinder.setTabOrder(self.comboBox_6, self.textEdit_2)
        PartitionFinder.setTabOrder(self.textEdit_2, self.comboBox_8)
        PartitionFinder.setTabOrder(self.comboBox_8, self.comboBox_7)
        PartitionFinder.setTabOrder(self.comboBox_7, self.comboBox_5)
        PartitionFinder.setTabOrder(self.comboBox_5, self.pushButton_cmd2)

    def retranslateUi(self, PartitionFinder):
        _translate = QtCore.QCoreApplication.translate
        PartitionFinder.setWindowTitle(_translate("PartitionFinder", "PartitionFinder"))
        self.groupBox_6.setTitle(_translate("PartitionFinder", "Progress"))
        self.label_11.setText(_translate("PartitionFinder", "PartitionFinder analysis"))
        self.pushButton_9.setText(_translate("PartitionFinder", "Show log"))
        self.groupBox_5.setTitle(_translate("PartitionFinder", "Run"))
        self.pushButton_7.setText(_translate("PartitionFinder", "Show configuration"))
        self.pushButton_8.setText(_translate("PartitionFinder", "Show command"))
        self.pushButton_5.setText(_translate("PartitionFinder", "Start"))
        self.pushButton_2.setText(_translate("PartitionFinder", "Stop"))
        self.groupBox_4.setTitle(_translate("PartitionFinder", "Input"))
        self.label_4.setText(_translate("PartitionFinder", "Alignment File:"))
        self.lineEdit.setPlaceholderText(_translate("PartitionFinder", "The alignment should be phylip format"))
        self.label_6.setText(_translate("PartitionFinder", "Tree File:"))
        self.lineEdit_2.setPlaceholderText(_translate("PartitionFinder", "Optional! (in newick format)"))
        self.label_14.setText(_translate("PartitionFinder", "<html><head/><body><p>Click <a href=\"http://www.robertlanfear.com/partitionfinder/\"><span style=\" text-decoration: underline; color:#0000ff;\">here</span></a> to learn more about <span style=\" font-weight:600; color:#ff0000;\">PartitionFinder2</span></p></body></html>"))
        self.label_12.setToolTip(_translate("PartitionFinder", "Brief example"))
        self.groupBox.setTitle(_translate("PartitionFinder", "Configuration"))
        self.label.setText(_translate("PartitionFinder", "branchlengths = "))
        self.comboBox.setItemText(0, _translate("PartitionFinder", "linked"))
        self.comboBox.setItemText(1, _translate("PartitionFinder", "unlinked"))
        self.groupBox_2.setTitle(_translate("PartitionFinder", "DATA BLOCKS"))
        self.toolButton.setToolTip(_translate("PartitionFinder", "Use Wraps"))
        self.toolButton.setText(_translate("PartitionFinder", "..."))
        self.textEdit.setToolTip(_translate("PartitionFinder", "For example:\n"
"atp6 = 1-693;\n"
"atp8 = 694-882;\n"
"cox1 = 883-2475;\n"
"cox2 = 2476-3225;\n"
"cox3 = 3226-4089;"))
        self.toolButton_cvt.setToolTip(_translate("PartitionFinder", "Codon Converter"))
        self.label_2.setText(_translate("PartitionFinder", "models = "))
        self.comboBox_2.setItemText(0, _translate("PartitionFinder", "all"))
        self.comboBox_2.setItemText(1, _translate("PartitionFinder", "allx"))
        self.comboBox_2.setItemText(2, _translate("PartitionFinder", "beast"))
        self.comboBox_2.setItemText(3, _translate("PartitionFinder", "mrbayes"))
        self.comboBox_2.setItemText(4, _translate("PartitionFinder", "gamma"))
        self.comboBox_2.setItemText(5, _translate("PartitionFinder", "gammai"))
        self.comboBox_2.setItemText(6, _translate("PartitionFinder", "<list>"))
        self.label_3.setText(_translate("PartitionFinder", "model_selection = "))
        self.comboBox_3.setItemText(0, _translate("PartitionFinder", "AICc"))
        self.comboBox_3.setItemText(1, _translate("PartitionFinder", "BIC"))
        self.comboBox_3.setItemText(2, _translate("PartitionFinder", "AIC"))
        self.label_5.setText(_translate("PartitionFinder", "search = "))
        self.comboBox_4.setItemText(0, _translate("PartitionFinder", "all"))
        self.comboBox_4.setItemText(1, _translate("PartitionFinder", "greedy"))
        self.comboBox_4.setItemText(2, _translate("PartitionFinder", "rcluster"))
        self.comboBox_4.setItemText(3, _translate("PartitionFinder", "rclusterf"))
        self.comboBox_4.setItemText(4, _translate("PartitionFinder", "hcluster"))
        self.comboBox_4.setItemText(5, _translate("PartitionFinder", "kmeans"))
        self.comboBox_4.setItemText(6, _translate("PartitionFinder", "user define"))
        self.pushButton_cmd1.setText(_translate("PartitionFinder", "Command line options"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("PartitionFinder", "Nucleotide"))
        self.label_10.setText(_translate("PartitionFinder", "branchlengths = "))
        self.comboBox_6.setItemText(0, _translate("PartitionFinder", "linked"))
        self.comboBox_6.setItemText(1, _translate("PartitionFinder", "unlinked"))
        self.groupBox_3.setTitle(_translate("PartitionFinder", "DATA BLOCKS"))
        self.toolButton_2.setToolTip(_translate("PartitionFinder", "Use Wraps"))
        self.toolButton_2.setText(_translate("PartitionFinder", "..."))
        self.textEdit_2.setToolTip(_translate("PartitionFinder", "For example:\n"
"COI     =   1-407;\n"
"COII    =   408-624;\n"
"EF1a    =   625-949;"))
        self.label_7.setText(_translate("PartitionFinder", "models = "))
        self.comboBox_8.setItemText(0, _translate("PartitionFinder", "all"))
        self.comboBox_8.setItemText(1, _translate("PartitionFinder", "allx"))
        self.comboBox_8.setItemText(2, _translate("PartitionFinder", "beast"))
        self.comboBox_8.setItemText(3, _translate("PartitionFinder", "mrbayes"))
        self.comboBox_8.setItemText(4, _translate("PartitionFinder", "gamma"))
        self.comboBox_8.setItemText(5, _translate("PartitionFinder", "gammai"))
        self.comboBox_8.setItemText(6, _translate("PartitionFinder", "<list>"))
        self.label_8.setText(_translate("PartitionFinder", "model_selection = "))
        self.comboBox_7.setItemText(0, _translate("PartitionFinder", "AICc"))
        self.comboBox_7.setItemText(1, _translate("PartitionFinder", "BIC"))
        self.comboBox_7.setItemText(2, _translate("PartitionFinder", "AIC"))
        self.label_9.setText(_translate("PartitionFinder", "search = "))
        self.comboBox_5.setItemText(0, _translate("PartitionFinder", "all"))
        self.comboBox_5.setItemText(1, _translate("PartitionFinder", "greedy"))
        self.comboBox_5.setItemText(2, _translate("PartitionFinder", "rcluster"))
        self.comboBox_5.setItemText(3, _translate("PartitionFinder", "rclusterf"))
        self.comboBox_5.setItemText(4, _translate("PartitionFinder", "hcluster"))
        self.comboBox_5.setItemText(5, _translate("PartitionFinder", "kmeans"))
        self.comboBox_5.setItemText(6, _translate("PartitionFinder", "user define"))
        self.pushButton_cmd2.setText(_translate("PartitionFinder", "Command line options"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("PartitionFinder", "Amino acid"))

from src.CustomWidget import ArrowPushButton, ClickedLableGif, InputQLineEdit
from uifiles import myRes_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PartitionFinder = QtWidgets.QDialog()
    ui = Ui_PartitionFinder()
    ui.setupUi(PartitionFinder)
    PartitionFinder.show()
    sys.exit(app.exec_())
