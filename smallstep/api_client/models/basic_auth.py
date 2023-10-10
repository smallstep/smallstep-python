from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BasicAuth")


@_attrs_define
class BasicAuth:
    """Configures provisioner webhook requests to include an Authorization header with these credentials. Optional for
    `EXTERNAL` webhook servers; not allowed with hosted webhook servers. At most one of `bearerToken` and `basicAuth`
    may be set.

        Example:
            {'password': 'secret', 'username': 'user'}

        Attributes:
            password (str):
            username (str):
    """

    password: str
    username: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        password = self.password
        username = self.username

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "password": password,
                "username": username,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        password = d.pop("password")

        username = d.pop("username")

        basic_auth = cls(
            password=password,
            username=username,
        )

        basic_auth.additional_properties = d
        return basic_auth

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
