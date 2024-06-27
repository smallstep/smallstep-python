from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.managed_endpoint_key_info_format import ManagedEndpointKeyInfoFormat
from ..models.managed_endpoint_key_info_protection import ManagedEndpointKeyInfoProtection
from ..models.managed_endpoint_key_info_type import ManagedEndpointKeyInfoType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ManagedEndpointKeyInfo")


@_attrs_define
class ManagedEndpointKeyInfo:
    """The attributes of the cryptographic key.

    Example:
        {'format': 'PKCS8', 'protection': 'NONE', 'pubFile': '/etc/db.csr', 'type': 'ECDSA_P256'}

    Attributes:
        format_ (Union[Unset, ManagedEndpointKeyInfoFormat]): The format used to encode the private key. For X509 keys
            the default format is PKCS#8. The classic format is PKCS#1 for RSA keys, SEC 1 for ECDSA keys, and PKCS#8 for
            ED25519 keys. For SSH keys the default format is always the OPENSSH format. When a hardware module is used to
            store the keys the default will be a JSON representation of the key, except on Linux where tss2 will be used.
        protection (Union[Unset, ManagedEndpointKeyInfoProtection]): Whether to use a hardware module to store the
            private key for a workload certificate. If set to `NONE` no hardware module will be used. If set to `DEFAULT` a
            hardware module will only be used with format `TSS2`. `HARDWARE_WITH_FALLBACK` can only be used with the key
            format `DEFAULT`.
        pub_file (Union[Unset, str]): A CSR or SSH public key to use instead of generating one.
        type (Union[Unset, ManagedEndpointKeyInfoType]): The key type used. The current DEFAULT type is ECDSA_P256.
    """

    format_: Union[Unset, ManagedEndpointKeyInfoFormat] = UNSET
    protection: Union[Unset, ManagedEndpointKeyInfoProtection] = UNSET
    pub_file: Union[Unset, str] = UNSET
    type: Union[Unset, ManagedEndpointKeyInfoType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        protection: Union[Unset, str] = UNSET
        if not isinstance(self.protection, Unset):
            protection = self.protection.value

        pub_file = self.pub_file

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if format_ is not UNSET:
            field_dict["format"] = format_
        if protection is not UNSET:
            field_dict["protection"] = protection
        if pub_file is not UNSET:
            field_dict["pubFile"] = pub_file
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, ManagedEndpointKeyInfoFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = ManagedEndpointKeyInfoFormat(_format_)

        _protection = d.pop("protection", UNSET)
        protection: Union[Unset, ManagedEndpointKeyInfoProtection]
        if isinstance(_protection, Unset):
            protection = UNSET
        else:
            protection = ManagedEndpointKeyInfoProtection(_protection)

        pub_file = d.pop("pubFile", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, ManagedEndpointKeyInfoType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ManagedEndpointKeyInfoType(_type)

        managed_endpoint_key_info = cls(
            format_=format_,
            protection=protection,
            pub_file=pub_file,
            type=type,
        )

        managed_endpoint_key_info.additional_properties = d
        return managed_endpoint_key_info

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
