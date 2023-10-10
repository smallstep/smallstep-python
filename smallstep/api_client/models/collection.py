import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Collection")


@_attrs_define
class Collection:
    """A collection of instances.

    Example:
        {'createdAt': '2023-03-12T02:30:53.708Z', 'displayName': 'Employee Laptops', 'instanceCount': 23, 'slug':
            'devices', 'updatedAt': '2023-03-22T02:30:53.708Z'}

    Attributes:
        created_at (datetime.datetime): Timestamp in RFC3339 format when the collections was created
        display_name (str): A user-friendly name for the collection.
        instance_count (int): The number of instances in the collection.
        slug (str): A lowercase name identifying the collection.
        updated_at (datetime.datetime): Timestamp in RFC3339 format when the collections was last updated
        schema_uri (Union[Unset, str]): Reference to a schema that all instances in the collection must conform to.
    """

    created_at: datetime.datetime
    display_name: str
    instance_count: int
    slug: str
    updated_at: datetime.datetime
    schema_uri: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        display_name = self.display_name
        instance_count = self.instance_count
        slug = self.slug
        updated_at = self.updated_at.isoformat()

        schema_uri = self.schema_uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "displayName": display_name,
                "instanceCount": instance_count,
                "slug": slug,
                "updatedAt": updated_at,
            }
        )
        if schema_uri is not UNSET:
            field_dict["schemaURI"] = schema_uri

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = isoparse(d.pop("createdAt"))

        display_name = d.pop("displayName")

        instance_count = d.pop("instanceCount")

        slug = d.pop("slug")

        updated_at = isoparse(d.pop("updatedAt"))

        schema_uri = d.pop("schemaURI", UNSET)

        collection = cls(
            created_at=created_at,
            display_name=display_name,
            instance_count=instance_count,
            slug=slug,
            updated_at=updated_at,
            schema_uri=schema_uri,
        )

        collection.additional_properties = d
        return collection

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
