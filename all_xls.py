# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'all_xls.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(501, 210)
        MainWindow.setStyleSheet("\n"
"#import_2 {\n"
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
"#MainWindow{\n"
"background-color: #f6f5f5;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.import_2.setIcon(icon)
        self.import_2.setIconSize(QtCore.QSize(32, 32))
        self.import_2.setObjectName("import_2")
        self.horizontalLayout.addWidget(self.import_2)
        self.imported = QtWidgets.QPushButton(self.centralwidget)
        self.imported.setMaximumSize(QtCore.QSize(40, 16777215))
        self.imported.setStyleSheet("background-color: #f6f5f5;\n"
"border: 1px solid #f6f5f5;")
        self.imported.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/true.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.imported.setIcon(icon1)
        self.imported.setIconSize(QtCore.QSize(32, 32))
        self.imported.setObjectName("imported")
        self.horizontalLayout.addWidget(self.imported)
        spacerItem = QtWidgets.QSpacerItem(140, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/fgdwfs.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.export_2.setIcon(icon2)
        self.export_2.setIconSize(QtCore.QSize(32, 32))
        self.export_2.setObjectName("export_2")
        self.horizontalLayout.addWidget(self.export_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.import_2.setText(_translate("MainWindow", "Импорт"))
        self.export_2.setText(_translate("MainWindow", "Экспорт"))
import Icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
