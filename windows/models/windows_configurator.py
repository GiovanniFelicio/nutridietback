from .windows_vo import WindowsVO
from core.common.enums.enum_generic_status import EnumGenericStatus


class WindowsConfigurator:
    settings: list[WindowsVO]

    def __init__(self):
        self.get_settings_v1()

    def get_settings_v1(self):
        self.settings.append(WindowsVO(1, 'Person', 'Person', 'person/', 0, EnumGenericStatus.ENABLED))
