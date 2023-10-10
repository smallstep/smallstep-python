from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="POSIXUser")


@_attrs_define
class POSIXUser:
    """A POSIX user is the login user on the SSH Host. It will be generated automatically if not supplied by the team's
    Identity Provider.

        Attributes:
            gid (Union[Unset, int]): The numeric group ID of the user.
            home_dir (Union[Unset, str]): The user's home directory.
            shell (Union[Unset, str]): The user's shell.
            uid (Union[Unset, int]): The numeric ID of the user.
            username (Union[Unset, str]): The login name of the user.
    """

    gid: Union[Unset, int] = UNSET
    home_dir: Union[Unset, str] = UNSET
    shell: Union[Unset, str] = UNSET
    uid: Union[Unset, int] = UNSET
    username: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        gid = self.gid
        home_dir = self.home_dir
        shell = self.shell
        uid = self.uid
        username = self.username

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gid is not UNSET:
            field_dict["gid"] = gid
        if home_dir is not UNSET:
            field_dict["homeDir"] = home_dir
        if shell is not UNSET:
            field_dict["shell"] = shell
        if uid is not UNSET:
            field_dict["uid"] = uid
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        gid = d.pop("gid", UNSET)

        home_dir = d.pop("homeDir", UNSET)

        shell = d.pop("shell", UNSET)

        uid = d.pop("uid", UNSET)

        username = d.pop("username", UNSET)

        posix_user = cls(
            gid=gid,
            home_dir=home_dir,
            shell=shell,
            uid=uid,
            username=username,
        )

        posix_user.additional_properties = d
        return posix_user

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
