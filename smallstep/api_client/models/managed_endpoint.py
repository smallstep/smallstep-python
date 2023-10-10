from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ssh_certificate_data import SSHCertificateData
    from ..models.x509_certificate_data import X509CertificateData


T = TypeVar("T", bound="ManagedEndpoint")


@_attrs_define
class ManagedEndpoint:
    """All the information used by an agent to grant a certificate to an endpoint. Exactly one of `x509CertificateData` or
    `sshCertificateData` must be set and must match the endpoint configuration certificate info type. This object is
    experimental and subject to change.

        Attributes:
            endpoint_configuration_id (str): UUID identifying the endpoint configuration.
            id (Union[Unset, str]): UUID identifying this managed endpoint. Read only.
            ssh_certificate_data (Union[Unset, SSHCertificateData]): Contains the information to include when granting an
                SSH certificate to a managed endpoint. Example: {'keyID': 'abc123', 'principals': ['ops', 'eng']}.
            x_509_certificate_data (Union[Unset, X509CertificateData]): Contains the information to include when granting an
                x509 certificate to a managed endpoint. Example: {'commonName': 'db', 'sans': ['db', 'db.internal']}.
    """

    endpoint_configuration_id: str
    id: Union[Unset, str] = UNSET
    ssh_certificate_data: Union[Unset, "SSHCertificateData"] = UNSET
    x_509_certificate_data: Union[Unset, "X509CertificateData"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        endpoint_configuration_id = self.endpoint_configuration_id
        id = self.id
        ssh_certificate_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ssh_certificate_data, Unset):
            ssh_certificate_data = self.ssh_certificate_data.to_dict()

        x_509_certificate_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.x_509_certificate_data, Unset):
            x_509_certificate_data = self.x_509_certificate_data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endpointConfigurationID": endpoint_configuration_id,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if ssh_certificate_data is not UNSET:
            field_dict["sshCertificateData"] = ssh_certificate_data
        if x_509_certificate_data is not UNSET:
            field_dict["x509CertificateData"] = x_509_certificate_data

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ssh_certificate_data import SSHCertificateData
        from ..models.x509_certificate_data import X509CertificateData

        d = src_dict.copy()
        endpoint_configuration_id = d.pop("endpointConfigurationID")

        id = d.pop("id", UNSET)

        _ssh_certificate_data = d.pop("sshCertificateData", UNSET)
        ssh_certificate_data: Union[Unset, SSHCertificateData]
        if isinstance(_ssh_certificate_data, Unset):
            ssh_certificate_data = UNSET
        else:
            ssh_certificate_data = SSHCertificateData.from_dict(_ssh_certificate_data)

        _x_509_certificate_data = d.pop("x509CertificateData", UNSET)
        x_509_certificate_data: Union[Unset, X509CertificateData]
        if isinstance(_x_509_certificate_data, Unset):
            x_509_certificate_data = UNSET
        else:
            x_509_certificate_data = X509CertificateData.from_dict(_x_509_certificate_data)

        managed_endpoint = cls(
            endpoint_configuration_id=endpoint_configuration_id,
            id=id,
            ssh_certificate_data=ssh_certificate_data,
            x_509_certificate_data=x_509_certificate_data,
        )

        managed_endpoint.additional_properties = d
        return managed_endpoint

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
