from enum import Enum


class EndpointConfigurationKind(str, Enum):
    DEVICE = "DEVICE"
    PEOPLE = "PEOPLE"
    WORKLOAD = "WORKLOAD"

    def __str__(self) -> str:
        return str(self.value)
