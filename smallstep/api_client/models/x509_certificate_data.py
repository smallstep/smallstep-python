from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="X509CertificateData")


@_attrs_define
class X509CertificateData:
    """Contains the information to include when granting an x509 certificate to a managed endpoint.

    Example:
        {'commonName': 'db', 'sans': ['db', 'db.internal']}

    Attributes:
        common_name (str): The Common Name to be used in the subject of the endpoint certificate.
        sans (List[str]): The list of SANs to include in the endpoint certificate.
    """

    common_name: str
    sans: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        common_name = self.common_name
        sans = self.sans

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commonName": common_name,
                "sans": sans,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        common_name = d.pop("commonName")

        sans = cast(List[str], d.pop("sans"))

        x509_certificate_data = cls(
            common_name=common_name,
            sans=sans,
        )

        x509_certificate_data.additional_properties = d
        return x509_certificate_data

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
