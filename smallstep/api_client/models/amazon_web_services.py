from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AmazonWebServices")


@_attrs_define
class AmazonWebServices:
    """Configuration for an AWS platform.

    Attributes:
        account_id (str):
        name (str): A friendly name for this AWS account.
        role_arn (Union[Unset, str]): A role ARN that allows the Smallstep Platform to manage resources on your behalf.
    """

    account_id: str
    name: str
    role_arn: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id

        name = self.name

        role_arn = self.role_arn

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
                "name": name,
            }
        )
        if role_arn is not UNSET:
            field_dict["roleArn"] = role_arn

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("accountId")

        name = d.pop("name")

        role_arn = d.pop("roleArn", UNSET)

        amazon_web_services = cls(
            account_id=account_id,
            name=name,
            role_arn=role_arn,
        )

        amazon_web_services.additional_properties = d
        return amazon_web_services

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
