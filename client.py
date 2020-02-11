import sys

from PyQt5 import QtCore, QtWidgets

from include.ArtistTracker import ArtistTracker

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    style_file = QtCore.QFile("./static/styles/material-light.qss")
    style_file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
    style = QtCore.QTextStream(style_file)
    app.setStyleSheet(style.readAll())

    at = ArtistTracker()
    at.show()

    sys.exit(app.exec_())
