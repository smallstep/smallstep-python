from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.vpn_connection_type import VPNConnectionType
from ..models.vpn_vendor import VPNVendor
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ike_v2_config import IkeV2Config


T = TypeVar("T", bound="VPN")


@_attrs_define
class VPN:
    """Configuration to connect a device to a VPN.

    Attributes:
        connection_type (VPNConnectionType):
        remote_address (str):
        autojoin (Union[Unset, bool]):
        ike (Union[Unset, IkeV2Config]):
        vendor (Union[Unset, VPNVendor]):
    """

    connection_type: VPNConnectionType
    remote_address: str
    autojoin: Union[Unset, bool] = UNSET
    ike: Union[Unset, "IkeV2Config"] = UNSET
    vendor: Union[Unset, VPNVendor] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_type = self.connection_type.value

        remote_address = self.remote_address

        autojoin = self.autojoin

        ike: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ike, Unset):
            ike = self.ike.to_dict()

        vendor: Union[Unset, str] = UNSET
        if not isinstance(self.vendor, Unset):
            vendor = self.vendor.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectionType": connection_type,
                "remoteAddress": remote_address,
            }
        )
        if autojoin is not UNSET:
            field_dict["autojoin"] = autojoin
        if ike is not UNSET:
            field_dict["ike"] = ike
        if vendor is not UNSET:
            field_dict["vendor"] = vendor

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.ike_v2_config import IkeV2Config

        d = src_dict.copy()
        connection_type = VPNConnectionType(d.pop("connectionType"))

        remote_address = d.pop("remoteAddress")

        autojoin = d.pop("autojoin", UNSET)

        _ike = d.pop("ike", UNSET)
        ike: Union[Unset, IkeV2Config]
        if isinstance(_ike, Unset):
            ike = UNSET
        else:
            ike = IkeV2Config.from_dict(_ike)

        _vendor = d.pop("vendor", UNSET)
        vendor: Union[Unset, VPNVendor]
        if isinstance(_vendor, Unset):
            vendor = UNSET
        else:
            vendor = VPNVendor(_vendor)

        vpn = cls(
            connection_type=connection_type,
            remote_address=remote_address,
            autojoin=autojoin,
            ike=ike,
            vendor=vendor,
        )

        vpn.additional_properties = d
        return vpn

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
