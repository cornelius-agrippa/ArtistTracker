import sqlite3
from typing import List

from models.Art import Art
from models.Alias import Alias
from models.Artist import Artist
from models.Service import Service

# Data Access Layer class
#   Connects with SQLite to perform CRUD operations
#
#   Database location is defined by self.dbFile
#
#   Migration version may be controlled with the version variable and
#   the self.insertMigration(<desiredVersion>) method
class DataLayer:
    def __init__(self):
        self.dbFile = "./db/tracker.db"
        self.conn = sqlite3.connect(self.dbFile, check_same_thread=True)

    def __del__(self):
        self.conn.close()

    def migrate(self):
        c = self.conn.cursor()

        c.execute('CREATE TABLE IF NOT EXISTS migrations ( id INTEGER PRIMARY KEY )');

        version = self.getLastMigration()

        if not version:
            print("[Migration] Creating initial tables and seeding data")

            c.execute('''CREATE TABLE IF NOT EXISTS circles (
                id INTEGER PRIMARY KEY,
                name TEXT )
            ''');

            c.execute('''CREATE TABLE IF NOT EXISTS services (
                id INTEGER PRIMARY KEY,
                name TEXT,
                icon TEXT
            )''');

            c.execute('''CREATE TABLE IF NOT EXISTS artists (
                id INTEGER PRIMARY KEY,
                name TEXT,
                status TEXT,
                id_circle INTEGER,
                FOREIGN KEY(id_circle) REFERENCES circles
            )''');

            c.execute('''CREATE TABLE IF NOT EXISTS art (
                id INTEGER PRIMARY KEY,
                id_artist INTEGER,
                filepath TEXT,
                rank INTEGER,
                FOREIGN KEY(id_artist ) REFERENCES artists(id)
            )''');

            c.execute('''CREATE TABLE IF NOT EXISTS aliases (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                url TEXT,
                id_service INTEGER,
                id_artist INTEGER NOT NULL,
                FOREIGN KEY(id_service) REFERENCES services(id),
                FOREIGN KEY(id_artist) REFERENCES artists(id)
            )''');

            services = [
                ('Twitter', './static/icons/twitter.png'),
                ('Pixiv', './static/icons/pixiv.png'),
                ('Soundcloud', './static/icons/soundcloud.png'),
                ('DeviantArt', './static/icons/deviantart.png'),
            ]

            c.executemany('INSERT INTO services (name, icon) VALUES (?, ?);', services);

            version = self.insertMigration(1)

        print("[Done, DB version: {0}]".format(version))

    # ##########################################################################
    # Gets
    def getLastRecord(self, tablename: str):
        c = self.conn.cursor()
        c.execute('SELECT * FROM {0} ORDER BY id DESC LIMIT 1'.format(tablename))
        data = c.fetchone()
        return data[0] if data is not None else False

    def getLastMigration(self):
        return self.getLastRecord("migrations")

    def getArtists(self) -> List[Artist]:
        c = self.conn.cursor()
        c.row_factory = lambda cursor, row: Artist(row[0], row[1])

        c.execute('''SELECT a.id, a.name
            FROM artists AS a
            --LEFT JOIN circles AS c ON c.id = a.id_circle
            ORDER BY name DESC'''
        )

        return c.fetchall()

    def getAliases(self, idArtist: int) -> List[Alias]:
        c = self.conn.cursor()
        c.row_factory = lambda cursor, row: Alias(row[0], row[1], row[2], row[3])
        c.execute('SELECT id, name, url, id_service, id_artist FROM aliases WHERE id_artist = ?', (idArtist,))
        return c.fetchall()

    def getArt(self, idArtist: int) -> List[Art]:
        c = self.conn.cursor()
        c.row_factory = lambda cursor, row: Art(row[0], row[1])
        c.execute('SELECT filepath, rank FROM art WHERE id_artist = ? ORDER BY rank ASC', (idArtist,))
        return c.fetchall()

    def getServices(self) -> List[Service]:
        c = self.conn.cursor()
        c.row_factory = lambda cursor, row: Service(row[0], row[1], row[2])
        c.execute('SELECT id, name, icon FROM services')
        return c.fetchall()

    # ##########################################################################
    # Inserts
    def insertMigration(self, version):
        c = self.conn.cursor()
        c.execute('INSERT INTO migrations (id) VALUES (?)', (version,))
        self.conn.commit()
        return c.lastrowid

    def insertArtist(self, artist: Artist):
        c = self.conn.cursor()
        c.execute('''INSERT INTO artists (name, status, id_circle) VALUES (?, ?, ?)''', (
            artist.name,
            artist.status,
            artist.circle.id if artist.circle else None,
        ))
        self.conn.commit()

        return c.lastrowid

    def insertAlias(self, alias: Alias):
        c = self.conn.cursor()
        c.execute('INSERT INTO aliases (name, url, id_service, id_artist) VALUES (?, ?, ?, ?)', (
            alias.name,
            alias.url,
            alias.idService,
            alias.idArtist,
        ))
        self.conn.commit()
        return c.lastrowid

    # ##########################################################################
    # Updates
    def updateArtist(self, artist: Artist):
        if not artist.id:
            print ("[Error] Tried to update an Artist with no ID. Check if Artist is valid.")
            return False

        c = self.conn.cursor()
        c.execute('''UPDATE artists SET
            name = coalesce(?, name),
            status = coalesce(?, status),
            id_circle = coalesce(?, id_circle)
            WHERE id = ?
        ''', (
            artist.name,
            artist.status,
            artist.circle.id if artist.circle else None,
            int(artist.id),
        ))
        self.conn.commit()

        return c.lastrowid

    def updateAlias(self, alias: Alias):
        if not alias.id:
            print ("[Error] Tried to update an Alias with no ID. Check if Alias is valid.")
            return False

        c = self.conn.cursor()
        c.execute('''UPDATE aliases SET
            name = coalesce(?, name),
            url = coalesce(?, url),
            id_service = coalesce(?, id_service),
            id_artist = coalesce(?, id_artist)
            WHERE id = ?
        ''', (
            alias.name,
            alias.url,
            alias.idService,
            alias.idArtist,
            alias.id,
        ))
        self.conn.commit()

        return c.lastrowid

    # ##########################################################################
    # Deletes
    def deleteArtist(self, idArtist: int):
        c = self.conn.cursor()
        c.execute('DELETE FROM artists WHERE id = ?', (idArtist,))
        self.conn.commit()
        return c.lastrowid

    def deleteAlias(self, idAlias: int):
        c = self.conn.cursor()
        c.execute('DELETE FROM aliases WHERE id = ?', (idAlias,))
        self.conn.commit()
        return c.lastrowid