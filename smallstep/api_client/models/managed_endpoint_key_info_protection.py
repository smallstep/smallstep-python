from enum import Enum


class ManagedEndpointKeyInfoProtection(str, Enum):
    DEFAULT = "DEFAULT"
    HARDWARE = "HARDWARE"
    HARDWARE_ATTESTED = "HARDWARE_ATTESTED"
    HARDWARE_WITH_FALLBACK = "HARDWARE_WITH_FALLBACK"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
