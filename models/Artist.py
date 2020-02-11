from typing import List

from models.Circle import Circle
from models.Alias import Alias
from models.Art import Art

class Artist:
    def __init__(self, id: int, name: str, aliases: list = [], art: list = [], circle: Circle = None, status: str = None):
        self.id: int = id

        # Main name used by this artist
        self.name: str = name

        # List of aliases by service
        self.aliases: List[Alias] = aliases

        # Example art by this artist
        self.art: List[Art] = art

        # Is artist still active? Still drawing stuff, etc?
        self.status: str = status

        # The circle/artist group this Artist belongs to
        self.circle: Circle = circle

    def toJson(self):
        import json
        return json.dumps (self, default=lambda o: o.__dict__, sort_keys=True)

    def loadFromTuple(artistTuple):
        pass
