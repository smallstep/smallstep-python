from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SSHHostTag")


@_attrs_define
class SSHHostTag:
    """A key-value pair attached to a host.
    Smallstep determines access by comparing host tags to group grants when a user attempts to SSH to a host.

        Attributes:
            id (Union[Unset, str]): A UUID identifying this host tag.
            name (Union[Unset, str]): The key for the host tag.
            value (Union[Unset, str]): The value for the host tag.
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        value = d.pop("value", UNSET)

        ssh_host_tag = cls(
            id=id,
            name=name,
            value=value,
        )

        ssh_host_tag.additional_properties = d
        return ssh_host_tag

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
