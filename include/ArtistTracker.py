import os, sys

from ui.MainUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

from include.DataLayer import DataLayer
from include.ArtistManager import ArtistManager
from include.AliasList import AliasList

from models.Service import Service
from models.Artist import Artist
from models.Alias import Alias
from models.Art import Art

class ArtistTracker(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.dal = DataLayer()
        self.dal.migrate()

        self.artists = []
        self.filteredArtists = []

        self.loadServices()
        self.loadArtists()
        self.displayArtists()
        self.clearAvatar()

        # Events
        self.ui.lineSearch.textChanged.connect(lambda search: self.onSearchArtists(search))
        self.ui.pushClear.clicked.connect(lambda: self.ui.lineSearch.clear())

        self.ui.tableArtists.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableArtists.currentCellChanged.connect(lambda row: self.onArtistChange(row))
        self.ui.tableArtists.doubleClicked.connect(lambda row: self.onArtistDetails(row))

        self.ui.pushNewArtist.clicked.connect(lambda: self.onNewArtist())

    def displayArtists(self):
        self.ui.tableArtists.setColumnCount(2)

        # Cleanup previous contents
        self.ui.tableArtists.model().removeRows(0, self.ui.tableArtists.rowCount())

        self.ui.tableArtists.setRowCount(len(self.filteredArtists))

        for i, artist in enumerate(self.filteredArtists):
            self.ui.tableArtists.setItem(i, 0, QtWidgets.QTableWidgetItem(artist.name))

            shownAliases = []

            if len(artist.aliases):
                for alias in artist.aliases:
                    if alias.name not in shownAliases:
                        shownAliases.append(alias.name)

                self.ui.tableArtists.setItem(i, 1, QtWidgets.QTableWidgetItem(', '.join(shownAliases)))
            else:
                self.ui.tableArtists.setItem(i, 1, QtWidgets.QTableWidgetItem(' --- '))

        self.ui.tableArtists.setCurrentIndex(self.ui.tableArtists.model().index(2, 0))
        self.ui.tableArtists.setHorizontalHeaderLabels(['Name', 'Alias'])
        self.ui.tableArtists.resizeColumnsToContents()
        self.ui.tableArtists.resizeRowsToContents()
        self.ui.tableArtists.show()

    def onSearchArtists(self, searchTerm):
        if not len(searchTerm):
            self.filteredArtists = self.artists.copy()
        else:
            self.filteredArtists = list(filter(
                lambda artist:
                    searchTerm.lower() in artist.name.lower()
                    or list(filter(
                        lambda alias:
                            searchTerm.lower() in alias.name.lower(),
                        artist.aliases)),
                self.artists))

        self.displayArtists()

    def loadServices(self):
        for service in self.dal.getServices():
            Service.List[service[0]] = Service(service[0], service[1], service[2])

    def loadArtists(self):
        self.artists.clear()
        self.filteredArtists.clear()

        artists = self.dal.getArtists()

        for artist in artists:
            aliases = []
            for alias in self.dal.getAliases(artist[0]):
                aliases.append(Alias(alias[0], alias[1], alias[2], alias[3]))

            arts = []
            for art in self.dal.getArt(artist[0]):
                arts.append(Art(art[0], art[1]))

            self.artists.append(Artist(artist[0], artist[1], aliases, arts))

        self.filteredArtists = self.artists.copy()

    def setAvatar(self, filepath):
        if not os.path.exists(filepath):
            clearAvatar()
            print("[Error] Unable to load avatar for selected item. Tried to load: {0} but file doesn't exist.".format(filepath))
            return

        w = self.ui.labelAvatar.width();
        h = self.ui.labelAvatar.height();

        self.ui.labelAvatar.setPixmap(QtGui.QPixmap(filepath).scaled(w, h, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.ui.labelAvatar.show()

    def clearAvatar(self):
        self.setAvatar('./static/no-image.jpg')

    def onArtistChange(self, row):
        if not len(self.filteredArtists):
            self.clearAvatar()
            self.ui.listAlias.clear()
            return

        if len(self.filteredArtists[row].art):
            filepath = "./db/artists/{0}/{1}".format(self.filteredArtists[row].id, self.filteredArtists[row].art[0].filepath)
            self.setAvatar(filepath)
        else:
            self.clearAvatar()

        self.ui.listAlias.clear()

        for alias in self.filteredArtists[row].aliases:
            AliasList.createListItem(self.ui.listAlias, alias)

    def onNewArtist(self):
        self.amMainWindow = ArtistManager(self)
        self.amMainWindow.show()

    def onArtistDetails(self, index: QtCore.QModelIndex):
        if (index.row() > len(self.filteredArtists) - 1):
            return

        artist = self.filteredArtists[index.row()]

        self.amMainWindow = ArtistManager(self)
        self.amMainWindow.loadArtist(artist)
        self.amMainWindow.show()
