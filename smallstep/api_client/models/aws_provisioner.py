from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AWSProvisioner")


@_attrs_define
class AWSProvisioner:
    """The [AWS provisioner](https://smallstep.com/docs/step-ca/provisioners/#aws) grants a certificate to an Amazon EC2
    instance using the Instance Identity Document.

        Attributes:
            accounts (List[str]): The list of AWS account IDs that are allowed to use an AWS cloud provisioner.
            disable_custom_sans (Union[Unset, bool]): By default custom SANs are valid, but if this option is set to `true`
                only the SANs available in the instance identity document will be valid. These are the private IP and the DNS
                ip-<private-ip>.<region>.compute.internal.
            disable_trust_on_first_use (Union[Unset, bool]): By default only one certificate will be granted per instance,
                but if the option is set to `true` this limit is not set and different tokens can be used to get different
                certificates.
            instance_age (Union[Unset, str]): The maximum age of an instance that should be allowed to obtain a certificate.
                Limits certificate issuance to new instances to mitigate the risk of credential-misuse from instances that don't
                need a certificate. Parsed as a [Golang duration](https://pkg.go.dev/time#ParseDuration).
    """

    accounts: List[str]
    disable_custom_sans: Union[Unset, bool] = UNSET
    disable_trust_on_first_use: Union[Unset, bool] = UNSET
    instance_age: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        accounts = self.accounts

        disable_custom_sans = self.disable_custom_sans
        disable_trust_on_first_use = self.disable_trust_on_first_use
        instance_age = self.instance_age

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accounts": accounts,
            }
        )
        if disable_custom_sans is not UNSET:
            field_dict["disableCustomSANs"] = disable_custom_sans
        if disable_trust_on_first_use is not UNSET:
            field_dict["disableTrustOnFirstUse"] = disable_trust_on_first_use
        if instance_age is not UNSET:
            field_dict["instanceAge"] = instance_age

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        accounts = cast(List[str], d.pop("accounts"))

        disable_custom_sans = d.pop("disableCustomSANs", UNSET)

        disable_trust_on_first_use = d.pop("disableTrustOnFirstUse", UNSET)

        instance_age = d.pop("instanceAge", UNSET)

        aws_provisioner = cls(
            accounts=accounts,
            disable_custom_sans=disable_custom_sans,
            disable_trust_on_first_use=disable_trust_on_first_use,
            instance_age=instance_age,
        )

        aws_provisioner.additional_properties = d
        return aws_provisioner

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
