from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DistinguishedName")


@_attrs_define
class DistinguishedName:
    """Name used in x509 certificates

    Example:
        [{'organization': 'admins'}]

    Attributes:
        common_name (Union[Unset, str]):
        country (Union[Unset, str]):
        email_address (Union[Unset, str]):
        locality (Union[Unset, str]):
        organization (Union[Unset, str]):
        organizational_unit (Union[Unset, str]):
        postal_code (Union[Unset, str]):
        province (Union[Unset, str]):
        serial_number (Union[Unset, str]):
        street_address (Union[Unset, str]):
    """

    common_name: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    email_address: Union[Unset, str] = UNSET
    locality: Union[Unset, str] = UNSET
    organization: Union[Unset, str] = UNSET
    organizational_unit: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    province: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    street_address: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        common_name = self.common_name
        country = self.country
        email_address = self.email_address
        locality = self.locality
        organization = self.organization
        organizational_unit = self.organizational_unit
        postal_code = self.postal_code
        province = self.province
        serial_number = self.serial_number
        street_address = self.street_address

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if common_name is not UNSET:
            field_dict["commonName"] = common_name
        if country is not UNSET:
            field_dict["country"] = country
        if email_address is not UNSET:
            field_dict["emailAddress"] = email_address
        if locality is not UNSET:
            field_dict["locality"] = locality
        if organization is not UNSET:
            field_dict["organization"] = organization
        if organizational_unit is not UNSET:
            field_dict["organizationalUnit"] = organizational_unit
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if province is not UNSET:
            field_dict["province"] = province
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if street_address is not UNSET:
            field_dict["streetAddress"] = street_address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        common_name = d.pop("commonName", UNSET)

        country = d.pop("country", UNSET)

        email_address = d.pop("emailAddress", UNSET)

        locality = d.pop("locality", UNSET)

        organization = d.pop("organization", UNSET)

        organizational_unit = d.pop("organizationalUnit", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        province = d.pop("province", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        street_address = d.pop("streetAddress", UNSET)

        distinguished_name = cls(
            common_name=common_name,
            country=country,
            email_address=email_address,
            locality=locality,
            organization=organization,
            organizational_unit=organizational_unit,
            postal_code=postal_code,
            province=province,
            serial_number=serial_number,
            street_address=street_address,
        )

        distinguished_name.additional_properties = d
        return distinguished_name

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
