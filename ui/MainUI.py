# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alex\Dropbox\Desenvolvimento\Python\ArtistTracker\designer\MainUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.setWindowModality(QtCore.Qt.NonModal)
		MainWindow.resize(745, 483)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
		MainWindow.setSizePolicy(sizePolicy)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout.setObjectName("gridLayout")
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setMaximumSize(QtCore.QSize(16777215, 23))
		font = QtGui.QFont()
		font.setFamily("MS Shell Dlg 2")
		font.setPointSize(14)
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.horizontalLayout_3.addWidget(self.label)
		self.pushNewArtist = QtWidgets.QPushButton(self.centralwidget)
		self.pushNewArtist.setMaximumSize(QtCore.QSize(92, 92))
		self.pushNewArtist.setObjectName("pushNewArtist")
		self.horizontalLayout_3.addWidget(self.pushNewArtist)
		self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.lineSearch = QtWidgets.QLineEdit(self.centralwidget)
		self.lineSearch.setInputMask("")
		self.lineSearch.setText("")
		self.lineSearch.setObjectName("lineSearch")
		self.horizontalLayout_2.addWidget(self.lineSearch)
		self.pushClear = QtWidgets.QPushButton(self.centralwidget)
		self.pushClear.setMaximumSize(QtCore.QSize(24, 16777215))
		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)
		self.pushClear.setFont(font)
		self.pushClear.setObjectName("pushClear")
		self.horizontalLayout_2.addWidget(self.pushClear)
		self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.tableArtists = QtWidgets.QTableWidget(self.centralwidget)
		self.tableArtists.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
		self.tableArtists.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
		self.tableArtists.setColumnCount(1)
		self.tableArtists.setObjectName("tableArtists")
		self.tableArtists.setRowCount(0)
		self.horizontalLayout.addWidget(self.tableArtists)
		self.verticalLayout_2 = QtWidgets.QVBoxLayout()
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.labelAvatar = QtWidgets.QLabel(self.centralwidget)
		self.labelAvatar.setMinimumSize(QtCore.QSize(192, 192))
		self.labelAvatar.setMaximumSize(QtCore.QSize(192, 192))
		self.labelAvatar.setFrameShape(QtWidgets.QFrame.StyledPanel)
		self.labelAvatar.setText("")
		self.labelAvatar.setAlignment(QtCore.Qt.AlignCenter)
		self.labelAvatar.setObjectName("labelAvatar")
		self.verticalLayout_2.addWidget(self.labelAvatar)
		self.listAlias = QtWidgets.QListWidget(self.centralwidget)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.listAlias.sizePolicy().hasHeightForWidth())
		self.listAlias.setSizePolicy(sizePolicy)
		self.listAlias.setMinimumSize(QtCore.QSize(192, 0))
		self.listAlias.setMaximumSize(QtCore.QSize(192, 16777215))
		self.listAlias.setIconSize(QtCore.QSize(32, 32))
		self.listAlias.setWordWrap(False)
		self.listAlias.setObjectName("listAlias")
		self.verticalLayout_2.addWidget(self.listAlias)
		self.horizontalLayout.addLayout(self.verticalLayout_2)
		self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 745, 21))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "Artist Tracker"))
		self.label.setText(_translate("MainWindow", "Artist Tracker"))
		self.pushNewArtist.setText(_translate("MainWindow", "Add New Artist"))
		self.pushNewArtist.setProperty("class", _translate("MainWindow", "primary"))
		self.lineSearch.setPlaceholderText(_translate("MainWindow", "Search..."))
		self.pushClear.setText(_translate("MainWindow", "X"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())
