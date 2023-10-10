from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SSHHostGrant")


@_attrs_define
class SSHHostGrant:
    """A grant gives permission to all users in a group to access a host with a matching tag.

    Attributes:
        group_id (Union[Unset, str]): A UUID identifying the group this grant is attached to.
        id (Union[Unset, str]): A UUID identifying this grant.
        name (Union[Unset, str]): Matched against host tag names.
        sudo (Union[Unset, bool]): Whether users in the group will have sudo permission on matching hosts.
        value (Union[Unset, str]): Matched against host tag values.
    """

    group_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    sudo: Union[Unset, bool] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group_id = self.group_id
        id = self.id
        name = self.name
        sudo = self.sudo
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_id is not UNSET:
            field_dict["groupID"] = group_id
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if sudo is not UNSET:
            field_dict["sudo"] = sudo
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        group_id = d.pop("groupID", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        sudo = d.pop("sudo", UNSET)

        value = d.pop("value", UNSET)

        ssh_host_grant = cls(
            group_id=group_id,
            id=id,
            name=name,
            sudo=sudo,
            value=value,
        )

        ssh_host_grant.additional_properties = d
        return ssh_host_grant

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
