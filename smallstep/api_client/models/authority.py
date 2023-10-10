import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.authority_type import AuthorityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Authority")


@_attrs_define
class Authority:
    """An X509 authority hosted by Smallstep.

    Attributes:
        created_at (datetime.datetime): Timestamp when the authority was created.
        domain (str): The domain where the authority can be reached.
        id (str): A UUID identifying this authority.
        name (str): The name of the authority.
        type (AuthorityType): One of the available authority types
        active_revocation (Union[Unset, bool]): Whether CRL and OCSP are enabled (advanced authorities only).
        admin_emails (Union[Unset, List[str]]): Users that have admin access to manage the authority.
        fingerprint (Union[Unset, str]): The SHA-256 digest of the authority's root certificate in hex format.
        root (Union[Unset, str]): The root certificate in pem format.
    """

    created_at: datetime.datetime
    domain: str
    id: str
    name: str
    type: AuthorityType
    active_revocation: Union[Unset, bool] = UNSET
    admin_emails: Union[Unset, List[str]] = UNSET
    fingerprint: Union[Unset, str] = UNSET
    root: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at.isoformat()

        domain = self.domain
        id = self.id
        name = self.name
        type = self.type.value

        active_revocation = self.active_revocation
        admin_emails: Union[Unset, List[str]] = UNSET
        if not isinstance(self.admin_emails, Unset):
            admin_emails = self.admin_emails

        fingerprint = self.fingerprint
        root = self.root

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "createdAt": created_at,
                "domain": domain,
                "id": id,
                "name": name,
                "type": type,
            }
        )
        if active_revocation is not UNSET:
            field_dict["activeRevocation"] = active_revocation
        if admin_emails is not UNSET:
            field_dict["adminEmails"] = admin_emails
        if fingerprint is not UNSET:
            field_dict["fingerprint"] = fingerprint
        if root is not UNSET:
            field_dict["root"] = root

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = isoparse(d.pop("createdAt"))

        domain = d.pop("domain")

        id = d.pop("id")

        name = d.pop("name")

        type = AuthorityType(d.pop("type"))

        active_revocation = d.pop("activeRevocation", UNSET)

        admin_emails = cast(List[str], d.pop("adminEmails", UNSET))

        fingerprint = d.pop("fingerprint", UNSET)

        root = d.pop("root", UNSET)

        authority = cls(
            created_at=created_at,
            domain=domain,
            id=id,
            name=name,
            type=type,
            active_revocation=active_revocation,
            admin_emails=admin_emails,
            fingerprint=fingerprint,
            root=root,
        )

        authority.additional_properties = d
        return authority

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
