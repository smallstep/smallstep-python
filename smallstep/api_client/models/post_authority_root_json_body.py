from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PostAuthorityRootJsonBody")


@_attrs_define
class PostAuthorityRootJsonBody:
    """
    Attributes:
        admin_emails (List[str]): Users that will have admin access to manage the authority
        id (str): The `id` returned from a previous call to `/authorities/csr`
        intermediate_pem (str): The signed intermediate certificate
        root_name (str): A name for the external root issuer
        root_pem (str): The root certificate in pem format
    """

    admin_emails: List[str]
    id: str
    intermediate_pem: str
    root_name: str
    root_pem: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        admin_emails = self.admin_emails

        id = self.id
        intermediate_pem = self.intermediate_pem
        root_name = self.root_name
        root_pem = self.root_pem

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "adminEmails": admin_emails,
                "id": id,
                "intermediatePEM": intermediate_pem,
                "rootName": root_name,
                "rootPEM": root_pem,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        admin_emails = cast(List[str], d.pop("adminEmails"))

        id = d.pop("id")

        intermediate_pem = d.pop("intermediatePEM")

        root_name = d.pop("rootName")

        root_pem = d.pop("rootPEM")

        post_authority_root_json_body = cls(
            admin_emails=admin_emails,
            id=id,
            intermediate_pem=intermediate_pem,
            root_name=root_name,
            root_pem=root_pem,
        )

        post_authority_root_json_body.additional_properties = d
        return post_authority_root_json_body

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
