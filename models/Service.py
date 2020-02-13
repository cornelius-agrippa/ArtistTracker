class Service:
    def __init__(self, id, name, icon):
        self.id:   int = id
        self.name: str = name
        self.icon: str = icon

    # Globally accessible service list
    List = {}
