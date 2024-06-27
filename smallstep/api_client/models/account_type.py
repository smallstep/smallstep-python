from enum import Enum


class AccountType(str, Enum):
    BROWSER = "browser"
    ETHERNET = "ethernet"
    VPN = "vpn"
    WIFI = "wifi"

    def __str__(self) -> str:
        return str(self.value)
