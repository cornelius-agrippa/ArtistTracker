from enum import Enum

class CrudStatus(Enum):
    default = 0
    created = 1
    updated = 2
    deleted = 3