from enum import Enum


class ProvisionerWebhookServerType(str, Enum):
    EXTERNAL = "EXTERNAL"
    HOSTED_ATTESTATION = "HOSTED_ATTESTATION"

    def __str__(self) -> str:
        return str(self.value)
