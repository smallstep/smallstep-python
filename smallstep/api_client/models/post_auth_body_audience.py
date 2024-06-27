from enum import Enum


class PostAuthBodyAudience(str, Enum):
    STEP_AGENT = "step-agent"

    def __str__(self) -> str:
        return str(self.value)
