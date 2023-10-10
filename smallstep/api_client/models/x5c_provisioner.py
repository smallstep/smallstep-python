from typing import Any, Dict, List, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="X5CProvisioner")


@_attrs_define
class X5CProvisioner:
    """A [provisioner](https://smallstep.com/docs/step-ca/provisioners/#x5c---x509-certificate) that authenticates a
    certificate request with an existing x509 certificate.

        Attributes:
            roots (List[str]): A list of pem-encoded x509 certificates. Any certificate bundle that chains up to any of
                these roots can be used in a certificate request.
    """

    roots: List[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        roots = self.roots

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "roots": roots,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        roots = cast(List[str], d.pop("roots"))

        x5c_provisioner = cls(
            roots=roots,
        )

        x5c_provisioner.additional_properties = d
        return x5c_provisioner

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
