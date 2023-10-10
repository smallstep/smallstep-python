from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.managed_endpoint import ManagedEndpoint


T = TypeVar("T", bound="ManagedConfiguration")


@_attrs_define
class ManagedConfiguration:
    """The agent and managed endpoints used in one host. This object is experimental and subject to change.

    Example:
        {'agentConfigurationID': '12d6f7a3-2096-4ed6-b4e7-53e7f925facd', 'hostID':
            '8d996786-29c8-4fcd-999a-4a625be60616', 'id': 'aad6ad55-866b-4988-a51e-58a7225db66c', 'managedEndpoints':
            [{'endpointConfigurationID': '3b872b88-bb2f-4575-b3fe-69cf92ae57f6', 'id':
            '5bad10b3-32fe-44da-b516-aef568790e66', 'x509CertificateData': {'commonName': 'db', 'sans': ['db',
            'db.internal']}}, {'endpointConfigurationID': '1f42f5fe-eda0-4300-bb7f-462afe483ae1', 'id':
            '99e45a28-36b9-4dd0-ac57-2d43aac9f36e', 'sshCertificateData': {'keyID': 'abc123', 'principals': ['ops',
            'eng']}}], 'name': 'My Server'}

    Attributes:
        agent_configuration_id (str): UUID identifying the agent configuration.
        managed_endpoints (List['ManagedEndpoint']): The list of endpoints managed by this configuration.
        name (str): The name of this managed configuration.
        host_id (Union[Unset, str]): UUID identifying the host this managed configuration is for. Will be generated on
            server-side if not provided.
        id (Union[Unset, str]): UUID identifying this managed configuration. Read only.
    """

    agent_configuration_id: str
    managed_endpoints: List["ManagedEndpoint"]
    name: str
    host_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        agent_configuration_id = self.agent_configuration_id
        managed_endpoints = []
        for managed_endpoints_item_data in self.managed_endpoints:
            managed_endpoints_item = managed_endpoints_item_data.to_dict()

            managed_endpoints.append(managed_endpoints_item)

        name = self.name
        host_id = self.host_id
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agentConfigurationID": agent_configuration_id,
                "managedEndpoints": managed_endpoints,
                "name": name,
            }
        )
        if host_id is not UNSET:
            field_dict["hostID"] = host_id
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.managed_endpoint import ManagedEndpoint

        d = src_dict.copy()
        agent_configuration_id = d.pop("agentConfigurationID")

        managed_endpoints = []
        _managed_endpoints = d.pop("managedEndpoints")
        for managed_endpoints_item_data in _managed_endpoints:
            managed_endpoints_item = ManagedEndpoint.from_dict(managed_endpoints_item_data)

            managed_endpoints.append(managed_endpoints_item)

        name = d.pop("name")

        host_id = d.pop("hostID", UNSET)

        id = d.pop("id", UNSET)

        managed_configuration = cls(
            agent_configuration_id=agent_configuration_id,
            managed_endpoints=managed_endpoints,
            name=name,
            host_id=host_id,
            id=id,
        )

        managed_configuration.additional_properties = d
        return managed_configuration

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
