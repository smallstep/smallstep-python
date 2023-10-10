from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GCPVMDeviceType")


@_attrs_define
class GCPVMDeviceType:
    """Configuration for the GCP provisioner for device collections of GCP instances. At least one service account or
    project ID must be set.

        Attributes:
            disable_custom_sans (Union[Unset, bool]): By default custom SANs are valid, but if this option is set to `true`
                only the SANs available in the instance identity document will be valid, these are the DNS `<instance-
                name>.c.<project-id>.internal` and `<instance-name>.<zone>.c.<project-id>.internal`.
            project_ids (Union[Unset, List[str]]): The list of project identifiers that are allowed to use a GCP cloud
                provisioner.
            service_accounts (Union[Unset, List[str]]): The list of service accounts that are allowed to use a GCP cloud
                provisioner.
    """

    disable_custom_sans: Union[Unset, bool] = UNSET
    project_ids: Union[Unset, List[str]] = UNSET
    service_accounts: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        disable_custom_sans = self.disable_custom_sans
        project_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.project_ids, Unset):
            project_ids = self.project_ids

        service_accounts: Union[Unset, List[str]] = UNSET
        if not isinstance(self.service_accounts, Unset):
            service_accounts = self.service_accounts

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if disable_custom_sans is not UNSET:
            field_dict["disableCustomSANs"] = disable_custom_sans
        if project_ids is not UNSET:
            field_dict["projectIDs"] = project_ids
        if service_accounts is not UNSET:
            field_dict["serviceAccounts"] = service_accounts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        disable_custom_sans = d.pop("disableCustomSANs", UNSET)

        project_ids = cast(List[str], d.pop("projectIDs", UNSET))

        service_accounts = cast(List[str], d.pop("serviceAccounts", UNSET))

        gcpvm_device_type = cls(
            disable_custom_sans=disable_custom_sans,
            project_ids=project_ids,
            service_accounts=service_accounts,
        )

        gcpvm_device_type.additional_properties = d
        return gcpvm_device_type

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
