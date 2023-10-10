import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ssh_host_tag import SSHHostTag


T = TypeVar("T", bound="SSHHost")


@_attrs_define
class SSHHost:
    """A host where Smallstep has been installed to manage SSH access.

    Attributes:
        active (Union[Unset, bool]): A host is active until it is unregistered.
        bastion (Union[Unset, bool]): Whether or not this host is a bastion.
        bastion_hostname (Union[Unset, str]): The hostname of the bastion server required to access this host, if any.
        created_at (Union[Unset, datetime.datetime]): Timestamp in RFC3339 format when the host was registered.
        hostname (Union[Unset, str]): The hostname detected during installation.
        id (Union[Unset, str]): A UUID identifying this host.
        tags (Union[Unset, List['SSHHostTag']]):
        updated_at (Union[Unset, datetime.datetime]): Timestamp in RFC3339 format when the host was last updated.
    """

    active: Union[Unset, bool] = UNSET
    bastion: Union[Unset, bool] = UNSET
    bastion_hostname: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    hostname: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    tags: Union[Unset, List["SSHHostTag"]] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active = self.active
        bastion = self.bastion
        bastion_hostname = self.bastion_hostname
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        hostname = self.hostname
        id = self.id
        tags: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()

                tags.append(tags_item)

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if bastion is not UNSET:
            field_dict["bastion"] = bastion
        if bastion_hostname is not UNSET:
            field_dict["bastionHostname"] = bastion_hostname
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if id is not UNSET:
            field_dict["id"] = id
        if tags is not UNSET:
            field_dict["tags"] = tags
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ssh_host_tag import SSHHostTag

        d = src_dict.copy()
        active = d.pop("active", UNSET)

        bastion = d.pop("bastion", UNSET)

        bastion_hostname = d.pop("bastionHostname", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        hostname = d.pop("hostname", UNSET)

        id = d.pop("id", UNSET)

        tags = []
        _tags = d.pop("tags", UNSET)
        for tags_item_data in _tags or []:
            tags_item = SSHHostTag.from_dict(tags_item_data)

            tags.append(tags_item)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        ssh_host = cls(
            active=active,
            bastion=bastion,
            bastion_hostname=bastion_hostname,
            created_at=created_at,
            hostname=hostname,
            id=id,
            tags=tags,
            updated_at=updated_at,
        )

        ssh_host.additional_properties = d
        return ssh_host

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
