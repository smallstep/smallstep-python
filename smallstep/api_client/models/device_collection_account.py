from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.managed_endpoint_certificate_info import ManagedEndpointCertificateInfo
    from ..models.managed_endpoint_hooks import ManagedEndpointHooks
    from ..models.managed_endpoint_key_info import ManagedEndpointKeyInfo
    from ..models.managed_endpoint_reload_info import ManagedEndpointReloadInfo


T = TypeVar("T", bound="DeviceCollectionAccount")


@_attrs_define
class DeviceCollectionAccount:
    """The certificate details binding an account to a device collection.

    Attributes:
        account_id (str): Identifier of the account.
        display_name (str): A friendly name for the device collection account. Also used as the Common Name, if no
            static SANs are provided.
        slug (str): Used as the identifier for the device collection account.
        admin_emails (Union[Unset, List[str]]): Users that will have admin access to manage the workloads authority,
            which will be created if it does not already exist. Ignored if the workloads authority already exists. Never
            returned in responses.
        authority_id (Union[Unset, str]): A UUID identifying the authority. Defaults to the accounts authority if not
            set.
        certificate_info (Union[Unset, ManagedEndpointCertificateInfo]): Details on a managed certificate. Example:
            {'crtFile': '/etc/db.crt', 'duration': '24h0m0s', 'gid': 999, 'keyFile': '/etc/db.key', 'mode': 256, 'rootFile':
            '/etc/ca.crt', 'type': 'X509', 'uid': 1001}.
        hooks (Union[Unset, ManagedEndpointHooks]): The collection of commands to run when a certificate for a managed
            endpoint is signed or renewed.
        key_info (Union[Unset, ManagedEndpointKeyInfo]): The attributes of the cryptographic key. Example: {'format':
            'PKCS8', 'protection': 'NONE', 'pubFile': '/etc/db.csr', 'type': 'ECDSA_P256'}.
        reload_info (Union[Unset, ManagedEndpointReloadInfo]): The properties used to reload a service. Example:
            {'method': 'SIGNAL', 'pidFile': '/var/run/db.pid', 'signal': 1}.
    """

    account_id: str
    display_name: str
    slug: str
    admin_emails: Union[Unset, List[str]] = UNSET
    authority_id: Union[Unset, str] = UNSET
    certificate_info: Union[Unset, "ManagedEndpointCertificateInfo"] = UNSET
    hooks: Union[Unset, "ManagedEndpointHooks"] = UNSET
    key_info: Union[Unset, "ManagedEndpointKeyInfo"] = UNSET
    reload_info: Union[Unset, "ManagedEndpointReloadInfo"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id

        display_name = self.display_name

        slug = self.slug

        admin_emails: Union[Unset, List[str]] = UNSET
        if not isinstance(self.admin_emails, Unset):
            admin_emails = self.admin_emails

        authority_id = self.authority_id

        certificate_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.certificate_info, Unset):
            certificate_info = self.certificate_info.to_dict()

        hooks: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.hooks, Unset):
            hooks = self.hooks.to_dict()

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
                "accountID": account_id,
                "displayName": display_name,
                "slug": slug,
            }
        )
        if admin_emails is not UNSET:
            field_dict["adminEmails"] = admin_emails
        if authority_id is not UNSET:
            field_dict["authorityID"] = authority_id
        if certificate_info is not UNSET:
            field_dict["certificateInfo"] = certificate_info
        if hooks is not UNSET:
            field_dict["hooks"] = hooks
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
        account_id = d.pop("accountID")

        display_name = d.pop("displayName")

        slug = d.pop("slug")

        admin_emails = cast(List[str], d.pop("adminEmails", UNSET))

        authority_id = d.pop("authorityID", UNSET)

        _certificate_info = d.pop("certificateInfo", UNSET)
        certificate_info: Union[Unset, ManagedEndpointCertificateInfo]
        if isinstance(_certificate_info, Unset):
            certificate_info = UNSET
        else:
            certificate_info = ManagedEndpointCertificateInfo.from_dict(_certificate_info)

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

        device_collection_account = cls(
            account_id=account_id,
            display_name=display_name,
            slug=slug,
            admin_emails=admin_emails,
            authority_id=authority_id,
            certificate_info=certificate_info,
            hooks=hooks,
            key_info=key_info,
            reload_info=reload_info,
        )

        device_collection_account.additional_properties = d
        return device_collection_account

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
