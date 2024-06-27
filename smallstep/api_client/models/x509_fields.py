from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.certificate_field_device_metadata import CertificateFieldDeviceMetadata
    from ..models.certificate_field_list import CertificateFieldList
    from ..models.certificate_field_static import CertificateFieldStatic


T = TypeVar("T", bound="X509Fields")


@_attrs_define
class X509Fields:
    """
    Attributes:
        common_name (Union['CertificateFieldDeviceMetadata', 'CertificateFieldStatic', Unset]): A certificate field that
            takes a single string value, e.g. Common Name.
        country (Union[Unset, CertificateFieldList]): A certificate field that accepts multiple string values, e.g.
            SANs.
        locality (Union[Unset, CertificateFieldList]): A certificate field that accepts multiple string values, e.g.
            SANs.
        organization (Union[Unset, CertificateFieldList]): A certificate field that accepts multiple string values, e.g.
            SANs.
        organizational_unit (Union[Unset, CertificateFieldList]): A certificate field that accepts multiple string
            values, e.g. SANs.
        postal_code (Union[Unset, CertificateFieldList]): A certificate field that accepts multiple string values, e.g.
            SANs.
        province (Union[Unset, CertificateFieldList]): A certificate field that accepts multiple string values, e.g.
            SANs.
        sans (Union[Unset, CertificateFieldList]): A certificate field that accepts multiple string values, e.g. SANs.
        street_address (Union[Unset, CertificateFieldList]): A certificate field that accepts multiple string values,
            e.g. SANs.
    """

    common_name: Union["CertificateFieldDeviceMetadata", "CertificateFieldStatic", Unset] = UNSET
    country: Union[Unset, "CertificateFieldList"] = UNSET
    locality: Union[Unset, "CertificateFieldList"] = UNSET
    organization: Union[Unset, "CertificateFieldList"] = UNSET
    organizational_unit: Union[Unset, "CertificateFieldList"] = UNSET
    postal_code: Union[Unset, "CertificateFieldList"] = UNSET
    province: Union[Unset, "CertificateFieldList"] = UNSET
    sans: Union[Unset, "CertificateFieldList"] = UNSET
    street_address: Union[Unset, "CertificateFieldList"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.certificate_field_static import CertificateFieldStatic

        common_name: Union[Dict[str, Any], Unset]
        if isinstance(self.common_name, Unset):
            common_name = UNSET
        elif isinstance(self.common_name, CertificateFieldStatic):
            common_name = self.common_name.to_dict()
        else:
            common_name = self.common_name.to_dict()

        country: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.country, Unset):
            country = self.country.to_dict()

        locality: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.locality, Unset):
            locality = self.locality.to_dict()

        organization: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        organizational_unit: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.organizational_unit, Unset):
            organizational_unit = self.organizational_unit.to_dict()

        postal_code: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.postal_code, Unset):
            postal_code = self.postal_code.to_dict()

        province: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.province, Unset):
            province = self.province.to_dict()

        sans: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sans, Unset):
            sans = self.sans.to_dict()

        street_address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.street_address, Unset):
            street_address = self.street_address.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if common_name is not UNSET:
            field_dict["commonName"] = common_name
        if country is not UNSET:
            field_dict["country"] = country
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
        if sans is not UNSET:
            field_dict["sans"] = sans
        if street_address is not UNSET:
            field_dict["streetAddress"] = street_address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.certificate_field_device_metadata import CertificateFieldDeviceMetadata
        from ..models.certificate_field_list import CertificateFieldList
        from ..models.certificate_field_static import CertificateFieldStatic

        d = src_dict.copy()

        def _parse_common_name(
            data: object,
        ) -> Union["CertificateFieldDeviceMetadata", "CertificateFieldStatic", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemascertificate_field_type_0 = CertificateFieldStatic.from_dict(data)

                return componentsschemascertificate_field_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemascertificate_field_type_1 = CertificateFieldDeviceMetadata.from_dict(data)

            return componentsschemascertificate_field_type_1

        common_name = _parse_common_name(d.pop("commonName", UNSET))

        _country = d.pop("country", UNSET)
        country: Union[Unset, CertificateFieldList]
        if isinstance(_country, Unset):
            country = UNSET
        else:
            country = CertificateFieldList.from_dict(_country)

        _locality = d.pop("locality", UNSET)
        locality: Union[Unset, CertificateFieldList]
        if isinstance(_locality, Unset):
            locality = UNSET
        else:
            locality = CertificateFieldList.from_dict(_locality)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, CertificateFieldList]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = CertificateFieldList.from_dict(_organization)

        _organizational_unit = d.pop("organizationalUnit", UNSET)
        organizational_unit: Union[Unset, CertificateFieldList]
        if isinstance(_organizational_unit, Unset):
            organizational_unit = UNSET
        else:
            organizational_unit = CertificateFieldList.from_dict(_organizational_unit)

        _postal_code = d.pop("postalCode", UNSET)
        postal_code: Union[Unset, CertificateFieldList]
        if isinstance(_postal_code, Unset):
            postal_code = UNSET
        else:
            postal_code = CertificateFieldList.from_dict(_postal_code)

        _province = d.pop("province", UNSET)
        province: Union[Unset, CertificateFieldList]
        if isinstance(_province, Unset):
            province = UNSET
        else:
            province = CertificateFieldList.from_dict(_province)

        _sans = d.pop("sans", UNSET)
        sans: Union[Unset, CertificateFieldList]
        if isinstance(_sans, Unset):
            sans = UNSET
        else:
            sans = CertificateFieldList.from_dict(_sans)

        _street_address = d.pop("streetAddress", UNSET)
        street_address: Union[Unset, CertificateFieldList]
        if isinstance(_street_address, Unset):
            street_address = UNSET
        else:
            street_address = CertificateFieldList.from_dict(_street_address)

        x509_fields = cls(
            common_name=common_name,
            country=country,
            locality=locality,
            organization=organization,
            organizational_unit=organizational_unit,
            postal_code=postal_code,
            province=province,
            sans=sans,
            street_address=street_address,
        )

        x509_fields.additional_properties = d
        return x509_fields

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
