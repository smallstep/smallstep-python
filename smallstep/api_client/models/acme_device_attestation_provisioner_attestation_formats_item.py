from enum import Enum


class ACMEDeviceAttestationProvisionerAttestationFormatsItem(str, Enum):
    APPLE = "apple"
    STEP = "step"
    TPM = "tpm"

    def __str__(self) -> str:
        return str(self.value)
