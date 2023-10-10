from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SSHCertificateData")


@_attrs_define
class SSHCertificateData:
    """Contains the information to include when granting an SSH certificate to a managed endpoint.

    Example:
        {'keyID': 'abc123', 'principals': ['ops', 'eng']}

    Attributes:
        key_id (str): The key ID to include in the endpoint certificate.
        principals (List[str]): The principals to include in the endpoint certificate.
    """

    key_id: str
    principals: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key_id = self.key_id
        principals = self.principals

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keyID": key_id,
                "principals": principals,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key_id = d.pop("keyID")

        principals = cast(List[str], d.pop("principals"))

        ssh_certificate_data = cls(
            key_id=key_id,
            principals=principals,
        )

        ssh_certificate_data.additional_properties = d
        return ssh_certificate_data

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
