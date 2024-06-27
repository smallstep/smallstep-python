from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MicrosoftAzurePlatform")


@_attrs_define
class MicrosoftAzurePlatform:
    """Microsoft Azure

    Attributes:
        name (str): A friendly name for this Azure connection
        resource_groups (List[str]): A list of resource groups that are allowed to enroll with the Smallstep Platform.
        tenant_id (str): The Azure Entra tenant ID
        client_id (Union[Unset, str]): The client ID of an Azure Service Principal that allows the Smallstep Platform to
            manage resources on your behalf.
        client_secret (Union[Unset, str]): The client secret of an Azure Service Principal that allows the Smallstep
            Platform to manage resources on your behalf.
    """

    name: str
    resource_groups: List[str]
    tenant_id: str
    client_id: Union[Unset, str] = UNSET
    client_secret: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        resource_groups = self.resource_groups

        tenant_id = self.tenant_id

        client_id = self.client_id

        client_secret = self.client_secret

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "resourceGroups": resource_groups,
                "tenantId": tenant_id,
            }
        )
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if client_secret is not UNSET:
            field_dict["clientSecret"] = client_secret

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        resource_groups = cast(List[str], d.pop("resourceGroups"))

        tenant_id = d.pop("tenantId")

        client_id = d.pop("clientId", UNSET)

        client_secret = d.pop("clientSecret", UNSET)

        microsoft_azure_platform = cls(
            name=name,
            resource_groups=resource_groups,
            tenant_id=tenant_id,
            client_id=client_id,
            client_secret=client_secret,
        )

        microsoft_azure_platform.additional_properties = d
        return microsoft_azure_platform

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
