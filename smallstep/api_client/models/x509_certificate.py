from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.x509_certificate_revocation_reason import X509CertificateRevocationReason
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.basic_constraints import BasicConstraints
    from ..models.name_constraints import NameConstraints
    from ..models.subject import Subject


T = TypeVar("T", bound="X509Certificate")


@_attrs_define
class X509Certificate:
    """
    Attributes:
        authority_key_id (str):
        basic_constraints (BasicConstraints):
        issuer (Subject): Name used in x509 certificates
        key_usage (List[str]):
        pem (str):
        serial_number (str):
        signature_algorithm (str):
        subject (Subject): Name used in x509 certificates
        subject_key_id (str):
        version (int):
        crl_distribution_points (Union[Unset, List[str]]):
        dns_names (Union[Unset, List[str]]):
        email_addresses (Union[Unset, List[str]]):
        ext_key_usage (Union[Unset, List[str]]):
        ip_addresses (Union[Unset, List[str]]):
        issuing_certificate_url (Union[Unset, List[str]]):
        name_constraints (Union[Unset, NameConstraints]): X509 certificate name constraints.
        ocsp_server (Union[Unset, List[str]]):
        policy_identifiers (Union[Unset, List[str]]):
        revocation_reason (Union[Unset, X509CertificateRevocationReason]):
        revoked (Union[Unset, bool]):
        uris (Union[Unset, List[str]]):
    """

    authority_key_id: str
    basic_constraints: "BasicConstraints"
    issuer: "Subject"
    key_usage: List[str]
    pem: str
    serial_number: str
    signature_algorithm: str
    subject: "Subject"
    subject_key_id: str
    version: int
    crl_distribution_points: Union[Unset, List[str]] = UNSET
    dns_names: Union[Unset, List[str]] = UNSET
    email_addresses: Union[Unset, List[str]] = UNSET
    ext_key_usage: Union[Unset, List[str]] = UNSET
    ip_addresses: Union[Unset, List[str]] = UNSET
    issuing_certificate_url: Union[Unset, List[str]] = UNSET
    name_constraints: Union[Unset, "NameConstraints"] = UNSET
    ocsp_server: Union[Unset, List[str]] = UNSET
    policy_identifiers: Union[Unset, List[str]] = UNSET
    revocation_reason: Union[Unset, X509CertificateRevocationReason] = UNSET
    revoked: Union[Unset, bool] = UNSET
    uris: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        authority_key_id = self.authority_key_id

        basic_constraints = self.basic_constraints.to_dict()

        issuer = self.issuer.to_dict()

        key_usage = self.key_usage

        pem = self.pem

        serial_number = self.serial_number

        signature_algorithm = self.signature_algorithm

        subject = self.subject.to_dict()

        subject_key_id = self.subject_key_id

        version = self.version

        crl_distribution_points: Union[Unset, List[str]] = UNSET
        if not isinstance(self.crl_distribution_points, Unset):
            crl_distribution_points = self.crl_distribution_points

        dns_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.dns_names, Unset):
            dns_names = self.dns_names

        email_addresses: Union[Unset, List[str]] = UNSET
        if not isinstance(self.email_addresses, Unset):
            email_addresses = self.email_addresses

        ext_key_usage: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ext_key_usage, Unset):
            ext_key_usage = self.ext_key_usage

        ip_addresses: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ip_addresses, Unset):
            ip_addresses = self.ip_addresses

        issuing_certificate_url: Union[Unset, List[str]] = UNSET
        if not isinstance(self.issuing_certificate_url, Unset):
            issuing_certificate_url = self.issuing_certificate_url

        name_constraints: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.name_constraints, Unset):
            name_constraints = self.name_constraints.to_dict()

        ocsp_server: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ocsp_server, Unset):
            ocsp_server = self.ocsp_server

        policy_identifiers: Union[Unset, List[str]] = UNSET
        if not isinstance(self.policy_identifiers, Unset):
            policy_identifiers = self.policy_identifiers

        revocation_reason: Union[Unset, str] = UNSET
        if not isinstance(self.revocation_reason, Unset):
            revocation_reason = self.revocation_reason.value

        revoked = self.revoked

        uris: Union[Unset, List[str]] = UNSET
        if not isinstance(self.uris, Unset):
            uris = self.uris

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authorityKeyId": authority_key_id,
                "basicConstraints": basic_constraints,
                "issuer": issuer,
                "keyUsage": key_usage,
                "pem": pem,
                "serialNumber": serial_number,
                "signatureAlgorithm": signature_algorithm,
                "subject": subject,
                "subjectKeyId": subject_key_id,
                "version": version,
            }
        )
        if crl_distribution_points is not UNSET:
            field_dict["crlDistributionPoints"] = crl_distribution_points
        if dns_names is not UNSET:
            field_dict["dnsNames"] = dns_names
        if email_addresses is not UNSET:
            field_dict["emailAddresses"] = email_addresses
        if ext_key_usage is not UNSET:
            field_dict["extKeyUsage"] = ext_key_usage
        if ip_addresses is not UNSET:
            field_dict["ipAddresses"] = ip_addresses
        if issuing_certificate_url is not UNSET:
            field_dict["issuingCertificateURL"] = issuing_certificate_url
        if name_constraints is not UNSET:
            field_dict["nameConstraints"] = name_constraints
        if ocsp_server is not UNSET:
            field_dict["ocspServer"] = ocsp_server
        if policy_identifiers is not UNSET:
            field_dict["policyIdentifiers"] = policy_identifiers
        if revocation_reason is not UNSET:
            field_dict["revocationReason"] = revocation_reason
        if revoked is not UNSET:
            field_dict["revoked"] = revoked
        if uris is not UNSET:
            field_dict["uris"] = uris

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.basic_constraints import BasicConstraints
        from ..models.name_constraints import NameConstraints
        from ..models.subject import Subject

        d = src_dict.copy()
        authority_key_id = d.pop("authorityKeyId")

        basic_constraints = BasicConstraints.from_dict(d.pop("basicConstraints"))

        issuer = Subject.from_dict(d.pop("issuer"))

        key_usage = cast(List[str], d.pop("keyUsage"))

        pem = d.pop("pem")

        serial_number = d.pop("serialNumber")

        signature_algorithm = d.pop("signatureAlgorithm")

        subject = Subject.from_dict(d.pop("subject"))

        subject_key_id = d.pop("subjectKeyId")

        version = d.pop("version")

        crl_distribution_points = cast(List[str], d.pop("crlDistributionPoints", UNSET))

        dns_names = cast(List[str], d.pop("dnsNames", UNSET))

        email_addresses = cast(List[str], d.pop("emailAddresses", UNSET))

        ext_key_usage = cast(List[str], d.pop("extKeyUsage", UNSET))

        ip_addresses = cast(List[str], d.pop("ipAddresses", UNSET))

        issuing_certificate_url = cast(List[str], d.pop("issuingCertificateURL", UNSET))

        _name_constraints = d.pop("nameConstraints", UNSET)
        name_constraints: Union[Unset, NameConstraints]
        if isinstance(_name_constraints, Unset):
            name_constraints = UNSET
        else:
            name_constraints = NameConstraints.from_dict(_name_constraints)

        ocsp_server = cast(List[str], d.pop("ocspServer", UNSET))

        policy_identifiers = cast(List[str], d.pop("policyIdentifiers", UNSET))

        _revocation_reason = d.pop("revocationReason", UNSET)
        revocation_reason: Union[Unset, X509CertificateRevocationReason]
        if isinstance(_revocation_reason, Unset):
            revocation_reason = UNSET
        else:
            revocation_reason = X509CertificateRevocationReason(_revocation_reason)

        revoked = d.pop("revoked", UNSET)

        uris = cast(List[str], d.pop("uris", UNSET))

        x509_certificate = cls(
            authority_key_id=authority_key_id,
            basic_constraints=basic_constraints,
            issuer=issuer,
            key_usage=key_usage,
            pem=pem,
            serial_number=serial_number,
            signature_algorithm=signature_algorithm,
            subject=subject,
            subject_key_id=subject_key_id,
            version=version,
            crl_distribution_points=crl_distribution_points,
            dns_names=dns_names,
            email_addresses=email_addresses,
            ext_key_usage=ext_key_usage,
            ip_addresses=ip_addresses,
            issuing_certificate_url=issuing_certificate_url,
            name_constraints=name_constraints,
            ocsp_server=ocsp_server,
            policy_identifiers=policy_identifiers,
            revocation_reason=revocation_reason,
            revoked=revoked,
            uris=uris,
        )

        x509_certificate.additional_properties = d
        return x509_certificate

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
