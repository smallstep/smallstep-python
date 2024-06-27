from enum import Enum


class ManagedEndpointKeyInfoFormat(str, Enum):
    CLASSIC = "CLASSIC"
    DEFAULT = "DEFAULT"
    OPENSSH = "OPENSSH"
    PKCS8 = "PKCS8"
    TSS2 = "TSS2"

    def __str__(self) -> str:
        return str(self.value)
