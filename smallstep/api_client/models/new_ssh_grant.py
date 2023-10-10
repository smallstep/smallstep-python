from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewSSHGrant")


@_attrs_define
class NewSSHGrant:
    """The body of a request to add a grant to a group.

    Attributes:
        group_id (str): A UUID identifying the group this grant is attached to.
        name (str): Matched against host tag names
        sudo (Union[Unset, bool]): Whether users in the group will have sudo permission on matching hosts
        value (Union[Unset, str]): Matched against host tag values
    """

    group_id: str
    name: str
    sudo: Union[Unset, bool] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group_id = self.group_id
        name = self.name
        sudo = self.sudo
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "groupID": group_id,
                "name": name,
            }
        )
        if sudo is not UNSET:
            field_dict["sudo"] = sudo
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        group_id = d.pop("groupID")

        name = d.pop("name")

        sudo = d.pop("sudo", UNSET)

        value = d.pop("value", UNSET)

        new_ssh_grant = cls(
            group_id=group_id,
            name=name,
            sudo=sudo,
            value=value,
        )

        new_ssh_grant.additional_properties = d
        return new_ssh_grant

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
