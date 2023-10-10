from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.managed_endpoint_key_info_format import ManagedEndpointKeyInfoFormat
from ..models.managed_endpoint_key_info_type import ManagedEndpointKeyInfoType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ManagedEndpointKeyInfo")


@_attrs_define
class ManagedEndpointKeyInfo:
    """The attributes of the cryptographic key.

    Example:
        {'format': 'DER', 'pubFile': '/etc/db.csr', 'type': 'ECDSA_P256'}

    Attributes:
        format_ (Union[Unset, ManagedEndpointKeyInfoFormat]): The format used to encode the private key. For X509 keys
            the default format is SEC 1 for ECDSA keys, PKCS#1 for RSA keys and PKCS#8 for ED25519 keys. For SSH keys the
            default format is always the OPENSSH format.
        pub_file (Union[Unset, str]): A CSR or SSH public key to use instead of generating one.
        type (Union[Unset, ManagedEndpointKeyInfoType]): The key type used. The current DEFAULT type is ECDSA_P256.
    """

    format_: Union[Unset, ManagedEndpointKeyInfoFormat] = UNSET
    pub_file: Union[Unset, str] = UNSET
    type: Union[Unset, ManagedEndpointKeyInfoType] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        pub_file = self.pub_file
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if format_ is not UNSET:
            field_dict["format"] = format_
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

        pub_file = d.pop("pubFile", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, ManagedEndpointKeyInfoType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ManagedEndpointKeyInfoType(_type)

        managed_endpoint_key_info = cls(
            format_=format_,
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
