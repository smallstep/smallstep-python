from enum import Enum


class ProvisionerWebhookCertType(str, Enum):
    ALL = "ALL"
    SSH = "SSH"
    X509 = "X509"

    def __str__(self) -> str:
        return str(self.value)
