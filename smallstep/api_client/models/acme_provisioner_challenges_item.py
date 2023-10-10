from enum import Enum


class ACMEProvisionerChallengesItem(str, Enum):
    DNS_01 = "dns-01"
    HTTP_01 = "http-01"
    TLS_ALPN_01 = "tls-alpn-01"

    def __str__(self) -> str:
        return str(self.value)
