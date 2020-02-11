class Service:
    def __init__(self, id, name, icon):
        self.id:   int = id
        self.name: str = name
        self.icon: str = icon

    # Static globally accessible service list
    List = {}
