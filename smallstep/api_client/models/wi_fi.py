from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WiFi")


@_attrs_define
class WiFi:
    """Configuration to connect a device to a protected WiFi network.

    Attributes:
        ssid (str):
        autojoin (Union[Unset, bool]):
        ca_chain (Union[Unset, str]):
        external_radius_server (Union[Unset, bool]):
        hidden (Union[Unset, bool]):
        network_access_server_ip (Union[Unset, str]):
    """

    ssid: str
    autojoin: Union[Unset, bool] = UNSET
    ca_chain: Union[Unset, str] = UNSET
    external_radius_server: Union[Unset, bool] = UNSET
    hidden: Union[Unset, bool] = UNSET
    network_access_server_ip: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ssid = self.ssid

        autojoin = self.autojoin

        ca_chain = self.ca_chain

        external_radius_server = self.external_radius_server

        hidden = self.hidden

        network_access_server_ip = self.network_access_server_ip

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ssid": ssid,
            }
        )
        if autojoin is not UNSET:
            field_dict["autojoin"] = autojoin
        if ca_chain is not UNSET:
            field_dict["caChain"] = ca_chain
        if external_radius_server is not UNSET:
            field_dict["externalRadiusServer"] = external_radius_server
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if network_access_server_ip is not UNSET:
            field_dict["networkAccessServerIP"] = network_access_server_ip

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ssid = d.pop("ssid")

        autojoin = d.pop("autojoin", UNSET)

        ca_chain = d.pop("caChain", UNSET)

        external_radius_server = d.pop("externalRadiusServer", UNSET)

        hidden = d.pop("hidden", UNSET)

        network_access_server_ip = d.pop("networkAccessServerIP", UNSET)

        wi_fi = cls(
            ssid=ssid,
            autojoin=autojoin,
            ca_chain=ca_chain,
            external_radius_server=external_radius_server,
            hidden=hidden,
            network_access_server_ip=network_access_server_ip,
        )

        wi_fi.additional_properties = d
        return wi_fi

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
