from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GoogleCloudPlatform")


@_attrs_define
class GoogleCloudPlatform:
    """Google Cloud Platform

    Attributes:
        name (str): A friendly name for this GCP connection
        project_ids (List[str]): The project IDs where the resources are located.
        service_account_key (Union[Unset, str]): A JSON-formatted service account key that allows the Smallstep Platform
            to manage resources on your behalf.
        service_accounts (Union[Unset, List[str]]): GCE service accounts that are allowed to enroll with the Smallstep
            Platform.
    """

    name: str
    project_ids: List[str]
    service_account_key: Union[Unset, str] = UNSET
    service_accounts: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        project_ids = self.project_ids

        service_account_key = self.service_account_key

        service_accounts: Union[Unset, List[str]] = UNSET
        if not isinstance(self.service_accounts, Unset):
            service_accounts = self.service_accounts

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "projectIds": project_ids,
            }
        )
        if service_account_key is not UNSET:
            field_dict["serviceAccountKey"] = service_account_key
        if service_accounts is not UNSET:
            field_dict["serviceAccounts"] = service_accounts

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        project_ids = cast(List[str], d.pop("projectIds"))

        service_account_key = d.pop("serviceAccountKey", UNSET)

        service_accounts = cast(List[str], d.pop("serviceAccounts", UNSET))

        google_cloud_platform = cls(
            name=name,
            project_ids=project_ids,
            service_account_key=service_account_key,
            service_accounts=service_accounts,
        )

        google_cloud_platform.additional_properties = d
        return google_cloud_platform

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
