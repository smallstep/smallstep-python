from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.x509_issuer import X509Issuer


T = TypeVar("T", bound="NewAuthorityCSR")


@_attrs_define
class NewAuthorityCSR:
    """Body of a request to create a new X509 advanced authority with an external root.

    Attributes:
        intermediate_issuer (X509Issuer): A Customized X509 issuer for an authority.
        name (str): The name of the authority.
        subdomain (str): The new authority will be available at <subdomain>.<team slug>.ca.smallstep.com.
        active_revocation (Union[Unset, bool]): Whether to enable CRL and OCSP on the authority.
    """

    intermediate_issuer: "X509Issuer"
    name: str
    subdomain: str
    active_revocation: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        intermediate_issuer = self.intermediate_issuer.to_dict()

        name = self.name
        subdomain = self.subdomain
        active_revocation = self.active_revocation

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "intermediateIssuer": intermediate_issuer,
                "name": name,
                "subdomain": subdomain,
            }
        )
        if active_revocation is not UNSET:
            field_dict["activeRevocation"] = active_revocation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.x509_issuer import X509Issuer

        d = src_dict.copy()
        intermediate_issuer = X509Issuer.from_dict(d.pop("intermediateIssuer"))

        name = d.pop("name")

        subdomain = d.pop("subdomain")

        active_revocation = d.pop("activeRevocation", UNSET)

        new_authority_csr = cls(
            intermediate_issuer=intermediate_issuer,
            name=name,
            subdomain=subdomain,
            active_revocation=active_revocation,
        )

        new_authority_csr.additional_properties = d
        return new_authority_csr

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
