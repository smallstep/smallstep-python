from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.managed_endpoint_certificate_info_type import ManagedEndpointCertificateInfoType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ManagedEndpointCertificateInfo")


@_attrs_define
class ManagedEndpointCertificateInfo:
    """Details on a managed certificate.

    Example:
        {'crtFile': '/etc/db.crt', 'duration': '24h0m0s', 'gid': 999, 'keyFile': '/etc/db.key', 'mode': 256, 'rootFile':
            '/etc/ca.crt', 'type': 'X509', 'uid': 1001}

    Attributes:
        type (ManagedEndpointCertificateInfoType): The type of certificate.
        crt_file (Union[Unset, str]): The filepath where the certificate is to be stored.
        duration (Union[Unset, str]): The certificate lifetime. Parsed as a [Golang
            duration](https://pkg.go.dev/time#ParseDuration).
        gid (Union[Unset, int]): GID of the files where the certificate is stored.
        key_file (Union[Unset, str]): The filepath where the key is to be stored.
        mode (Union[Unset, int]): Permission bits of the files where the certificate is stored.
        root_file (Union[Unset, str]): The filepath where the root certificate is to be stored.
        uid (Union[Unset, int]): UID of the files where the certificate is stored.
    """

    type: ManagedEndpointCertificateInfoType
    crt_file: Union[Unset, str] = UNSET
    duration: Union[Unset, str] = UNSET
    gid: Union[Unset, int] = UNSET
    key_file: Union[Unset, str] = UNSET
    mode: Union[Unset, int] = UNSET
    root_file: Union[Unset, str] = UNSET
    uid: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        crt_file = self.crt_file
        duration = self.duration
        gid = self.gid
        key_file = self.key_file
        mode = self.mode
        root_file = self.root_file
        uid = self.uid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if crt_file is not UNSET:
            field_dict["crtFile"] = crt_file
        if duration is not UNSET:
            field_dict["duration"] = duration
        if gid is not UNSET:
            field_dict["gid"] = gid
        if key_file is not UNSET:
            field_dict["keyFile"] = key_file
        if mode is not UNSET:
            field_dict["mode"] = mode
        if root_file is not UNSET:
            field_dict["rootFile"] = root_file
        if uid is not UNSET:
            field_dict["uid"] = uid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ManagedEndpointCertificateInfoType(d.pop("type"))

        crt_file = d.pop("crtFile", UNSET)

        duration = d.pop("duration", UNSET)

        gid = d.pop("gid", UNSET)

        key_file = d.pop("keyFile", UNSET)

        mode = d.pop("mode", UNSET)

        root_file = d.pop("rootFile", UNSET)

        uid = d.pop("uid", UNSET)

        managed_endpoint_certificate_info = cls(
            type=type,
            crt_file=crt_file,
            duration=duration,
            gid=gid,
            key_file=key_file,
            mode=mode,
            root_file=root_file,
            uid=uid,
        )

        managed_endpoint_certificate_info.additional_properties = d
        return managed_endpoint_certificate_info

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
