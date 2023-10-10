from enum import Enum


class ManagedEndpointReloadInfoMethod(str, Enum):
    AUTOMATIC = "AUTOMATIC"
    CUSTOM = "CUSTOM"
    DBUS = "DBUS"
    SIGNAL = "SIGNAL"

    def __str__(self) -> str:
        return str(self.value)
