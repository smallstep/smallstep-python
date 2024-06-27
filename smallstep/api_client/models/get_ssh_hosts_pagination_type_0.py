from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetSshHostsPaginationType0")


@_attrs_define
class GetSshHostsPaginationType0:
    """
    Attributes:
        after (Union[None, Unset, str]): Fetch a page of results other than the first page.
            Must be copied from a previously returned X-Next-Cursor header.
             Example: MTIzNA==.
        first (Union[None, Unset, int]): Limits the number of results returned.
            Defaults to 100.
             Example: 30.
    """

    after: Union[None, Unset, str] = UNSET
    first: Union[None, Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        after: Union[None, Unset, str]
        if isinstance(self.after, Unset):
            after = UNSET
        else:
            after = self.after

        first: Union[None, Unset, int]
        if isinstance(self.first, Unset):
            first = UNSET
        else:
            first = self.first

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if after is not UNSET:
            field_dict["after"] = after
        if first is not UNSET:
            field_dict["first"] = first

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_after(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        after = _parse_after(d.pop("after", UNSET))

        def _parse_first(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        first = _parse_first(d.pop("first", UNSET))

        get_ssh_hosts_pagination_type_0 = cls(
            after=after,
            first=first,
        )

        get_ssh_hosts_pagination_type_0.additional_properties = d
        return get_ssh_hosts_pagination_type_0

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
