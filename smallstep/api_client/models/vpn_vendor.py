from enum import Enum


class VPNVendor(str, Enum):
    CISCO = "Cisco"
    F5 = "F5"
    JUNIPER = "Juniper"

    def __str__(self) -> str:
        return str(self.value)
