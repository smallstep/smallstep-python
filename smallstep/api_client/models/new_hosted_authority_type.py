from enum import Enum


class NewHostedAuthorityType(str, Enum):
    ADVANCED = "advanced"
    DEVOPS = "devops"

    def __str__(self) -> str:
        return str(self.value)
