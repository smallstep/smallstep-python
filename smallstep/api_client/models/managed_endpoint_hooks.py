from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.managed_endpoint_hook import ManagedEndpointHook


T = TypeVar("T", bound="ManagedEndpointHooks")


@_attrs_define
class ManagedEndpointHooks:
    """The collection of commands to run when a certificate for a managed endpoint is signed or renewed.

    Attributes:
        renew (Union[Unset, ManagedEndpointHook]): A list of commands to run before and after a certificate is granted.
            Example: {'after': ['echo done'], 'before': ['echo start'], 'onError': ['echo failed'], 'shell': '/bin/bash'}.
        sign (Union[Unset, ManagedEndpointHook]): A list of commands to run before and after a certificate is granted.
            Example: {'after': ['echo done'], 'before': ['echo start'], 'onError': ['echo failed'], 'shell': '/bin/bash'}.
    """

    renew: Union[Unset, "ManagedEndpointHook"] = UNSET
    sign: Union[Unset, "ManagedEndpointHook"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        renew: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.renew, Unset):
            renew = self.renew.to_dict()

        sign: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sign, Unset):
            sign = self.sign.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if renew is not UNSET:
            field_dict["renew"] = renew
        if sign is not UNSET:
            field_dict["sign"] = sign

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.managed_endpoint_hook import ManagedEndpointHook

        d = src_dict.copy()
        _renew = d.pop("renew", UNSET)
        renew: Union[Unset, ManagedEndpointHook]
        if isinstance(_renew, Unset):
            renew = UNSET
        else:
            renew = ManagedEndpointHook.from_dict(_renew)

        _sign = d.pop("sign", UNSET)
        sign: Union[Unset, ManagedEndpointHook]
        if isinstance(_sign, Unset):
            sign = UNSET
        else:
            sign = ManagedEndpointHook.from_dict(_sign)

        managed_endpoint_hooks = cls(
            renew=renew,
            sign=sign,
        )

        managed_endpoint_hooks.additional_properties = d
        return managed_endpoint_hooks

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
