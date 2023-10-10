from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JWKProvisioner")


@_attrs_define
class JWKProvisioner:
    """A [provisioner](https://smallstep.com/docs/step-ca/provisioners/#jwk) that uses public-key cryptography to sign and
    validate a JSON Web Token (JWT).

        Attributes:
            key (Any): The public JSON web key.
            encrypted_key (Union[Unset, str]): The JWE encrypted private key.
    """

    key: Any
    encrypted_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key
        encrypted_key = self.encrypted_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
            }
        )
        if encrypted_key is not UNSET:
            field_dict["encryptedKey"] = encrypted_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key")

        encrypted_key = d.pop("encryptedKey", UNSET)

        jwk_provisioner = cls(
            key=key,
            encrypted_key=encrypted_key,
        )

        jwk_provisioner.additional_properties = d
        return jwk_provisioner

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
