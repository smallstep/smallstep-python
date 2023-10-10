from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.endpoint_configuration_kind import EndpointConfigurationKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.managed_endpoint_certificate_info import ManagedEndpointCertificateInfo
    from ..models.managed_endpoint_hooks import ManagedEndpointHooks
    from ..models.managed_endpoint_key_info import ManagedEndpointKeyInfo
    from ..models.managed_endpoint_reload_info import ManagedEndpointReloadInfo


T = TypeVar("T", bound="EndpointConfiguration")


@_attrs_define
class EndpointConfiguration:
    """Configuration for a managed endpoint. This object is experimental and subject to change.

    Example:
        {'authorityID': '8e3ff498-2059-4859-9053-c334ceab5f83', 'certificateInfo': {'crtFile': '/etc/db.crt',
            'duration': '24h0m0s', 'gid': 999, 'keyFile': '/etc/db.key', 'mode': 256, 'rootFile': '/etc/ca.crt', 'type':
            'X509', 'uid': 1001}, 'hooks': {'renew': {'after': ['echo renewed'], 'before': ['echo renewing'], 'onError':
            ['echo failed to renew'], 'shell': '/bin/bash'}, 'sign': {'after': ['echo signed'], 'before': ['echo signing'],
            'onError': ['echo failed to sign'], 'shell': '/bin/bash'}}, 'id': 'd9dd9ca8-8624-4eca-84e9-ee3dd74c1786',
            'keyInfo': {'format': 'DER', 'pubFile': '/etc/db.csr', 'type': 'ECDSA_P256'}, 'kind': 'WORKLOAD', 'name': 'My
            Database Server', 'provisioner': 'Endpoints Provisioner', 'reloadInfo': {'method': 'SIGNAL', 'pidFile':
            '/var/run/db.pid', 'signal': 1}}

    Attributes:
        authority_id (str): UUID identifying the authority that will issue certificates for the endpoint.
        certificate_info (ManagedEndpointCertificateInfo): Details on a managed certificate. Example: {'crtFile':
            '/etc/db.crt', 'duration': '24h0m0s', 'gid': 999, 'keyFile': '/etc/db.key', 'mode': 256, 'rootFile':
            '/etc/ca.crt', 'type': 'X509', 'uid': 1001}.
        kind (EndpointConfigurationKind): The kind of endpoint this configuration applies to.
        name (str): The name of the endpoint configuration.
        provisioner (str): Name of the provisioner on the authority that will authorize certificates for the endpoint.
        hooks (Union[Unset, ManagedEndpointHooks]): The collection of commands to run when a certificate for a managed
            endpoint is signed or renewed.
        id (Union[Unset, str]): A UUID identifying this endpoint configuration. Read only.
        key_info (Union[Unset, ManagedEndpointKeyInfo]): The attributes of the cryptographic key. Example: {'format':
            'DER', 'pubFile': '/etc/db.csr', 'type': 'ECDSA_P256'}.
        reload_info (Union[Unset, ManagedEndpointReloadInfo]): The properties used to reload a service. Example:
            {'method': 'SIGNAL', 'pidFile': '/var/run/db.pid', 'signal': 1}.
    """

    authority_id: str
    certificate_info: "ManagedEndpointCertificateInfo"
    kind: EndpointConfigurationKind
    name: str
    provisioner: str
    hooks: Union[Unset, "ManagedEndpointHooks"] = UNSET
    id: Union[Unset, str] = UNSET
    key_info: Union[Unset, "ManagedEndpointKeyInfo"] = UNSET
    reload_info: Union[Unset, "ManagedEndpointReloadInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        authority_id = self.authority_id
        certificate_info = self.certificate_info.to_dict()

        kind = self.kind.value

        name = self.name
        provisioner = self.provisioner
        hooks: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hooks, Unset):
            hooks = self.hooks.to_dict()

        id = self.id
        key_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.key_info, Unset):
            key_info = self.key_info.to_dict()

        reload_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reload_info, Unset):
            reload_info = self.reload_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authorityID": authority_id,
                "certificateInfo": certificate_info,
                "kind": kind,
                "name": name,
                "provisioner": provisioner,
            }
        )
        if hooks is not UNSET:
            field_dict["hooks"] = hooks
        if id is not UNSET:
            field_dict["id"] = id
        if key_info is not UNSET:
            field_dict["keyInfo"] = key_info
        if reload_info is not UNSET:
            field_dict["reloadInfo"] = reload_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.managed_endpoint_certificate_info import ManagedEndpointCertificateInfo
        from ..models.managed_endpoint_hooks import ManagedEndpointHooks
        from ..models.managed_endpoint_key_info import ManagedEndpointKeyInfo
        from ..models.managed_endpoint_reload_info import ManagedEndpointReloadInfo

        d = src_dict.copy()
        authority_id = d.pop("authorityID")

        certificate_info = ManagedEndpointCertificateInfo.from_dict(d.pop("certificateInfo"))

        kind = EndpointConfigurationKind(d.pop("kind"))

        name = d.pop("name")

        provisioner = d.pop("provisioner")

        _hooks = d.pop("hooks", UNSET)
        hooks: Union[Unset, ManagedEndpointHooks]
        if isinstance(_hooks, Unset):
            hooks = UNSET
        else:
            hooks = ManagedEndpointHooks.from_dict(_hooks)

        id = d.pop("id", UNSET)

        _key_info = d.pop("keyInfo", UNSET)
        key_info: Union[Unset, ManagedEndpointKeyInfo]
        if isinstance(_key_info, Unset):
            key_info = UNSET
        else:
            key_info = ManagedEndpointKeyInfo.from_dict(_key_info)

        _reload_info = d.pop("reloadInfo", UNSET)
        reload_info: Union[Unset, ManagedEndpointReloadInfo]
        if isinstance(_reload_info, Unset):
            reload_info = UNSET
        else:
            reload_info = ManagedEndpointReloadInfo.from_dict(_reload_info)

        endpoint_configuration = cls(
            authority_id=authority_id,
            certificate_info=certificate_info,
            kind=kind,
            name=name,
            provisioner=provisioner,
            hooks=hooks,
            id=id,
            key_info=key_info,
            reload_info=reload_info,
        )

        endpoint_configuration.additional_properties = d
        return endpoint_configuration

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
