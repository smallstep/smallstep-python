from enum import Enum


class SCEPProvisionerEncryptionAlgorithmIdentifier(str, Enum):
    AES_128_CBC = "AES_128_CBC"
    AES_128_GCM = "AES_128_GCM"
    AES_256_CBC = "AES_256_CBC"
    AES_256_GCM = "AES_256_GCM"
    DES_CBC = "DES_CBC"

    def __str__(self) -> str:
        return str(self.value)
