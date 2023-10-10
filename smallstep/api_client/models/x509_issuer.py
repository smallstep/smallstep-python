from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.x509_issuer_key_version import X509IssuerKeyVersion
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.distinguished_name import DistinguishedName
    from ..models.name_constraints import NameConstraints


T = TypeVar("T", bound="X509Issuer")


@_attrs_define
class X509Issuer:
    """A Customized X509 issuer for an authority.

    Attributes:
        key_version (X509IssuerKeyVersion): The signature algorithm.
        name (str): The name of the issuer.
        duration (Union[Unset, str]): The certificate lifetime. Parsed as a [Golang
            duration](https://pkg.go.dev/time#ParseDuration).
        max_path_length (Union[Unset, int]):
        name_constraints (Union[Unset, NameConstraints]): X509 certificate name constratins.
        subject (Union[Unset, DistinguishedName]): Name used in x509 certificates
             Example: [{'organization': 'admins'}].
    """

    key_version: X509IssuerKeyVersion
    name: str
    duration: Union[Unset, str] = UNSET
    max_path_length: Union[Unset, int] = UNSET
    name_constraints: Union[Unset, "NameConstraints"] = UNSET
    subject: Union[Unset, "DistinguishedName"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key_version = self.key_version.value

        name = self.name
        duration = self.duration
        max_path_length = self.max_path_length
        name_constraints: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.name_constraints, Unset):
            name_constraints = self.name_constraints.to_dict()

        subject: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.subject, Unset):
            subject = self.subject.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "keyVersion": key_version,
                "name": name,
            }
        )
        if duration is not UNSET:
            field_dict["duration"] = duration
        if max_path_length is not UNSET:
            field_dict["maxPathLength"] = max_path_length
        if name_constraints is not UNSET:
            field_dict["nameConstraints"] = name_constraints
        if subject is not UNSET:
            field_dict["subject"] = subject

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.distinguished_name import DistinguishedName
        from ..models.name_constraints import NameConstraints

        d = src_dict.copy()
        key_version = X509IssuerKeyVersion(d.pop("keyVersion"))

        name = d.pop("name")

        duration = d.pop("duration", UNSET)

        max_path_length = d.pop("maxPathLength", UNSET)

        _name_constraints = d.pop("nameConstraints", UNSET)
        name_constraints: Union[Unset, NameConstraints]
        if isinstance(_name_constraints, Unset):
            name_constraints = UNSET
        else:
            name_constraints = NameConstraints.from_dict(_name_constraints)

        _subject = d.pop("subject", UNSET)
        subject: Union[Unset, DistinguishedName]
        if isinstance(_subject, Unset):
            subject = UNSET
        else:
            subject = DistinguishedName.from_dict(_subject)

        x509_issuer = cls(
            key_version=key_version,
            name=name,
            duration=duration,
            max_path_length=max_path_length,
            name_constraints=name_constraints,
            subject=subject,
        )

        x509_issuer.additional_properties = d
        return x509_issuer

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
