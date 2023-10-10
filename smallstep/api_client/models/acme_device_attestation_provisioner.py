from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.acme_device_attestation_provisioner_attestation_formats_item import (
    ACMEDeviceAttestationProvisionerAttestationFormatsItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ACMEDeviceAttestationProvisioner")


@_attrs_define
class ACMEDeviceAttestationProvisioner:
    """A [provisioner](https://smallstep.com/docs/step-ca/provisioners/#acme) that enables automation with the [device-
    attest-01 challenge of the ACME protocol](https://smallstep.com/blog/acme-managed-device-attestation-explained/).

        Attributes:
            attestation_formats (List[ACMEDeviceAttestationProvisionerAttestationFormatsItem]): The allowed attestation
                formats for the device-attest-01 challenge. Valid values are `apple`, `step`, and `tpm`. The apple format is for
                Apple devices, and adds trust for Apple's CAs. The step format is for non-TPM devices that can issue attestation
                certificates, such as YubiKey PIV. It adds trust for Yubico's root CA. The tpm format is for TPMs and does not
                trust any CAs by default.
            attestation_roots (Union[Unset, List[str]]): A trust bundle of root certificates in PEM format that will be used
                to verify attestation certificates. The default value depends on the value of attestationFormats. If provided,
                this PEM bundle will override the CA trust established by setting attestationFormats to apple or step. At least
                one root certificate is required when using the tpm attestationFormat.
            force_cn (Union[Unset, bool]): Force one of the SANs to become the Common Name, if a Common Name is not
                provided.
            require_eab (Union[Unset, bool]): Only ACME clients that have been preconfigured with valid EAB credentials will
                be able to create an account with this provisioner.
    """

    attestation_formats: List[ACMEDeviceAttestationProvisionerAttestationFormatsItem]
    attestation_roots: Union[Unset, List[str]] = UNSET
    force_cn: Union[Unset, bool] = UNSET
    require_eab: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attestation_formats = []
        for attestation_formats_item_data in self.attestation_formats:
            attestation_formats_item = attestation_formats_item_data.value

            attestation_formats.append(attestation_formats_item)

        attestation_roots: Union[Unset, List[str]] = UNSET
        if not isinstance(self.attestation_roots, Unset):
            attestation_roots = self.attestation_roots

        force_cn = self.force_cn
        require_eab = self.require_eab

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attestationFormats": attestation_formats,
            }
        )
        if attestation_roots is not UNSET:
            field_dict["attestationRoots"] = attestation_roots
        if force_cn is not UNSET:
            field_dict["forceCN"] = force_cn
        if require_eab is not UNSET:
            field_dict["requireEAB"] = require_eab

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        attestation_formats = []
        _attestation_formats = d.pop("attestationFormats")
        for attestation_formats_item_data in _attestation_formats:
            attestation_formats_item = ACMEDeviceAttestationProvisionerAttestationFormatsItem(
                attestation_formats_item_data
            )

            attestation_formats.append(attestation_formats_item)

        attestation_roots = cast(List[str], d.pop("attestationRoots", UNSET))

        force_cn = d.pop("forceCN", UNSET)

        require_eab = d.pop("requireEAB", UNSET)

        acme_device_attestation_provisioner = cls(
            attestation_formats=attestation_formats,
            attestation_roots=attestation_roots,
            force_cn=force_cn,
            require_eab=require_eab,
        )

        acme_device_attestation_provisioner.additional_properties = d
        return acme_device_attestation_provisioner

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
