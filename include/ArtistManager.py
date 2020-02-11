from typing import List

from PyQt5 import QtGui, QtWidgets

from ui.ArtistManagerUI import Ui_ArtistManager

from include.AliasList import AliasList
import include.Pixmaps as Pixmaps

from models.Artist import Artist
from models.Service import Service
from models.Alias import Alias
from models.CrudStatus import CrudStatus

class ArtistManager(QtWidgets.QMainWindow):
    def __init__(self, parent: QtWidgets.QMainWindow):
        QtWidgets.QMainWindow.__init__(self, parent)

        self.parent = parent

        self.artist: Artist = Artist(None, None)
        self.aliasList: List[Alias] = []

        self.ui = Ui_ArtistManager()
        self.ui.setupUi(self)

        self.ui.pushDelete.setIcon(Pixmaps.getIcon("delete"))
        self.ui.pushDelete.setText("")
        self.ui.pushDelete.clicked.connect(lambda: self.onDeleteArtist())

        self.ui.pushSaveAlias.setIcon(Pixmaps.getIcon("save"))
        self.ui.pushSaveAlias.setText("")
        self.ui.pushSaveAlias.clicked.connect(lambda: self.onNewAlias())

        self.ui.pushRemoveAlias.setIcon(Pixmaps.getIcon("remove"))
        self.ui.pushRemoveAlias.setText("")
        self.ui.pushRemoveAlias.clicked.connect(lambda: self.onRemoveAlias())

        self.ui.pushSave.clicked.connect(lambda: self.onSaveArtist())
        self.ui.pushCancel.clicked.connect(lambda: self.close())

        self.ui.comboBoxServices.addItem("None")

        for key, service in Service.List.items():
            self.ui.comboBoxServices.addItem(QtGui.QIcon(service.icon), service.name, service.id)

    ############################################################################
    # Artist Management
    def loadArtist(self, artist: Artist):
        self.artist = artist
        self.ui.lineName.setText(artist.name)
        self.loadAliases()

    def onSaveArtist(self):
        self.artist.name = self.ui.lineName.text()

        # Updating artist
        if self.artist.id:
            self.parent.dal.updateArtist(self.artist)
            for alias in self.artist.aliases:
                if alias.status == CrudStatus.created:
                    self.parent.dal.insertAlias(alias)
                elif alias.status == CrudStatus.deleted:
                    self.parent.dal.deleteAlias(alias.id)

        # New artist
        else:
            self.artist.id = self.parent.dal.insertArtist(self.artist)
            for alias in self.artist.aliases:
                alias.idArtist = self.artist.id
                self.parent.dal.insertAlias(alias)

        self.parent.loadArtists()
        self.parent.displayArtists()
        self.close()

    def onDeleteArtist(self):
        if not self.artist.id:
            return

        qm = QtWidgets.QMessageBox.question(self, 'Delete Artist?', "Are you sure you want to delete this artist? All data associated with this entry will be permanently removed.", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        if qm == QtWidgets.QMessageBox.No:
            return

        self.parent.dal.deleteArtist(self.artist.id)
        self.parent.loadArtists()
        self.parent.displayArtists()

        self.close()

    ############################################################################
    # Alias Management
    def loadAliases(self):
        for alias in self.artist.aliases:
            AliasList.createListItem(self.ui.listAlias, alias)

    def onNewAlias(self):
        aliasName = self.ui.lineAliasName.text().strip()

        if not aliasName:
            return

        aliasUrl  = self.ui.lineAliasUrl.text().strip()
        idService = self.ui.comboBoxServices.currentData()
        idArtist = self.artist.id if self.artist.id else None

        alias = Alias(None, aliasName, aliasUrl, idService, idArtist)
        alias.status = CrudStatus.created

        AliasList.createListItem(self.ui.listAlias, alias)

        self.artist.aliases.append(alias)

    def onRemoveAlias(self):
        #qm = QtWidgets.QMessageBox.question(self, 'Delete Alias?', "Are you sure you want to delete this alias?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

        #if qm == QtWidgets.QMessageBox.No:
            #return

        for item in self.ui.listAlias.selectedItems():
            row = self.ui.listAlias.row(item)
            self.ui.listAlias.takeItem(row)
            self.artist.aliases[row].status = CrudStatus.deleted
