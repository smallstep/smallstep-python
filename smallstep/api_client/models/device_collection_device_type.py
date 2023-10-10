from enum import Enum


class DeviceCollectionDeviceType(str, Enum):
    AWS_VM = "aws-vm"
    AZURE_VM = "azure-vm"
    GCP_VM = "gcp-vm"
    TPM = "tpm"

    def __str__(self) -> str:
        return str(self.value)
