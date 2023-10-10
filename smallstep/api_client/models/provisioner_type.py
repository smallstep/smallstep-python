from enum import Enum


class ProvisionerType(str, Enum):
    ACME = "ACME"
    ACME_ATTESTATION = "ACME_ATTESTATION"
    AWS = "AWS"
    AZURE = "AZURE"
    GCP = "GCP"
    JWK = "JWK"
    OIDC = "OIDC"
    X5C = "X5C"

    def __str__(self) -> str:
        return str(self.value)
