from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TPMDeviceType")


@_attrs_define
class TPMDeviceType:
    """Configuration for a device collection of machines with TPMs.

    Attributes:
        attestor_intermediates (Union[Unset, str]): The pem-encoded list of intermediate certificates used to build a
            chain of trust to verify the attestation certificates submitted by agents. Ignored if the team already has an
            attestation authority.
        attestor_roots (Union[Unset, str]): The pem-encoded list of certificates used to verify the attestation
            certificates submitted by agents. Ignored if the team already has an attestation authority. Required if the team
            does not already have an attestation authority.
        force_cn (Union[Unset, bool]): Force one of the SANs to become the Common Name, if a Common Name is not
            provided.
        require_eab (Union[Unset, bool]): Only ACME clients that have been preconfigured with valid EAB credentials will
            be able to create an account with this provisioner.
    """

    attestor_intermediates: Union[Unset, str] = UNSET
    attestor_roots: Union[Unset, str] = UNSET
    force_cn: Union[Unset, bool] = UNSET
    require_eab: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attestor_intermediates = self.attestor_intermediates
        attestor_roots = self.attestor_roots
        force_cn = self.force_cn
        require_eab = self.require_eab

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attestor_intermediates is not UNSET:
            field_dict["attestorIntermediates"] = attestor_intermediates
        if attestor_roots is not UNSET:
            field_dict["attestorRoots"] = attestor_roots
        if force_cn is not UNSET:
            field_dict["forceCN"] = force_cn
        if require_eab is not UNSET:
            field_dict["requireEAB"] = require_eab

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        attestor_intermediates = d.pop("attestorIntermediates", UNSET)

        attestor_roots = d.pop("attestorRoots", UNSET)

        force_cn = d.pop("forceCN", UNSET)

        require_eab = d.pop("requireEAB", UNSET)

        tpm_device_type = cls(
            attestor_intermediates=attestor_intermediates,
            attestor_roots=attestor_roots,
            force_cn=force_cn,
            require_eab=require_eab,
        )

        tpm_device_type.additional_properties = d
        return tpm_device_type

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
