from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.extra_name import ExtraName


T = TypeVar("T", bound="Subject")


@_attrs_define
class Subject:
    """Name used in x509 certificates

    Attributes:
        common_name (Union[Unset, str]):
        country (Union[Unset, List[str]]):
        email_address (Union[Unset, List[str]]):
        extra_names (Union[Unset, List['ExtraName']]):
        locality (Union[Unset, List[str]]):
        organization (Union[Unset, List[str]]):
        organizational_unit (Union[Unset, List[str]]):
        postal_code (Union[Unset, List[str]]):
        province (Union[Unset, List[str]]):
        serial_number (Union[Unset, str]):
        street_address (Union[Unset, List[str]]):
    """

    common_name: Union[Unset, str] = UNSET
    country: Union[Unset, List[str]] = UNSET
    email_address: Union[Unset, List[str]] = UNSET
    extra_names: Union[Unset, List["ExtraName"]] = UNSET
    locality: Union[Unset, List[str]] = UNSET
    organization: Union[Unset, List[str]] = UNSET
    organizational_unit: Union[Unset, List[str]] = UNSET
    postal_code: Union[Unset, List[str]] = UNSET
    province: Union[Unset, List[str]] = UNSET
    serial_number: Union[Unset, str] = UNSET
    street_address: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        common_name = self.common_name

        country: Union[Unset, List[str]] = UNSET
        if not isinstance(self.country, Unset):
            country = self.country

        email_address: Union[Unset, List[str]] = UNSET
        if not isinstance(self.email_address, Unset):
            email_address = self.email_address

        extra_names: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.extra_names, Unset):
            extra_names = []
            for extra_names_item_data in self.extra_names:
                extra_names_item = extra_names_item_data.to_dict()
                extra_names.append(extra_names_item)

        locality: Union[Unset, List[str]] = UNSET
        if not isinstance(self.locality, Unset):
            locality = self.locality

        organization: Union[Unset, List[str]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization

        organizational_unit: Union[Unset, List[str]] = UNSET
        if not isinstance(self.organizational_unit, Unset):
            organizational_unit = self.organizational_unit

        postal_code: Union[Unset, List[str]] = UNSET
        if not isinstance(self.postal_code, Unset):
            postal_code = self.postal_code

        province: Union[Unset, List[str]] = UNSET
        if not isinstance(self.province, Unset):
            province = self.province

        serial_number = self.serial_number

        street_address: Union[Unset, List[str]] = UNSET
        if not isinstance(self.street_address, Unset):
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
        if extra_names is not UNSET:
            field_dict["extraNames"] = extra_names
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
        from ..models.extra_name import ExtraName

        d = src_dict.copy()
        common_name = d.pop("commonName", UNSET)

        country = cast(List[str], d.pop("country", UNSET))

        email_address = cast(List[str], d.pop("emailAddress", UNSET))

        extra_names = []
        _extra_names = d.pop("extraNames", UNSET)
        for extra_names_item_data in _extra_names or []:
            extra_names_item = ExtraName.from_dict(extra_names_item_data)

            extra_names.append(extra_names_item)

        locality = cast(List[str], d.pop("locality", UNSET))

        organization = cast(List[str], d.pop("organization", UNSET))

        organizational_unit = cast(List[str], d.pop("organizationalUnit", UNSET))

        postal_code = cast(List[str], d.pop("postalCode", UNSET))

        province = cast(List[str], d.pop("province", UNSET))

        serial_number = d.pop("serialNumber", UNSET)

        street_address = cast(List[str], d.pop("streetAddress", UNSET))

        subject = cls(
            common_name=common_name,
            country=country,
            email_address=email_address,
            extra_names=extra_names,
            locality=locality,
            organization=organization,
            organizational_unit=organizational_unit,
            postal_code=postal_code,
            province=province,
            serial_number=serial_number,
            street_address=street_address,
        )

        subject.additional_properties = d
        return subject

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
