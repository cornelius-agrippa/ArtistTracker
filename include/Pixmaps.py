from PyQt5 import QtGui

icons = {
    "tick":   ["./static/icons/tick.png"],
    "save":   ["./static/icons/plus.png"],
    "delete": ["./static/icons/delete.png"],
    "remove": ["./static/icons/remove.png"],
    "cancel": ["./static/icons/cancel.png"]
}

def getIcon(iconName: str) -> QtGui.QIcon():
    if iconName not in icons:
        raise IndexError("[Error] Unknown icon '{0}' is not defined in icons".format(iconName))

    if len(icons[iconName]) == 1:
        icon = QtGui.QIcon()
        pixmap = QtGui.QPixmap(icons[iconName][0])

        if pixmap.isNull():
            raise Exception("[Error] Unable to load icon '{0}'. Path was: '{1}'.".format(iconName, icons[iconName][0]))

        icon.addPixmap(pixmap, QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icons[iconName].append(icon)

    return icons[iconName][1]