from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AWSVMDeviceType")


@_attrs_define
class AWSVMDeviceType:
    """Configuration for an AWS provisioner for a device collection of AWS VMs.

    Attributes:
        accounts (List[str]): The list of AWS account IDs that are allowed to use an AWS cloud provisioner.
        disable_custom_sans (Union[Unset, bool]): By default custom SANs are valid, but if this option is set to `true`
            only the SANs available in the instance identity document will be valid. These are the private IP and the DNS
            ip-<private-ip>.<region>.compute.internal.
    """

    accounts: List[str]
    disable_custom_sans: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        accounts = self.accounts

        disable_custom_sans = self.disable_custom_sans

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accounts": accounts,
            }
        )
        if disable_custom_sans is not UNSET:
            field_dict["disableCustomSANs"] = disable_custom_sans

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        accounts = cast(List[str], d.pop("accounts"))

        disable_custom_sans = d.pop("disableCustomSANs", UNSET)

        awsvm_device_type = cls(
            accounts=accounts,
            disable_custom_sans=disable_custom_sans,
        )

        awsvm_device_type.additional_properties = d
        return awsvm_device_type

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
