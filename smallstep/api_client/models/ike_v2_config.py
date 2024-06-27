from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IkeV2Config")


@_attrs_define
class IkeV2Config:
    """
    Attributes:
        ca_chain (Union[Unset, str]):
        eap (Union[Unset, bool]):
        remote_id (Union[Unset, str]): Typically, the common name of the remote server. Defaults to the remote address.
    """

    ca_chain: Union[Unset, str] = UNSET
    eap: Union[Unset, bool] = UNSET
    remote_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ca_chain = self.ca_chain

        eap = self.eap

        remote_id = self.remote_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ca_chain is not UNSET:
            field_dict["caChain"] = ca_chain
        if eap is not UNSET:
            field_dict["eap"] = eap
        if remote_id is not UNSET:
            field_dict["remoteID"] = remote_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ca_chain = d.pop("caChain", UNSET)

        eap = d.pop("eap", UNSET)

        remote_id = d.pop("remoteID", UNSET)

        ike_v2_config = cls(
            ca_chain=ca_chain,
            eap=eap,
            remote_id=remote_id,
        )

        ike_v2_config.additional_properties = d
        return ike_v2_config

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
