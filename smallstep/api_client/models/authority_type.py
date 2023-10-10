from enum import Enum


class AuthorityType(str, Enum):
    ADVANCED = "advanced"
    DEVOPS = "devops"
    MANAGED = "managed"

    def __str__(self) -> str:
        return str(self.value)
