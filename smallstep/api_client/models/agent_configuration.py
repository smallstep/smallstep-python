from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentConfiguration")


@_attrs_define
class AgentConfiguration:
    """The agent configuration describes the attestation authority used by the agent to grant workload certificates. This
    object is experimental and subject to change.

        Example:
            {'attestationSlug': 'teamfooattestationca', 'authorityID': '60bba807-d3dc-414f-90c9-968a0e3b28c3', 'id':
                '59b4489d-f731-4ae2-8339-16cf829d143d', 'name': 'Agent 1', 'provisioner': 'agentsattestor'}

        Attributes:
            authority_id (str): UUID identifying the authority the agent uses to generate endpoint certificates.
            name (str): The name of this agent configuration.
            provisioner (str): The name of the provisioner on the authority the agent uses to generate endpoint
                certificates.
            attestation_slug (Union[Unset, str]): The slug of the attestation authority the agent connects to to get a
                certificate.
            id (Union[Unset, str]): A UUID identifying this agent configuration. Read only.
    """

    authority_id: str
    name: str
    provisioner: str
    attestation_slug: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        authority_id = self.authority_id
        name = self.name
        provisioner = self.provisioner
        attestation_slug = self.attestation_slug
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authorityID": authority_id,
                "name": name,
                "provisioner": provisioner,
            }
        )
        if attestation_slug is not UNSET:
            field_dict["attestationSlug"] = attestation_slug
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        authority_id = d.pop("authorityID")

        name = d.pop("name")

        provisioner = d.pop("provisioner")

        attestation_slug = d.pop("attestationSlug", UNSET)

        id = d.pop("id", UNSET)

        agent_configuration = cls(
            authority_id=authority_id,
            name=name,
            provisioner=provisioner,
            attestation_slug=attestation_slug,
            id=id,
        )

        agent_configuration.additional_properties = d
        return agent_configuration

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
