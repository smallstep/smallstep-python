from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="BasicConstraints")


@_attrs_define
class BasicConstraints:
    """
    Attributes:
        is_ca (bool):
        max_path_len (int):
    """

    is_ca: bool
    max_path_len: int
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_ca = self.is_ca

        max_path_len = self.max_path_len

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isCA": is_ca,
                "maxPathLen": max_path_len,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_ca = d.pop("isCA")

        max_path_len = d.pop("maxPathLen")

        basic_constraints = cls(
            is_ca=is_ca,
            max_path_len=max_path_len,
        )

        basic_constraints.additional_properties = d
        return basic_constraints

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
