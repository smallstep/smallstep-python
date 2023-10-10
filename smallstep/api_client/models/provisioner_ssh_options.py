from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProvisionerSSHOptions")


@_attrs_define
class ProvisionerSSHOptions:
    """Options that apply when issuing SSH certificates

    Example:
        {'template': '{"type": {{ toJson .Type }}, "keyId": {{ toJson .KeyID }}, "principals": {{ toJson .Principals }},
            "extensions": {{ toJson .Extensions }}, "criticalOptions": {{ toJson .CriticalOptions }} }', 'templateData':
            {'principals': ['eng', 'ops']}}

    Attributes:
        template (Union[Unset, str]): A JSON representation of the SSH certificate to be created. [More
            info](https://smallstep.com/docs/step-ca/templates/#ssh-templates).
        template_data (Union[Unset, Any]): A map of data that can be used by the certificate template.
    """

    template: Union[Unset, str] = UNSET
    template_data: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        template = self.template
        template_data = self.template_data

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if template is not UNSET:
            field_dict["template"] = template
        if template_data is not UNSET:
            field_dict["templateData"] = template_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        template = d.pop("template", UNSET)

        template_data = d.pop("templateData", UNSET)

        provisioner_ssh_options = cls(
            template=template,
            template_data=template_data,
        )

        provisioner_ssh_options.additional_properties = d
        return provisioner_ssh_options

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
