from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OIDCProvisioner")


@_attrs_define
class OIDCProvisioner:
    """A [provisioner](https://smallstep.com/docs/step-ca/provisioners/#oauthoidc-single-sign-on) that is configured to
    trust and accept an OAuth provider's ID tokens for authentication. By default, the issued certificate will use the
    subject (sub) claim from the identity token as its subject. The value of the token's email claim is also included as
    an email SAN in the certificate.

        Attributes:
            client_id (str): The id used to validate the audience in an OpenID Connect token.
            client_secret (str): The secret used to obtain the OpenID Connect tokens.
            configuration_endpoint (str): OpenID Connect configuration URL.
            admins (Union[Unset, List[str]]): The emails of admin users in an OpenID Connect provisioner. These users will
                not have restrictions in the certificates to sign.
            domains (Union[Unset, List[str]]): The domains used to validate the email claim in an OpenID Connect
                provisioner.
            groups (Union[Unset, List[str]]): The group list used to validate the groups extension in an OpenID Connect
                token.
            listen_address (Union[Unset, str]): The callback address used in the OpenID Connect flow.
            tenant_id (Union[Unset, str]): The tenant-id used to replace the templatized tenantid value in the OpenID
                Configuration.
    """

    client_id: str
    client_secret: str
    configuration_endpoint: str
    admins: Union[Unset, List[str]] = UNSET
    domains: Union[Unset, List[str]] = UNSET
    groups: Union[Unset, List[str]] = UNSET
    listen_address: Union[Unset, str] = UNSET
    tenant_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        client_id = self.client_id
        client_secret = self.client_secret
        configuration_endpoint = self.configuration_endpoint
        admins: Union[Unset, List[str]] = UNSET
        if not isinstance(self.admins, Unset):
            admins = self.admins

        domains: Union[Unset, List[str]] = UNSET
        if not isinstance(self.domains, Unset):
            domains = self.domains

        groups: Union[Unset, List[str]] = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups

        listen_address = self.listen_address
        tenant_id = self.tenant_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "clientID": client_id,
                "clientSecret": client_secret,
                "configurationEndpoint": configuration_endpoint,
            }
        )
        if admins is not UNSET:
            field_dict["admins"] = admins
        if domains is not UNSET:
            field_dict["domains"] = domains
        if groups is not UNSET:
            field_dict["groups"] = groups
        if listen_address is not UNSET:
            field_dict["listenAddress"] = listen_address
        if tenant_id is not UNSET:
            field_dict["tenantID"] = tenant_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        client_id = d.pop("clientID")

        client_secret = d.pop("clientSecret")

        configuration_endpoint = d.pop("configurationEndpoint")

        admins = cast(List[str], d.pop("admins", UNSET))

        domains = cast(List[str], d.pop("domains", UNSET))

        groups = cast(List[str], d.pop("groups", UNSET))

        listen_address = d.pop("listenAddress", UNSET)

        tenant_id = d.pop("tenantID", UNSET)

        oidc_provisioner = cls(
            client_id=client_id,
            client_secret=client_secret,
            configuration_endpoint=configuration_endpoint,
            admins=admins,
            domains=domains,
            groups=groups,
            listen_address=listen_address,
            tenant_id=tenant_id,
        )

        oidc_provisioner.additional_properties = d
        return oidc_provisioner

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
