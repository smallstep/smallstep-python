import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AttestationAuthority")


@_attrs_define
class AttestationAuthority:
    r"""An attestation authority used with the device-attest-01 ACME challenge to verify a device's hardware identity. This
    object is experimental and subject to change.

        Example:
            {'attestorIntermediates': '-----BEGIN CERTIFICATE-----\n ... \n-----END CERTIFICATE-----', 'attestorRoots': '
                -----BEGIN CERTIFICATE-----\n ... \n-----END CERTIFICATE-----', 'createdAt': '2022-11-10T23:00:00Z', 'id':
                '35507915-6ce4-4517-802f-1bdb6e9e80d8', 'name': 'Our Attestation Authority', 'root': '-----BEGIN
                CERTIFICATE-----\n ... \n-----END CERTIFICATE-----', 'slug': 'teamfooattestationca'}

        Attributes:
            attestor_roots (str): The pem-encoded list of certificates used to verify the attestation certificates submitted
                by devices.
            name (str): The name of the attestation authority.
            attestor_intermediates (Union[Unset, str]): The pem-encoded list of intermediate certificates used to build a
                chain of trust to verify the attestation certificates submitted by devices.
            created_at (Union[Unset, datetime.datetime]): Timestamp in RFC3339 format when the attestation authority was
                created.
            id (Union[Unset, str]): A UUID identifying this attestation authority. Read only.
            root (Union[Unset, str]): The pem-encoded root certificate of this attestation authority. This is generated
                server-side when the attestation authority is created. This certificate should be used in the `attestationRoots`
                field of an ACME_ATTESTATION provisioner with the `tpm` format.
            slug (Union[Unset, str]): A short name for this attestation authority. Read only.
    """

    attestor_roots: str
    name: str
    attestor_intermediates: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    id: Union[Unset, str] = UNSET
    root: Union[Unset, str] = UNSET
    slug: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attestor_roots = self.attestor_roots
        name = self.name
        attestor_intermediates = self.attestor_intermediates
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        id = self.id
        root = self.root
        slug = self.slug

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attestorRoots": attestor_roots,
                "name": name,
            }
        )
        if attestor_intermediates is not UNSET:
            field_dict["attestorIntermediates"] = attestor_intermediates
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if root is not UNSET:
            field_dict["root"] = root
        if slug is not UNSET:
            field_dict["slug"] = slug

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        attestor_roots = d.pop("attestorRoots")

        name = d.pop("name")

        attestor_intermediates = d.pop("attestorIntermediates", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        id = d.pop("id", UNSET)

        root = d.pop("root", UNSET)

        slug = d.pop("slug", UNSET)

        attestation_authority = cls(
            attestor_roots=attestor_roots,
            name=name,
            attestor_intermediates=attestor_intermediates,
            created_at=created_at,
            id=id,
            root=root,
            slug=slug,
        )

        attestation_authority.additional_properties = d
        return attestation_authority

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
