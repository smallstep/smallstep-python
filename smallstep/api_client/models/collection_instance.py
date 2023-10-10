import datetime
from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="CollectionInstance")


@_attrs_define
class CollectionInstance:
    """An instance in a collection.

    Attributes:
        created_at (datetime.datetime): Timestamp in RFC3339 format when the instance was added to the collection.
        data (Any): The instance data.
        id (str):
        updated_at (datetime.datetime): Timestamp in RFC3339 format when the instance was last changed.
    """

    created_at: datetime.datetime
    data: Any
    id: str
    updated_at: datetime.datetime
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        data = self.data
        id = self.id
        updated_at = self.updated_at.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "data": data,
                "id": id,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = isoparse(d.pop("createdAt"))

        data = d.pop("data")

        id = d.pop("id")

        updated_at = isoparse(d.pop("updatedAt"))

        collection_instance = cls(
            created_at=created_at,
            data=data,
            id=id,
            updated_at=updated_at,
        )

        collection_instance.additional_properties = d
        return collection_instance

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
