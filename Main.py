# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1319, 717)
        MainWindow.setMinimumSize(QtCore.QSize(0, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("#import_2 {\n"
"  background-color: white; \n"
"  color: black; \n"
"  border: 2px solid #4CAF50;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#import_2:hover {\n"
" background-color: #38ff7d;\n"
"  color: white;\n"
"\n"
"}\n"
"#import_2:pressed{\n"
"background-color: #38ef7d;\n"
"  color: white;\n"
"  border: 2px solid #4CAF50;\n"
"}\n"
"#export_2 {\n"
"  background-color: white; \n"
"  color: black; \n"
"  border: 2px solid #4CAF50;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"#export_2:hover {\n"
" background-color: #38ff7d;\n"
"  color: white;\n"
"\n"
"}\n"
"#export_2:pressed{\n"
"background-color: #38ef7d;\n"
"  color: white;\n"
"  border: 2px solid #4CAF50;\n"
"}\n"
"#search{\n"
"background-color: white;\n"
"border: 1px solid #d7d7d7;\n"
"}\n"
"#search_2{\n"
"background-color: white;\n"
"border: 1px solid #d7d7d7;\n"
"}\n"
"\n"
"#search_edit{\n"
"border: 1px solid #d7d7d7;\n"
"}\n"
"#search_edit_2{\n"
"border: 1px solid #d7d7d7;\n"
"}\n"
"#progressBar{\n"
"border: 1px solid black;\n"
"text-align: center\n"
"}\n"
"#progressBar::chunk {\n"
"    background-color: lightblue;\n"
"}\n"
"#progressBar2{\n"
"border: 1px solid black;\n"
"text-align: center\n"
"}\n"
"#progressBar2::chunk {\n"
"    background-color: lightblue;\n"
"}\n"
"#groupBox{\n"
"background-color: #e0ece4;\n"
"border-radius: 5px;\n"
"border: 2px solid #84a9ac;\n"
"}\n"
"#jami{\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"}\n"
"#table_box{\n"
"border-radius: 10px;\n"
"background-color: #d3dbff;\n"
"border: 3px solid lightgray;\n"
"}\n"
"#property{\n"
"background-color: #ebecf1;\n"
"border: 2px solid #ababf1;\n"
"border-radius: 8px;\n"
"}")
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setMinimumSize(QtCore.QSize(35, 35))
        self.search.setMaximumSize(QtCore.QSize(35, 35))
        self.search.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/search_icon1.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.search.setIcon(icon1)
        self.search.setIconSize(QtCore.QSize(30, 30))
        self.search.setObjectName("search")
        self.horizontalLayout.addWidget(self.search)
        self.search_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.search_edit.setMinimumSize(QtCore.QSize(0, 35))
        self.search_edit.setMaximumSize(QtCore.QSize(250, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.search_edit.setFont(font)
        self.search_edit.setStyleSheet("QLineEdit::focus{\n"
"border: 2px solid #8181ff;\n"
"}")
        self.search_edit.setInputMethodHints(QtCore.Qt.ImhFormattedNumbersOnly)
        self.search_edit.setText("")
        self.search_edit.setObjectName("search_edit")
        self.horizontalLayout.addWidget(self.search_edit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.search_2 = QtWidgets.QPushButton(self.centralwidget)
        self.search_2.setMinimumSize(QtCore.QSize(35, 35))
        self.search_2.setMaximumSize(QtCore.QSize(35, 35))
        self.search_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/search_icon2.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.search_2.setIcon(icon2)
        self.search_2.setIconSize(QtCore.QSize(30, 30))
        self.search_2.setObjectName("search_2")
        self.gridLayout_10.addWidget(self.search_2, 0, 0, 1, 1)
        self.search_edit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.search_edit_2.setMinimumSize(QtCore.QSize(0, 35))
        self.search_edit_2.setMaximumSize(QtCore.QSize(250, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.search_edit_2.setFont(font)
        self.search_edit_2.setStyleSheet("QLineEdit::focus{\n"
"border: 2px solid #8181ff;\n"
"}")
        self.search_edit_2.setObjectName("search_edit_2")
        self.gridLayout_10.addWidget(self.search_edit_2, 0, 1, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout_10)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 2, 1, 1)
        self.horizontalLayout_7.addLayout(self.gridLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 30))
        self.progressBar.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_7.addWidget(self.progressBar)
        spacerItem2 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.import_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.import_2.sizePolicy().hasHeightForWidth())
        self.import_2.setSizePolicy(sizePolicy)
        self.import_2.setMinimumSize(QtCore.QSize(0, 40))
        self.import_2.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.import_2.setFont(font)
        self.import_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/export.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.import_2.setIcon(icon3)
        self.import_2.setIconSize(QtCore.QSize(32, 32))
        self.import_2.setObjectName("import_2")
        self.horizontalLayout_7.addWidget(self.import_2)
        spacerItem3 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.progressBar2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar2.setMinimumSize(QtCore.QSize(0, 30))
        self.progressBar2.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.progressBar2.setFont(font)
        self.progressBar2.setProperty("value", 0)
        self.progressBar2.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar2.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar2.setObjectName("progressBar2")
        self.horizontalLayout_7.addWidget(self.progressBar2)
        spacerItem4 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.export_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.export_2.sizePolicy().hasHeightForWidth())
        self.export_2.setSizePolicy(sizePolicy)
        self.export_2.setMinimumSize(QtCore.QSize(0, 40))
        self.export_2.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.export_2.setFont(font)
        self.export_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icons/fgdwfs.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.export_2.setIcon(icon4)
        self.export_2.setIconSize(QtCore.QSize(32, 32))
        self.export_2.setObjectName("export_2")
        self.horizontalLayout_7.addWidget(self.export_2)
        spacerItem5 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.mix = QtWidgets.QPushButton(self.centralwidget)
        self.mix.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mix.setStyleSheet("QPushButton {\n"
"  background-color: white; \n"
"  color: black; \n"
"border: 2px solid #4CAF50;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
" background-color: #38ff7d;\n"
"  color: white;\n"
"\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #38ef7d;\n"
"  color: white;\n"
"\n"
"}")
        self.mix.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.mix.setIcon(icon5)
        self.mix.setIconSize(QtCore.QSize(22, 22))
        self.mix.setObjectName("mix")
        self.horizontalLayout_7.addWidget(self.mix)
        self.gridLayout_5.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.table_box = QtWidgets.QGroupBox(self.centralwidget)
        self.table_box.setTitle("")
        self.table_box.setObjectName("table_box")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.table_box)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem6 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_7.addItem(spacerItem6, 1, 0, 1, 1)
        self.filtered = QtWidgets.QTableWidget(self.table_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filtered.sizePolicy().hasHeightForWidth())
        self.filtered.setSizePolicy(sizePolicy)
        self.filtered.setMinimumSize(QtCore.QSize(0, 550))
        self.filtered.setMaximumSize(QtCore.QSize(666666, 666666))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.filtered.setFont(font)
        self.filtered.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.filtered.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.filtered.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.filtered.setAutoFillBackground(True)
        self.filtered.setStyleSheet("::section{background-color: #efefef;}\n"
"::item:selected { color:white; background:#01a9b4; font-weight:900; }\n"
"QTableCornerButton::section { background-color:#f4f6ff;border-radius: 1px; }")
        self.filtered.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.filtered.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.filtered.setAlternatingRowColors(True)
        self.filtered.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.filtered.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.filtered.setTextElideMode(QtCore.Qt.ElideLeft)
        self.filtered.setRowCount(10)
        self.filtered.setObjectName("filtered")
        self.filtered.setColumnCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.filtered.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        item.setFont(font)
        self.filtered.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        item.setFont(font)
        self.filtered.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        item.setFont(font)
        self.filtered.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        item.setFont(font)
        self.filtered.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        item.setFont(font)
        self.filtered.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        item.setFont(font)
        self.filtered.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.filtered.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.filtered.setHorizontalHeaderItem(8, item)
        self.filtered.horizontalHeader().setCascadingSectionResizes(False)
        self.filtered.horizontalHeader().setDefaultSectionSize(180)
        self.filtered.horizontalHeader().setHighlightSections(False)
        self.filtered.horizontalHeader().setSortIndicatorShown(False)
        self.filtered.horizontalHeader().setStretchLastSection(True)
        self.filtered.verticalHeader().setVisible(True)
        self.filtered.verticalHeader().setCascadingSectionResizes(False)
        self.filtered.verticalHeader().setHighlightSections(True)
        self.filtered.verticalHeader().setSortIndicatorShown(False)
        self.filtered.verticalHeader().setStretchLastSection(False)
        self.gridLayout_7.addWidget(self.filtered, 0, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_7, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.status = QtWidgets.QLabel(self.table_box)
        self.status.setMinimumSize(QtCore.QSize(0, 30))
        self.status.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.status.setFont(font)
        self.status.setObjectName("status")
        self.horizontalLayout_4.addWidget(self.status)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.gridLayout_6.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_6.addWidget(self.table_box)
        spacerItem9 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.property = QtWidgets.QGroupBox(self.centralwidget)
        self.property.setMinimumSize(QtCore.QSize(290, 0))
        self.property.setMaximumSize(QtCore.QSize(290, 16777215))
        self.property.setTitle("")
        self.property.setObjectName("property")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.property)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_4 = QtWidgets.QLabel(self.property)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.narx = QtWidgets.QLineEdit(self.property)
        self.narx.setMinimumSize(QtCore.QSize(160, 30))
        self.narx.setMaximumSize(QtCore.QSize(160, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.narx.setFont(font)
        self.narx.setStyleSheet("QLineEdit{\n"
"border-radius: 8px;\n"
"border: 1px solid black;\n"
"}\n"
"QLineEdit::focus{\n"
"border: 2px solid #8181ff;\n"
"}")
        self.narx.setObjectName("narx")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.narx)
        self.verticalLayout_2.addLayout(self.formLayout_5)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_5 = QtWidgets.QLabel(self.property)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.qadoq = QtWidgets.QLineEdit(self.property)
        self.qadoq.setMinimumSize(QtCore.QSize(160, 30))
        self.qadoq.setMaximumSize(QtCore.QSize(160, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.qadoq.setFont(font)
        self.qadoq.setStyleSheet("QLineEdit{\n"
"border-radius: 8px;\n"
"border: 1px solid black;\n"
"}\n"
"QLineEdit::focus{\n"
"border: 2px solid #8181ff;\n"
"}")
        self.qadoq.setObjectName("qadoq")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.qadoq)
        self.verticalLayout_2.addLayout(self.formLayout_4)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_6 = QtWidgets.QLabel(self.property)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.soni = QtWidgets.QLineEdit(self.property)
        self.soni.setMinimumSize(QtCore.QSize(160, 30))
        self.soni.setMaximumSize(QtCore.QSize(160, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.soni.setFont(font)
        self.soni.setStyleSheet("QLineEdit{\n"
"border-radius: 8px;\n"
"border: 1px solid black;\n"
"}\n"
"QLineEdit::focus{\n"
"border: 2px solid #8181ff;\n"
"}")
        self.soni.setObjectName("soni")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.soni)
        self.verticalLayout_2.addLayout(self.formLayout_3)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_7 = QtWidgets.QLabel(self.property)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.summa = QtWidgets.QLineEdit(self.property)
        self.summa.setMinimumSize(QtCore.QSize(160, 30))
        self.summa.setMaximumSize(QtCore.QSize(160, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.summa.setFont(font)
        self.summa.setStyleSheet("border-radius: 8px;\n"
"border: 1px solid black;")
        self.summa.setReadOnly(True)
        self.summa.setObjectName("summa")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.summa)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.delete_1 = QtWidgets.QPushButton(self.property)
        self.delete_1.setMinimumSize(QtCore.QSize(100, 40))
        self.delete_1.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        self.delete_1.setFont(font)
        self.delete_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_1.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
"border: 2px solid #fa1616;\n"
"background-color: white;\n"
"}\n"
"QPushButton::hover{\n"
"border: 2px solid #fa1616;\n"
"background-color: #ff7770;\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: #ff6666;\n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Icons/delete_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.delete_1.setIcon(icon6)
        self.delete_1.setIconSize(QtCore.QSize(32, 32))
        self.delete_1.setObjectName("delete_1")
        self.horizontalLayout_3.addWidget(self.delete_1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.btnsave = QtWidgets.QPushButton(self.property)
        self.btnsave.setMinimumSize(QtCore.QSize(100, 40))
        self.btnsave.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.btnsave.setFont(font)
        self.btnsave.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnsave.setStyleSheet("QPushButton{\n"
"background-color: white; \n"
"  color: black; \n"
"  border: 2px solid #76ead7;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #b2ebf2; \n"
"  color: black; \n"
"  border: 2px solid #76ead7;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: #7fdbda; \n"
"}")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btnsave.setIcon(icon7)
        self.btnsave.setIconSize(QtCore.QSize(22, 22))
        self.btnsave.setObjectName("btnsave")
        self.horizontalLayout_3.addWidget(self.btnsave)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.property)
        spacerItem11 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem11)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(290, 0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(290, 400))
        self.groupBox_2.setStyleSheet("QGroupBox{\n"
"background-color: #ebecf1;\n"
"border: 2px solid #ababf1;\n"
"border-radius: 8px;\n"
"}")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        spacerItem13 = QtWidgets.QSpacerItem(70, 17, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem13, 0, 0, 1, 1)
        self.jami = QtWidgets.QLineEdit(self.groupBox_2)
        self.jami.setMinimumSize(QtCore.QSize(165, 30))
        self.jami.setMaximumSize(QtCore.QSize(165, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.jami.setFont(font)
        self.jami.setReadOnly(True)
        self.jami.setObjectName("jami")
        self.gridLayout_11.addWidget(self.jami, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_11)
        self.delete_all = QtWidgets.QPushButton(self.groupBox_2)
        self.delete_all.setMinimumSize(QtCore.QSize(0, 40))
        self.delete_all.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.delete_all.setFont(font)
        self.delete_all.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_all.setStyleSheet("QPushButton{\n"
"border-radius: 10px;\n"
"border: 2px solid #fa1616;\n"
"background-color: white;\n"
"}\n"
"QPushButton::hover{\n"
"border: 2px solid #fa1616;\n"
"background-color: #ff7770;\n"
"color: white;\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: #ff6666;\n"
"}")
        self.delete_all.setIcon(icon6)
        self.delete_all.setIconSize(QtCore.QSize(32, 32))
        self.delete_all.setObjectName("delete_all")
        self.verticalLayout.addWidget(self.delete_all)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem14)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.gridLayout_5.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.search_edit, self.search_edit_2)
        MainWindow.setTabOrder(self.search_edit_2, self.import_2)
        MainWindow.setTabOrder(self.import_2, self.export_2)
        MainWindow.setTabOrder(self.export_2, self.narx)
        MainWindow.setTabOrder(self.narx, self.qadoq)
        MainWindow.setTabOrder(self.qadoq, self.soni)
        MainWindow.setTabOrder(self.soni, self.delete_1)
        MainWindow.setTabOrder(self.delete_1, self.btnsave)
        MainWindow.setTabOrder(self.btnsave, self.jami)
        MainWindow.setTabOrder(self.jami, self.delete_all)
        MainWindow.setTabOrder(self.delete_all, self.mix)
        MainWindow.setTabOrder(self.mix, self.search_2)
        MainWindow.setTabOrder(self.search_2, self.filtered)
        MainWindow.setTabOrder(self.filtered, self.summa)
        MainWindow.setTabOrder(self.summa, self.search)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reviziya"))
        self.search_edit.setPlaceholderText(_translate("MainWindow", "Қўшиш учун"))
        self.search_edit_2.setPlaceholderText(_translate("MainWindow", "Қидириш"))
        self.progressBar.setFormat(_translate("MainWindow", "%p%"))
        self.import_2.setText(_translate("MainWindow", "Импорт"))
        self.progressBar2.setFormat(_translate("MainWindow", "%p%"))
        self.export_2.setText(_translate("MainWindow", "Экспорт"))
        self.filtered.setSortingEnabled(False)
        item = self.filtered.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "CODE"))
        item = self.filtered.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Махсулот номи"))
        item = self.filtered.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Ишлаб чиқарувчи"))
        item = self.filtered.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Нархи"))
        item = self.filtered.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Қадоқ"))
        item = self.filtered.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Сони"))
        item = self.filtered.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Муддати"))
        item = self.filtered.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Date"))
        item = self.filtered.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "ID"))
        self.status.setText(_translate("MainWindow", "Қўшилган дорилар:"))
        self.label_4.setText(_translate("MainWindow", "Нархи:      "))
        self.label_5.setText(_translate("MainWindow", "Қадоқ:      "))
        self.label_6.setText(_translate("MainWindow", "Сони:        "))
        self.label_7.setText(_translate("MainWindow", "Сумма:      "))
        self.delete_1.setText(_translate("MainWindow", "Ўчириш"))
        self.btnsave.setText(_translate("MainWindow", "Сақлаш"))
        self.label.setText(_translate("MainWindow", "Жами сумма:"))
        self.delete_all.setText(_translate("MainWindow", "Барчасини ўчириш"))
import Icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
