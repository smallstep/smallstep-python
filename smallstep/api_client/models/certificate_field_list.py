from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CertificateFieldList")


@_attrs_define
class CertificateFieldList:
    """A certificate field that accepts multiple string values, e.g. SANs.

    Attributes:
        device_metadata (Union[Unset, List[str]]): A value populated from a key in the device's metadata.
        static (Union[Unset, List[str]]): A literal value.
    """

    device_metadata: Union[Unset, List[str]] = UNSET
    static: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        device_metadata: Union[Unset, List[str]] = UNSET
        if not isinstance(self.device_metadata, Unset):
            device_metadata = self.device_metadata

        static: Union[Unset, List[str]] = UNSET
        if not isinstance(self.static, Unset):
            static = self.static

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_metadata is not UNSET:
            field_dict["deviceMetadata"] = device_metadata
        if static is not UNSET:
            field_dict["static"] = static

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        device_metadata = cast(List[str], d.pop("deviceMetadata", UNSET))

        static = cast(List[str], d.pop("static", UNSET))

        certificate_field_list = cls(
            device_metadata=device_metadata,
            static=static,
        )

        certificate_field_list.additional_properties = d
        return certificate_field_list

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
