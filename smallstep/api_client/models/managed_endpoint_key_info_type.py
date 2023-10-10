from enum import Enum


class ManagedEndpointKeyInfoType(str, Enum):
    DEFAULT = "DEFAULT"
    ECDSA_P256 = "ECDSA_P256"
    ECDSA_P384 = "ECDSA_P384"
    ECDSA_P521 = "ECDSA_P521"
    ED25519 = "ED25519"
    RSA_2048 = "RSA_2048"
    RSA_3072 = "RSA_3072"
    RSA_4096 = "RSA_4096"

    def __str__(self) -> str:
        return str(self.value)
