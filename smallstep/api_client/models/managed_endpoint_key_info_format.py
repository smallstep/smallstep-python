from enum import Enum


class ManagedEndpointKeyInfoFormat(str, Enum):
    DEFAULT = "DEFAULT"
    DER = "DER"
    OPENSSH = "OPENSSH"
    PKCS8 = "PKCS8"

    def __str__(self) -> str:
        return str(self.value)
