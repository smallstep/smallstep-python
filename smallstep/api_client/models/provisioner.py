import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.provisioner_type import ProvisionerType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provisioner_claims import ProvisionerClaims
    from ..models.provisioner_options import ProvisionerOptions


T = TypeVar("T", bound="Provisioner")


@_attrs_define
class Provisioner:
    """[Provisioners](https://smallstep.com/docs/step-ca/provisioners/) are methods of using the CA to get certificates
    with different modes of authorization.

        Attributes:
            name (str): The name of the provisioner.
            type (ProvisionerType): The type of provisioner.
            claims (Union[Unset, ProvisionerClaims]): A set of constraints configuring how this provisioner can be used to
                issue certificates. Example: {'allowRenewalAfterExpiry': True, 'defaultHostSSHCertDuration': '168h',
                'defaultTLSCertDuration': '24h', 'defaultUserSSHCertDuration': '12h', 'disableRenewal': False, 'enableSSHCA':
                True, 'maxHostSSHCertDuration': '168h', 'maxTLSCertDuration': '168h', 'maxUserSSHCertDuration': '24h',
                'minHostSSHCertDuration': '48h', 'minTLSCertDuration': '1h', 'minUserSSHCertDuration': '4h'}.
            created_at (Union[Unset, datetime.datetime]): Timestamp of when the provisioner was created in RFC 3339 format.
                Generated server-side.
            id (Union[Unset, str]): A UUID identifying this provisioner. Generated server-side when the provisioner is
                created.
            options (Union[Unset, ProvisionerOptions]): Options that apply when issuing certificates with this provisioner.
    """

    name: str
    type: ProvisionerType
    claims: Union[Unset, "ProvisionerClaims"] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    options: Union[Unset, "ProvisionerOptions"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        type = self.type.value

        claims: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.claims, Unset):
            claims = self.claims.to_dict()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        id = self.id
        options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type,
            }
        )
        if claims is not UNSET:
            field_dict["claims"] = claims
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.provisioner_claims import ProvisionerClaims
        from ..models.provisioner_options import ProvisionerOptions

        d = src_dict.copy()
        name = d.pop("name")

        type = ProvisionerType(d.pop("type"))

        _claims = d.pop("claims", UNSET)
        claims: Union[Unset, ProvisionerClaims]
        if isinstance(_claims, Unset):
            claims = UNSET
        else:
            claims = ProvisionerClaims.from_dict(_claims)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        id = d.pop("id", UNSET)

        _options = d.pop("options", UNSET)
        options: Union[Unset, ProvisionerOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = ProvisionerOptions.from_dict(_options)

        provisioner = cls(
            name=name,
            type=type,
            claims=claims,
            created_at=created_at,
            id=id,
            options=options,
        )

        provisioner.additional_properties = d
        return provisioner

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
