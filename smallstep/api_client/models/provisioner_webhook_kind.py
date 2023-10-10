from enum import Enum


class ProvisionerWebhookKind(str, Enum):
    ENRICHING = "ENRICHING"

    def __str__(self) -> str:
        return str(self.value)
