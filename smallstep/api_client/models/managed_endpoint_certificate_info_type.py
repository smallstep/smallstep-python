from enum import Enum


class ManagedEndpointCertificateInfoType(str, Enum):
    SSH_HOST = "SSH_HOST"
    SSH_USER = "SSH_USER"
    X509 = "X509"

    def __str__(self) -> str:
        return str(self.value)
