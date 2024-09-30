from enum import Enum


class VPNConnectionType(str, Enum):
    IKEV2 = "IKEv2"
    IPSEC = "IPSec"
    SSL = "SSL"

    def __str__(self) -> str:
        return str(self.value)
