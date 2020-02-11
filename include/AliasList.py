import os

from models.Alias import Alias
from models.Service import Service

from PyQt5 import QtWidgets, QtGui, QtCore

class AliasList:
    @staticmethod
    def createListItem(listWidget: QtWidgets.QListWidget, alias: Alias):
        text = alias.name + (("\n{0}".format(alias.url)) if alias.url else "")
        item = QtWidgets.QListWidgetItem(text, listWidget)
        image = None

        if alias.idService:
            service = Service.List[alias.idService]

            if not os.path.exists(service.icon):
                print("[Error] Unable to load service icon for '{0}'. Tried to load: {1} but file doesn't exist.".format(service.icon, filepath))
                return

            image = QtGui.QPixmap(service.icon).scaled(48, 48, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        else:
            image = QtGui.QPixmap('./static/no-image.jpg').scaled(48, 48, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)

        icon = QtGui.QIcon(image)
        item.setIcon(icon)

        return item