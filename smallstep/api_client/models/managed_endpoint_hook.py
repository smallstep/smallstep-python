from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ManagedEndpointHook")


@_attrs_define
class ManagedEndpointHook:
    """A list of commands to run before and after a certificate is granted.

    Example:
        {'after': ['echo done'], 'before': ['echo start'], 'onError': ['echo failed'], 'shell': '/bin/bash'}

    Attributes:
        after (Union[Unset, List[str]]): List of commands to run after the operation.
        before (Union[Unset, List[str]]): List of commands to run before the operation.
        on_error (Union[Unset, List[str]]): List of commands to run when the operation fails.
        shell (Union[Unset, str]): The shell to use to execute the commands.
    """

    after: Union[Unset, List[str]] = UNSET
    before: Union[Unset, List[str]] = UNSET
    on_error: Union[Unset, List[str]] = UNSET
    shell: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        after: Union[Unset, List[str]] = UNSET
        if not isinstance(self.after, Unset):
            after = self.after

        before: Union[Unset, List[str]] = UNSET
        if not isinstance(self.before, Unset):
            before = self.before

        on_error: Union[Unset, List[str]] = UNSET
        if not isinstance(self.on_error, Unset):
            on_error = self.on_error

        shell = self.shell

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if after is not UNSET:
            field_dict["after"] = after
        if before is not UNSET:
            field_dict["before"] = before
        if on_error is not UNSET:
            field_dict["onError"] = on_error
        if shell is not UNSET:
            field_dict["shell"] = shell

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        after = cast(List[str], d.pop("after", UNSET))

        before = cast(List[str], d.pop("before", UNSET))

        on_error = cast(List[str], d.pop("onError", UNSET))

        shell = d.pop("shell", UNSET)

        managed_endpoint_hook = cls(
            after=after,
            before=before,
            on_error=on_error,
            shell=shell,
        )

        managed_endpoint_hook.additional_properties = d
        return managed_endpoint_hook

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
