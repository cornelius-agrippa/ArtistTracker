from models.CrudStatus import CrudStatus

class Alias:
    def __init__(self, id: int, name: str, url: str = None, idService: int = None, idArtist: int = None):
        self.id:        int = id
        self.name:      str = name
        self.url:       str = url
        self.idService: int = idService
        self.idArtist:  int = idArtist

        # Application managed status for controlling CRUDs
        self.status: CrudStatus = CrudStatus.default
