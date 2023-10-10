from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.managed_endpoint_certificate_info import ManagedEndpointCertificateInfo
    from ..models.managed_endpoint_hooks import ManagedEndpointHooks
    from ..models.managed_endpoint_key_info import ManagedEndpointKeyInfo
    from ..models.managed_endpoint_reload_info import ManagedEndpointReloadInfo


T = TypeVar("T", bound="Workload")


@_attrs_define
class Workload:
    """A workload represents anything that uses a certificate.

    Attributes:
        display_name (str): A friendly name for the workload. Also used as the Common Name if no static SANs are
            provide.
        slug (str): Used as the identifier for the workload.
        workload_type (str):
        admin_emails (Union[Unset, List[str]]): Users that will have admin access to manage the workloads authority,
            which will be created if it does not already exist. Ignored if the workloads authority already exists. Never
            returned in responses.
        certificate_info (Union[Unset, ManagedEndpointCertificateInfo]): Details on a managed certificate. Example:
            {'crtFile': '/etc/db.crt', 'duration': '24h0m0s', 'gid': 999, 'keyFile': '/etc/db.key', 'mode': 256, 'rootFile':
            '/etc/ca.crt', 'type': 'X509', 'uid': 1001}.
        device_metadata_key_sans (Union[Unset, List[str]]): SANs that will be populated from the instance data of the
            device in the device collection.
            For example, if the device instance data in the collection is `{"internal_host": "foo.internal",
            "external_host", "foo.example.com"}` at the time the workload certificate is issued and this field is set to
            `["internal_host", "external_host"]`, then the certificate would include the SANs `foo.internal` and
            `foo.example.com`.
        hooks (Union[Unset, ManagedEndpointHooks]): The collection of commands to run when a certificate for a managed
            endpoint is signed or renewed.
        key_info (Union[Unset, ManagedEndpointKeyInfo]): The attributes of the cryptographic key. Example: {'format':
            'DER', 'pubFile': '/etc/db.csr', 'type': 'ECDSA_P256'}.
        reload_info (Union[Unset, ManagedEndpointReloadInfo]): The properties used to reload a service. Example:
            {'method': 'SIGNAL', 'pidFile': '/var/run/db.pid', 'signal': 1}.
        static_sans (Union[Unset, List[str]]): SANs that will be added to every certificate issued for this workload.
            The first will be used as the default Common Name.
    """

    display_name: str
    slug: str
    workload_type: str
    admin_emails: Union[Unset, List[str]] = UNSET
    certificate_info: Union[Unset, "ManagedEndpointCertificateInfo"] = UNSET
    device_metadata_key_sans: Union[Unset, List[str]] = UNSET
    hooks: Union[Unset, "ManagedEndpointHooks"] = UNSET
    key_info: Union[Unset, "ManagedEndpointKeyInfo"] = UNSET
    reload_info: Union[Unset, "ManagedEndpointReloadInfo"] = UNSET
    static_sans: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name
        slug = self.slug
        workload_type = self.workload_type
        admin_emails: Union[Unset, List[str]] = UNSET
        if not isinstance(self.admin_emails, Unset):
            admin_emails = self.admin_emails

        certificate_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.certificate_info, Unset):
            certificate_info = self.certificate_info.to_dict()

        device_metadata_key_sans: Union[Unset, List[str]] = UNSET
        if not isinstance(self.device_metadata_key_sans, Unset):
            device_metadata_key_sans = self.device_metadata_key_sans

        hooks: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hooks, Unset):
            hooks = self.hooks.to_dict()

        key_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.key_info, Unset):
            key_info = self.key_info.to_dict()

        reload_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reload_info, Unset):
            reload_info = self.reload_info.to_dict()

        static_sans: Union[Unset, List[str]] = UNSET
        if not isinstance(self.static_sans, Unset):
            static_sans = self.static_sans

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "displayName": display_name,
                "slug": slug,
                "workloadType": workload_type,
            }
        )
        if admin_emails is not UNSET:
            field_dict["adminEmails"] = admin_emails
        if certificate_info is not UNSET:
            field_dict["certificateInfo"] = certificate_info
        if device_metadata_key_sans is not UNSET:
            field_dict["deviceMetadataKeySANs"] = device_metadata_key_sans
        if hooks is not UNSET:
            field_dict["hooks"] = hooks
        if key_info is not UNSET:
            field_dict["keyInfo"] = key_info
        if reload_info is not UNSET:
            field_dict["reloadInfo"] = reload_info
        if static_sans is not UNSET:
            field_dict["staticSANs"] = static_sans

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.managed_endpoint_certificate_info import ManagedEndpointCertificateInfo
        from ..models.managed_endpoint_hooks import ManagedEndpointHooks
        from ..models.managed_endpoint_key_info import ManagedEndpointKeyInfo
        from ..models.managed_endpoint_reload_info import ManagedEndpointReloadInfo

        d = src_dict.copy()
        display_name = d.pop("displayName")

        slug = d.pop("slug")

        workload_type = d.pop("workloadType")

        admin_emails = cast(List[str], d.pop("adminEmails", UNSET))

        _certificate_info = d.pop("certificateInfo", UNSET)
        certificate_info: Union[Unset, ManagedEndpointCertificateInfo]
        if isinstance(_certificate_info, Unset):
            certificate_info = UNSET
        else:
            certificate_info = ManagedEndpointCertificateInfo.from_dict(_certificate_info)

        device_metadata_key_sans = cast(List[str], d.pop("deviceMetadataKeySANs", UNSET))

        _hooks = d.pop("hooks", UNSET)
        hooks: Union[Unset, ManagedEndpointHooks]
        if isinstance(_hooks, Unset):
            hooks = UNSET
        else:
            hooks = ManagedEndpointHooks.from_dict(_hooks)

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

        static_sans = cast(List[str], d.pop("staticSANs", UNSET))

        workload = cls(
            display_name=display_name,
            slug=slug,
            workload_type=workload_type,
            admin_emails=admin_emails,
            certificate_info=certificate_info,
            device_metadata_key_sans=device_metadata_key_sans,
            hooks=hooks,
            key_info=key_info,
            reload_info=reload_info,
            static_sans=static_sans,
        )

        workload.additional_properties = d
        return workload

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
