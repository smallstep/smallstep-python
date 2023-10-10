from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AzureVMDeviceType")


@_attrs_define
class AzureVMDeviceType:
    """
    Attributes:
        resource_groups (List[str]): The list of resource group names that are allowed to use this provisioner.
        tenant_id (str): The Azure account tenant ID for this provisioner. This ID is the Directory ID available in the
            Azure Active Directory properties.
        audience (Union[Unset, str]): Defaults to https://management.azure.com/ but it can be changed if necessary.
        disable_custom_sans (Union[Unset, bool]): By default custom SANs are valid, but if this option is set to `true`
            only the SANs available in the token will be valid, in Azure only the virtual machine name is available.
    """

    resource_groups: List[str]
    tenant_id: str
    audience: Union[Unset, str] = UNSET
    disable_custom_sans: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        resource_groups = self.resource_groups

        tenant_id = self.tenant_id
        audience = self.audience
        disable_custom_sans = self.disable_custom_sans

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resourceGroups": resource_groups,
                "tenantID": tenant_id,
            }
        )
        if audience is not UNSET:
            field_dict["audience"] = audience
        if disable_custom_sans is not UNSET:
            field_dict["disableCustomSANs"] = disable_custom_sans

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        resource_groups = cast(List[str], d.pop("resourceGroups"))

        tenant_id = d.pop("tenantID")

        audience = d.pop("audience", UNSET)

        disable_custom_sans = d.pop("disableCustomSANs", UNSET)

        azure_vm_device_type = cls(
            resource_groups=resource_groups,
            tenant_id=tenant_id,
            audience=audience,
            disable_custom_sans=disable_custom_sans,
        )

        azure_vm_device_type.additional_properties = d
        return azure_vm_device_type

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
