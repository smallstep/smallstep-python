from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceEnrollmentToken")


@_attrs_define
class DeviceEnrollmentToken:
    """A JWT that can be used to enroll devices with the Smallstep Agent

    Example:
        {'id': 'a94fa793-7e2a-40b4-b0fe-ccee7c4afc4a', 'secret': 'eyJh...F2I', 'title': 'Enrollment token for
            i-01234567890'}

    Attributes:
        id (Union[Unset, str]): The unique identifier of the token
        secret (Union[Unset, str]): The JWT itself; this value cannot be retrieved after initially generated and should
            be kept secret
        title (Union[Unset, str]): The name of the token
    """

    id: Union[Unset, str] = UNSET
    secret: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        secret = self.secret
        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if secret is not UNSET:
            field_dict["secret"] = secret
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        secret = d.pop("secret", UNSET)

        title = d.pop("title", UNSET)

        device_enrollment_token = cls(
            id=id,
            secret=secret,
            title=title,
        )

        device_enrollment_token.additional_properties = d
        return device_enrollment_token

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
