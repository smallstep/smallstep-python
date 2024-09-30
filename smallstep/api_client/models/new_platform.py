from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.new_platform_platform_type import NewPlatformPlatformType

if TYPE_CHECKING:
    from ..models.amazon_web_services import AmazonWebServices
    from ..models.google_cloud_platform import GoogleCloudPlatform
    from ..models.microsoft_azure_platform import MicrosoftAzurePlatform


T = TypeVar("T", bound="NewPlatform")


@_attrs_define
class NewPlatform:
    """Configuration to create a new platform.

    Attributes:
        display_name (str):
        platform_configuration (Union['AmazonWebServices', 'GoogleCloudPlatform', 'MicrosoftAzurePlatform']):
        platform_type (NewPlatformPlatformType): Determines which set of fields to use in platformConfiguration. Cannot
            be changed.
        slug (str):
    """

    display_name: str
    platform_configuration: Union["AmazonWebServices", "GoogleCloudPlatform", "MicrosoftAzurePlatform"]
    platform_type: NewPlatformPlatformType
    slug: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.amazon_web_services import AmazonWebServices
        from ..models.microsoft_azure_platform import MicrosoftAzurePlatform

        display_name = self.display_name

        platform_configuration: Dict[str, Any]
        if isinstance(self.platform_configuration, AmazonWebServices):
            platform_configuration = self.platform_configuration.to_dict()
        elif isinstance(self.platform_configuration, MicrosoftAzurePlatform):
            platform_configuration = self.platform_configuration.to_dict()
        else:
            platform_configuration = self.platform_configuration.to_dict()

        platform_type = self.platform_type.value

        slug = self.slug

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayName": display_name,
                "platformConfiguration": platform_configuration,
                "platformType": platform_type,
                "slug": slug,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.amazon_web_services import AmazonWebServices
        from ..models.google_cloud_platform import GoogleCloudPlatform
        from ..models.microsoft_azure_platform import MicrosoftAzurePlatform

        d = src_dict.copy()
        display_name = d.pop("displayName")

        def _parse_platform_configuration(
            data: object,
        ) -> Union["AmazonWebServices", "GoogleCloudPlatform", "MicrosoftAzurePlatform"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                platform_configuration_type_0 = AmazonWebServices.from_dict(data)

                return platform_configuration_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                platform_configuration_type_1 = MicrosoftAzurePlatform.from_dict(data)

                return platform_configuration_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            platform_configuration_type_2 = GoogleCloudPlatform.from_dict(data)

            return platform_configuration_type_2

        platform_configuration = _parse_platform_configuration(d.pop("platformConfiguration"))

        platform_type = NewPlatformPlatformType(d.pop("platformType"))

        slug = d.pop("slug")

        new_platform = cls(
            display_name=display_name,
            platform_configuration=platform_configuration,
            platform_type=platform_type,
            slug=slug,
        )

        new_platform.additional_properties = d
        return new_platform

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
