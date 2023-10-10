from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AuthorityCSR")


@_attrs_define
class AuthorityCSR:
    """A certificate signing request for an X509 advanced authority with an external root.

    Attributes:
        authority_id (str): A UUID identifying the authority.
        csr (str): A certificate sigining request for the authority's intermediate issuer in pem format.
        id (str): A UUID identifying this CSR.
    """

    authority_id: str
    csr: str
    id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        authority_id = self.authority_id
        csr = self.csr
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authorityID": authority_id,
                "csr": csr,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        authority_id = d.pop("authorityID")

        csr = d.pop("csr")

        id = d.pop("id")

        authority_csr = cls(
            authority_id=authority_id,
            csr=csr,
            id=id,
        )

        authority_csr.additional_properties = d
        return authority_csr

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
