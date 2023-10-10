from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.email import Email
    from ..models.posix_user import POSIXUser
    from ..models.ssh_group import SSHGroup


T = TypeVar("T", bound="SSHUser")


@_attrs_define
class SSHUser:
    """SSH Users are synced from the team's Identity Provider, or from the default Smallstep directory if no external
    Identity Provider has been configured.

        Attributes:
            active (Union[Unset, bool]): Whether the user has been deactivated in the team's Identity Provider.
            display_name (Union[Unset, str]): The user's display name.
            emails (Union[Unset, List['Email']]):
            family_name (Union[Unset, str]): The user's family name.
            given_name (Union[Unset, str]): The user's given name.
            groups (Union[Unset, List['SSHGroup']]):
            id (Union[Unset, str]): A UUID identifying the user.
            posix_users (Union[Unset, List['POSIXUser']]):
    """

    active: Union[Unset, bool] = UNSET
    display_name: Union[Unset, str] = UNSET
    emails: Union[Unset, List["Email"]] = UNSET
    family_name: Union[Unset, str] = UNSET
    given_name: Union[Unset, str] = UNSET
    groups: Union[Unset, List["SSHGroup"]] = UNSET
    id: Union[Unset, str] = UNSET
    posix_users: Union[Unset, List["POSIXUser"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        active = self.active
        display_name = self.display_name
        emails: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.emails, Unset):
            emails = []
            for emails_item_data in self.emails:
                emails_item = emails_item_data.to_dict()

                emails.append(emails_item)

        family_name = self.family_name
        given_name = self.given_name
        groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()

                groups.append(groups_item)

        id = self.id
        posix_users: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.posix_users, Unset):
            posix_users = []
            for posix_users_item_data in self.posix_users:
                posix_users_item = posix_users_item_data.to_dict()

                posix_users.append(posix_users_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if emails is not UNSET:
            field_dict["emails"] = emails
        if family_name is not UNSET:
            field_dict["familyName"] = family_name
        if given_name is not UNSET:
            field_dict["givenName"] = given_name
        if groups is not UNSET:
            field_dict["groups"] = groups
        if id is not UNSET:
            field_dict["id"] = id
        if posix_users is not UNSET:
            field_dict["posixUsers"] = posix_users

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.email import Email
        from ..models.posix_user import POSIXUser
        from ..models.ssh_group import SSHGroup

        d = src_dict.copy()
        active = d.pop("active", UNSET)

        display_name = d.pop("displayName", UNSET)

        emails = []
        _emails = d.pop("emails", UNSET)
        for emails_item_data in _emails or []:
            emails_item = Email.from_dict(emails_item_data)

            emails.append(emails_item)

        family_name = d.pop("familyName", UNSET)

        given_name = d.pop("givenName", UNSET)

        groups = []
        _groups = d.pop("groups", UNSET)
        for groups_item_data in _groups or []:
            groups_item = SSHGroup.from_dict(groups_item_data)

            groups.append(groups_item)

        id = d.pop("id", UNSET)

        posix_users = []
        _posix_users = d.pop("posixUsers", UNSET)
        for posix_users_item_data in _posix_users or []:
            posix_users_item = POSIXUser.from_dict(posix_users_item_data)

            posix_users.append(posix_users_item)

        ssh_user = cls(
            active=active,
            display_name=display_name,
            emails=emails,
            family_name=family_name,
            given_name=given_name,
            groups=groups,
            id=id,
            posix_users=posix_users,
        )

        ssh_user.additional_properties = d
        return ssh_user

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
