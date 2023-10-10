from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.posix_group import POSIXGroup
    from ..models.ssh_host_grant import SSHHostGrant


T = TypeVar("T", bound="SSHGroup")


@_attrs_define
class SSHGroup:
    """A group is a set of users that have been synced from an identity provider.

    Attributes:
        host_grants (Union[Unset, List['SSHHostGrant']]):
        id (Union[Unset, str]): A UUID identifying the group.
        name (Union[Unset, str]): The name of the group.
        posix_groups (Union[Unset, List['POSIXGroup']]):
        principals (Union[Unset, List[str]]): Additional principals that will be appended to users' certilficates, in
            addition to the user's email and POSIX username.
    """

    host_grants: Union[Unset, List["SSHHostGrant"]] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    posix_groups: Union[Unset, List["POSIXGroup"]] = UNSET
    principals: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        host_grants: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.host_grants, Unset):
            host_grants = []
            for host_grants_item_data in self.host_grants:
                host_grants_item = host_grants_item_data.to_dict()

                host_grants.append(host_grants_item)

        id = self.id
        name = self.name
        posix_groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.posix_groups, Unset):
            posix_groups = []
            for posix_groups_item_data in self.posix_groups:
                posix_groups_item = posix_groups_item_data.to_dict()

                posix_groups.append(posix_groups_item)

        principals: Union[Unset, List[str]] = UNSET
        if not isinstance(self.principals, Unset):
            principals = self.principals

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host_grants is not UNSET:
            field_dict["hostGrants"] = host_grants
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if posix_groups is not UNSET:
            field_dict["posixGroups"] = posix_groups
        if principals is not UNSET:
            field_dict["principals"] = principals

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.posix_group import POSIXGroup
        from ..models.ssh_host_grant import SSHHostGrant

        d = src_dict.copy()
        host_grants = []
        _host_grants = d.pop("hostGrants", UNSET)
        for host_grants_item_data in _host_grants or []:
            host_grants_item = SSHHostGrant.from_dict(host_grants_item_data)

            host_grants.append(host_grants_item)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        posix_groups = []
        _posix_groups = d.pop("posixGroups", UNSET)
        for posix_groups_item_data in _posix_groups or []:
            posix_groups_item = POSIXGroup.from_dict(posix_groups_item_data)

            posix_groups.append(posix_groups_item)

        principals = cast(List[str], d.pop("principals", UNSET))

        ssh_group = cls(
            host_grants=host_grants,
            id=id,
            name=name,
            posix_groups=posix_groups,
            principals=principals,
        )

        ssh_group.additional_properties = d
        return ssh_group

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
