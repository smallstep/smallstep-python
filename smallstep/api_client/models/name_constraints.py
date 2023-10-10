from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NameConstraints")


@_attrs_define
class NameConstraints:
    """X509 certificate name constratins.

    Attributes:
        critical (Union[Unset, bool]): Whether or not name constraints are marked critical.
        excluded_dns_domains (Union[Unset, List[str]]):
        excluded_email_addresses (Union[Unset, List[str]]):
        excluded_ip_ranges (Union[Unset, List[str]]):
        excluded_uri_domains (Union[Unset, List[str]]):
        permitted_dns_domains (Union[Unset, List[str]]):
        permitted_email_addresses (Union[Unset, List[str]]):
        permitted_ip_ranges (Union[Unset, List[str]]):
        permitted_uri_domains (Union[Unset, List[str]]):
    """

    critical: Union[Unset, bool] = UNSET
    excluded_dns_domains: Union[Unset, List[str]] = UNSET
    excluded_email_addresses: Union[Unset, List[str]] = UNSET
    excluded_ip_ranges: Union[Unset, List[str]] = UNSET
    excluded_uri_domains: Union[Unset, List[str]] = UNSET
    permitted_dns_domains: Union[Unset, List[str]] = UNSET
    permitted_email_addresses: Union[Unset, List[str]] = UNSET
    permitted_ip_ranges: Union[Unset, List[str]] = UNSET
    permitted_uri_domains: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        critical = self.critical
        excluded_dns_domains: Union[Unset, List[str]] = UNSET
        if not isinstance(self.excluded_dns_domains, Unset):
            excluded_dns_domains = self.excluded_dns_domains

        excluded_email_addresses: Union[Unset, List[str]] = UNSET
        if not isinstance(self.excluded_email_addresses, Unset):
            excluded_email_addresses = self.excluded_email_addresses

        excluded_ip_ranges: Union[Unset, List[str]] = UNSET
        if not isinstance(self.excluded_ip_ranges, Unset):
            excluded_ip_ranges = self.excluded_ip_ranges

        excluded_uri_domains: Union[Unset, List[str]] = UNSET
        if not isinstance(self.excluded_uri_domains, Unset):
            excluded_uri_domains = self.excluded_uri_domains

        permitted_dns_domains: Union[Unset, List[str]] = UNSET
        if not isinstance(self.permitted_dns_domains, Unset):
            permitted_dns_domains = self.permitted_dns_domains

        permitted_email_addresses: Union[Unset, List[str]] = UNSET
        if not isinstance(self.permitted_email_addresses, Unset):
            permitted_email_addresses = self.permitted_email_addresses

        permitted_ip_ranges: Union[Unset, List[str]] = UNSET
        if not isinstance(self.permitted_ip_ranges, Unset):
            permitted_ip_ranges = self.permitted_ip_ranges

        permitted_uri_domains: Union[Unset, List[str]] = UNSET
        if not isinstance(self.permitted_uri_domains, Unset):
            permitted_uri_domains = self.permitted_uri_domains

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if critical is not UNSET:
            field_dict["critical"] = critical
        if excluded_dns_domains is not UNSET:
            field_dict["excludedDNSDomains"] = excluded_dns_domains
        if excluded_email_addresses is not UNSET:
            field_dict["excludedEmailAddresses"] = excluded_email_addresses
        if excluded_ip_ranges is not UNSET:
            field_dict["excludedIPRanges"] = excluded_ip_ranges
        if excluded_uri_domains is not UNSET:
            field_dict["excludedURIDomains"] = excluded_uri_domains
        if permitted_dns_domains is not UNSET:
            field_dict["permittedDNSDomains"] = permitted_dns_domains
        if permitted_email_addresses is not UNSET:
            field_dict["permittedEmailAddresses"] = permitted_email_addresses
        if permitted_ip_ranges is not UNSET:
            field_dict["permittedIPRanges"] = permitted_ip_ranges
        if permitted_uri_domains is not UNSET:
            field_dict["permittedURIDomains"] = permitted_uri_domains

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        critical = d.pop("critical", UNSET)

        excluded_dns_domains = cast(List[str], d.pop("excludedDNSDomains", UNSET))

        excluded_email_addresses = cast(List[str], d.pop("excludedEmailAddresses", UNSET))

        excluded_ip_ranges = cast(List[str], d.pop("excludedIPRanges", UNSET))

        excluded_uri_domains = cast(List[str], d.pop("excludedURIDomains", UNSET))

        permitted_dns_domains = cast(List[str], d.pop("permittedDNSDomains", UNSET))

        permitted_email_addresses = cast(List[str], d.pop("permittedEmailAddresses", UNSET))

        permitted_ip_ranges = cast(List[str], d.pop("permittedIPRanges", UNSET))

        permitted_uri_domains = cast(List[str], d.pop("permittedURIDomains", UNSET))

        name_constraints = cls(
            critical=critical,
            excluded_dns_domains=excluded_dns_domains,
            excluded_email_addresses=excluded_email_addresses,
            excluded_ip_ranges=excluded_ip_ranges,
            excluded_uri_domains=excluded_uri_domains,
            permitted_dns_domains=permitted_dns_domains,
            permitted_email_addresses=permitted_email_addresses,
            permitted_ip_ranges=permitted_ip_ranges,
            permitted_uri_domains=permitted_uri_domains,
        )

        name_constraints.additional_properties = d
        return name_constraints

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
