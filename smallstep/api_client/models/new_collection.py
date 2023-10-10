from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewCollection")


@_attrs_define
class NewCollection:
    """Body of a request to create a new collection.

    Example:
        {'displayName': 'Employee Laptops', 'slug': 'devices'}

    Attributes:
        slug (str): A lowercase name identifying the collection.
        display_name (Union[Unset, str]): A user-friendly name for the collection.
        schema_uri (Union[Unset, str]): Reference to a schema that all instances in the collection must conform to.
    """

    slug: str
    display_name: Union[Unset, str] = UNSET
    schema_uri: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        slug = self.slug
        display_name = self.display_name
        schema_uri = self.schema_uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "slug": slug,
            }
        )
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if schema_uri is not UNSET:
            field_dict["schemaURI"] = schema_uri

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        slug = d.pop("slug")

        display_name = d.pop("displayName", UNSET)

        schema_uri = d.pop("schemaURI", UNSET)

        new_collection = cls(
            slug=slug,
            display_name=display_name,
            schema_uri=schema_uri,
        )

        new_collection.additional_properties = d
        return new_collection

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
