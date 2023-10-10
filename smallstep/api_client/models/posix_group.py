from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="POSIXGroup")


@_attrs_define
class POSIXGroup:
    """A POSIX group represents a group that exists on a host with the given group name and gid.
    A managed group will be created or deleted on the host by Smallstep.
    Unmanaged groups must already exist on the host.

    An SSH Group may have multiple POSIX groups.
    An SSH User belonging to the group will be a member of the POSIX group when they access the host.

        Attributes:
            gid (Union[Unset, int]): The numeric group ID.
            id (Union[Unset, str]): A UUID identifying the POSIX group.
            managed (Union[Unset, bool]): Whether Smallstep should create and delete the group.
            name (Union[Unset, str]): The name of the group.
    """

    gid: Union[Unset, int] = UNSET
    id: Union[Unset, str] = UNSET
    managed: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        gid = self.gid
        id = self.id
        managed = self.managed
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gid is not UNSET:
            field_dict["gid"] = gid
        if id is not UNSET:
            field_dict["id"] = id
        if managed is not UNSET:
            field_dict["managed"] = managed
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        gid = d.pop("gid", UNSET)

        id = d.pop("id", UNSET)

        managed = d.pop("managed", UNSET)

        name = d.pop("name", UNSET)

        posix_group = cls(
            gid=gid,
            id=id,
            managed=managed,
            name=name,
        )

        posix_group.additional_properties = d
        return posix_group

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
