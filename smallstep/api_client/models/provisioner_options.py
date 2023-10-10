from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provisioner_ssh_options import ProvisionerSSHOptions
    from ..models.provisioner_webhook import ProvisionerWebhook
    from ..models.provisioner_x509_options import ProvisionerX509Options


T = TypeVar("T", bound="ProvisionerOptions")


@_attrs_define
class ProvisionerOptions:
    """Options that apply when issuing certificates with this provisioner.

    Attributes:
        ssh (Union[Unset, ProvisionerSSHOptions]): Options that apply when issuing SSH certificates Example:
            {'template': '{"type": {{ toJson .Type }}, "keyId": {{ toJson .KeyID }}, "principals": {{ toJson .Principals }},
            "extensions": {{ toJson .Extensions }}, "criticalOptions": {{ toJson .CriticalOptions }} }', 'templateData':
            {'principals': ['eng', 'ops']}}.
        webhooks (Union[Unset, List['ProvisionerWebhook']]):
        x509 (Union[Unset, ProvisionerX509Options]): Options that apply when issuing x509 certificates. Example:
            {'template': '{"subject": {{ toJson .Subject }}, "sans": {{ toJson .SANs }}, "keyUsage": ["digitalSignature"],
            "extKeyUsage": ["serverAuth", "clientAuth"]}', 'templateData': {'defaultOrg': 'eng'}}.
    """

    ssh: Union[Unset, "ProvisionerSSHOptions"] = UNSET
    webhooks: Union[Unset, List["ProvisionerWebhook"]] = UNSET
    x509: Union[Unset, "ProvisionerX509Options"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ssh: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ssh, Unset):
            ssh = self.ssh.to_dict()

        webhooks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.webhooks, Unset):
            webhooks = []
            for webhooks_item_data in self.webhooks:
                webhooks_item = webhooks_item_data.to_dict()

                webhooks.append(webhooks_item)

        x509: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.x509, Unset):
            x509 = self.x509.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ssh is not UNSET:
            field_dict["ssh"] = ssh
        if webhooks is not UNSET:
            field_dict["webhooks"] = webhooks
        if x509 is not UNSET:
            field_dict["x509"] = x509

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.provisioner_ssh_options import ProvisionerSSHOptions
        from ..models.provisioner_webhook import ProvisionerWebhook
        from ..models.provisioner_x509_options import ProvisionerX509Options

        d = src_dict.copy()
        _ssh = d.pop("ssh", UNSET)
        ssh: Union[Unset, ProvisionerSSHOptions]
        if isinstance(_ssh, Unset):
            ssh = UNSET
        else:
            ssh = ProvisionerSSHOptions.from_dict(_ssh)

        webhooks = []
        _webhooks = d.pop("webhooks", UNSET)
        for webhooks_item_data in _webhooks or []:
            webhooks_item = ProvisionerWebhook.from_dict(webhooks_item_data)

            webhooks.append(webhooks_item)

        _x509 = d.pop("x509", UNSET)
        x509: Union[Unset, ProvisionerX509Options]
        if isinstance(_x509, Unset):
            x509 = UNSET
        else:
            x509 = ProvisionerX509Options.from_dict(_x509)

        provisioner_options = cls(
            ssh=ssh,
            webhooks=webhooks,
            x509=x509,
        )

        provisioner_options.additional_properties = d
        return provisioner_options

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
