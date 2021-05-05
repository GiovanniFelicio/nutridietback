from core.enums.enum_generic_status import EnumGenericStatus


class WindowsVO:
    id: int
    name: str
    title: str
    path: str
    upper: int
    status: EnumGenericStatus

    def __init__(self, id: int, name: str, title: str, path: str, upper: int, status: EnumGenericStatus):
        self.id = id
        self.name = name
        self.title = title
        self.path = path
        self.upper = upper
        self.status = status
