class AbstractVO:
    name: str
    label: str

    def __init__(self, name, label):
        self.name = name
        self.label = label

    def get_dict(self):
        return self.__dict__
