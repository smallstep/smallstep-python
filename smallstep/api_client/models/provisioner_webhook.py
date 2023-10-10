from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.provisioner_webhook_cert_type import ProvisionerWebhookCertType
from ..models.provisioner_webhook_kind import ProvisionerWebhookKind
from ..models.provisioner_webhook_server_type import ProvisionerWebhookServerType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.basic_auth import BasicAuth


T = TypeVar("T", bound="ProvisionerWebhook")


@_attrs_define
class ProvisionerWebhook:
    """A [webhook](https://smallstep.com/docs/step-ca/webhooks/) to call when a certificate request is being processed.

    Attributes:
        cert_type (ProvisionerWebhookCertType):
        kind (ProvisionerWebhookKind): The webhook kind indicates how and when it is called.

            ENRICHING webhooks are called before rendering the certificate template. They have two functions. First, they
            must allow the certificate request or it will be aborted. Second, they can return additional data to be
            referenced in the certificate template. The payload sent to the webhook server varies based on whether an X509
            or SSH certificate is to be signed and based on the type of provisioner.
        name (str): The name of the webhook. For `ENRICHING` webhooks, the returned data can be referenced in the
            certificate under the path `.Webhooks.<name>`. Must be unique to the provisioner.
        server_type (ProvisionerWebhookServerType): An EXTERNAL webhook server is not operated by Smallstep. The caller
            must use the returned ID and secret to configure the server.

            A HOSTED_ATTESTATION webhook server is hosted by Smallstep and must be used with an `ENRICHING` webhook type and
            an ACME Attestation provisioner. The webhook server will verify the attested permanent identifier exists as the
            ID of an instance in the configured collection. The data of the instance in the collection will be added to the
            template data.
        basic_auth (Union[Unset, BasicAuth]): Configures provisioner webhook requests to include an Authorization header
            with these credentials. Optional for `EXTERNAL` webhook servers; not allowed with hosted webhook servers. At
            most one of `bearerToken` and `basicAuth` may be set. Example: {'password': 'secret', 'username': 'user'}.
        bearer_token (Union[Unset, str]): Webhook requests will include an Authorization header with the token. Optional
            for `EXTERNAL` webhook servers; not allowed with hosted webhook servers. At most one of `bearerToken` and
            `basicAuth` may be set.
        collection_slug (Union[Unset, str]): For HOSTED_ATTESTATION webhooks, the collectionSlug is a reference to the
            collection that holds the devices that may be issued certificates. This collection must already exist. Required
            for `HOSTED_ATTESTATION` webhook servers; not allowed for `EXTERNAL`.
        disable_tls_client_auth (Union[Unset, bool]): The CA will not send a client certificate when requested by the
            webhook server. Optional for `EXTERNAL` webhook servers; not allowed with hosted webhook servers.
        id (Union[Unset, str]): UUID identifying this webhook. Generated server-side when the webhook is created. Will
            be sent to the webhook server in every request in the `X-Smallstep-Webhook-ID` header.
        secret (Union[Unset, str]): The shared secret used to authenticate the payload sent to the webhook server.
            Generated server-side. This is returned only for `EXTERNAL` webhook servers and only once, at the time of
            creation.
        url (Union[Unset, str]): The URL of the webhook server. Required for `EXTERNAL` webhook servers; read-only for
            hosted webhook servers.
    """

    cert_type: ProvisionerWebhookCertType
    kind: ProvisionerWebhookKind
    name: str
    server_type: ProvisionerWebhookServerType
    basic_auth: Union[Unset, "BasicAuth"] = UNSET
    bearer_token: Union[Unset, str] = UNSET
    collection_slug: Union[Unset, str] = UNSET
    disable_tls_client_auth: Union[Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    secret: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cert_type = self.cert_type.value

        kind = self.kind.value

        name = self.name
        server_type = self.server_type.value

        basic_auth: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.basic_auth, Unset):
            basic_auth = self.basic_auth.to_dict()

        bearer_token = self.bearer_token
        collection_slug = self.collection_slug
        disable_tls_client_auth = self.disable_tls_client_auth
        id = self.id
        secret = self.secret
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "certType": cert_type,
                "kind": kind,
                "name": name,
                "serverType": server_type,
            }
        )
        if basic_auth is not UNSET:
            field_dict["basicAuth"] = basic_auth
        if bearer_token is not UNSET:
            field_dict["bearerToken"] = bearer_token
        if collection_slug is not UNSET:
            field_dict["collectionSlug"] = collection_slug
        if disable_tls_client_auth is not UNSET:
            field_dict["disableTLSClientAuth"] = disable_tls_client_auth
        if id is not UNSET:
            field_dict["id"] = id
        if secret is not UNSET:
            field_dict["secret"] = secret
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.basic_auth import BasicAuth

        d = src_dict.copy()
        cert_type = ProvisionerWebhookCertType(d.pop("certType"))

        kind = ProvisionerWebhookKind(d.pop("kind"))

        name = d.pop("name")

        server_type = ProvisionerWebhookServerType(d.pop("serverType"))

        _basic_auth = d.pop("basicAuth", UNSET)
        basic_auth: Union[Unset, BasicAuth]
        if isinstance(_basic_auth, Unset):
            basic_auth = UNSET
        else:
            basic_auth = BasicAuth.from_dict(_basic_auth)

        bearer_token = d.pop("bearerToken", UNSET)

        collection_slug = d.pop("collectionSlug", UNSET)

        disable_tls_client_auth = d.pop("disableTLSClientAuth", UNSET)

        id = d.pop("id", UNSET)

        secret = d.pop("secret", UNSET)

        url = d.pop("url", UNSET)

        provisioner_webhook = cls(
            cert_type=cert_type,
            kind=kind,
            name=name,
            server_type=server_type,
            basic_auth=basic_auth,
            bearer_token=bearer_token,
            collection_slug=collection_slug,
            disable_tls_client_auth=disable_tls_client_auth,
            id=id,
            secret=secret,
            url=url,
        )

        provisioner_webhook.additional_properties = d
        return provisioner_webhook

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
