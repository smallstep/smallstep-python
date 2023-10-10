from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.new_hosted_authority_type import NewHostedAuthorityType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.x509_issuer import X509Issuer


T = TypeVar("T", bound="NewHostedAuthority")


@_attrs_define
class NewHostedAuthority:
    """The body of a request to create a new authority.

    Attributes:
        admin_emails (List[str]): Users that will have admin access to manage the authority.
        name (str): The name of the authority.
        subdomain (str): The new authority will be available at <subdomain>.<team slug>.ca.smallstep.com.
        type (NewHostedAuthorityType): Create either a devops or advanced authority.
        active_revocation (Union[Unset, bool]): Whether to enable CRL and OCSP on an advanced authority.
        intermediate_issuer (Union[Unset, X509Issuer]): A Customized X509 issuer for an authority.
        root_issuer (Union[Unset, X509Issuer]): A Customized X509 issuer for an authority.
    """

    admin_emails: List[str]
    name: str
    subdomain: str
    type: NewHostedAuthorityType
    active_revocation: Union[Unset, bool] = UNSET
    intermediate_issuer: Union[Unset, "X509Issuer"] = UNSET
    root_issuer: Union[Unset, "X509Issuer"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        admin_emails = self.admin_emails

        name = self.name
        subdomain = self.subdomain
        type = self.type.value

        active_revocation = self.active_revocation
        intermediate_issuer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.intermediate_issuer, Unset):
            intermediate_issuer = self.intermediate_issuer.to_dict()

        root_issuer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.root_issuer, Unset):
            root_issuer = self.root_issuer.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "adminEmails": admin_emails,
                "name": name,
                "subdomain": subdomain,
                "type": type,
            }
        )
        if active_revocation is not UNSET:
            field_dict["activeRevocation"] = active_revocation
        if intermediate_issuer is not UNSET:
            field_dict["intermediateIssuer"] = intermediate_issuer
        if root_issuer is not UNSET:
            field_dict["rootIssuer"] = root_issuer

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.x509_issuer import X509Issuer

        d = src_dict.copy()
        admin_emails = cast(List[str], d.pop("adminEmails"))

        name = d.pop("name")

        subdomain = d.pop("subdomain")

        type = NewHostedAuthorityType(d.pop("type"))

        active_revocation = d.pop("activeRevocation", UNSET)

        _intermediate_issuer = d.pop("intermediateIssuer", UNSET)
        intermediate_issuer: Union[Unset, X509Issuer]
        if isinstance(_intermediate_issuer, Unset):
            intermediate_issuer = UNSET
        else:
            intermediate_issuer = X509Issuer.from_dict(_intermediate_issuer)

        _root_issuer = d.pop("rootIssuer", UNSET)
        root_issuer: Union[Unset, X509Issuer]
        if isinstance(_root_issuer, Unset):
            root_issuer = UNSET
        else:
            root_issuer = X509Issuer.from_dict(_root_issuer)

        new_hosted_authority = cls(
            admin_emails=admin_emails,
            name=name,
            subdomain=subdomain,
            type=type,
            active_revocation=active_revocation,
            intermediate_issuer=intermediate_issuer,
            root_issuer=root_issuer,
        )

        new_hosted_authority.additional_properties = d
        return new_hosted_authority

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
