from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.device_collection_device_type import DeviceCollectionDeviceType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.awsvm_device_type import AWSVMDeviceType
    from ..models.azure_vm_device_type import AzureVMDeviceType
    from ..models.gcpvm_device_type import GCPVMDeviceType
    from ..models.tpm_device_type import TPMDeviceType


T = TypeVar("T", bound="DeviceCollection")


@_attrs_define
class DeviceCollection:
    """Configuration to create a new device collection.

    Attributes:
        device_type (DeviceCollectionDeviceType): Must match the deviceTypeConfiguration. Cannot be changed.
        device_type_configuration (Union['AWSVMDeviceType', 'AzureVMDeviceType', 'GCPVMDeviceType', 'TPMDeviceType']):
        display_name (str):
        slug (str):
        admin_emails (Union[Unset, List[str]]): Users that will have admin access to manage the agents authority, which
            will be created if it does not already exist. Ignored if the agent authority already exists. Never returned in
            API responses.
    """

    device_type: DeviceCollectionDeviceType
    device_type_configuration: Union["AWSVMDeviceType", "AzureVMDeviceType", "GCPVMDeviceType", "TPMDeviceType"]
    display_name: str
    slug: str
    admin_emails: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.awsvm_device_type import AWSVMDeviceType
        from ..models.azure_vm_device_type import AzureVMDeviceType
        from ..models.gcpvm_device_type import GCPVMDeviceType

        device_type = self.device_type.value

        device_type_configuration: Dict[str, Any]

        if isinstance(self.device_type_configuration, AWSVMDeviceType):
            device_type_configuration = self.device_type_configuration.to_dict()

        elif isinstance(self.device_type_configuration, AzureVMDeviceType):
            device_type_configuration = self.device_type_configuration.to_dict()

        elif isinstance(self.device_type_configuration, GCPVMDeviceType):
            device_type_configuration = self.device_type_configuration.to_dict()

        else:
            device_type_configuration = self.device_type_configuration.to_dict()

        display_name = self.display_name
        slug = self.slug
        admin_emails: Union[Unset, List[str]] = UNSET
        if not isinstance(self.admin_emails, Unset):
            admin_emails = self.admin_emails

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deviceType": device_type,
                "deviceTypeConfiguration": device_type_configuration,
                "displayName": display_name,
                "slug": slug,
            }
        )
        if admin_emails is not UNSET:
            field_dict["adminEmails"] = admin_emails

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.awsvm_device_type import AWSVMDeviceType
        from ..models.azure_vm_device_type import AzureVMDeviceType
        from ..models.gcpvm_device_type import GCPVMDeviceType
        from ..models.tpm_device_type import TPMDeviceType

        d = src_dict.copy()
        device_type = DeviceCollectionDeviceType(d.pop("deviceType"))

        def _parse_device_type_configuration(
            data: object,
        ) -> Union["AWSVMDeviceType", "AzureVMDeviceType", "GCPVMDeviceType", "TPMDeviceType"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                device_type_configuration_type_0 = AWSVMDeviceType.from_dict(data)

                return device_type_configuration_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                device_type_configuration_type_1 = AzureVMDeviceType.from_dict(data)

                return device_type_configuration_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                device_type_configuration_type_2 = GCPVMDeviceType.from_dict(data)

                return device_type_configuration_type_2
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            device_type_configuration_type_3 = TPMDeviceType.from_dict(data)

            return device_type_configuration_type_3

        device_type_configuration = _parse_device_type_configuration(d.pop("deviceTypeConfiguration"))

        display_name = d.pop("displayName")

        slug = d.pop("slug")

        admin_emails = cast(List[str], d.pop("adminEmails", UNSET))

        device_collection = cls(
            device_type=device_type,
            device_type_configuration=device_type_configuration,
            display_name=display_name,
            slug=slug,
            admin_emails=admin_emails,
        )

        device_collection.additional_properties = d
        return device_collection

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
