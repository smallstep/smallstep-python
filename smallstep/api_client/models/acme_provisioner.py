from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.acme_provisioner_challenges_item import ACMEProvisionerChallengesItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="ACMEProvisioner")


@_attrs_define
class ACMEProvisioner:
    """A [provisioner](https://smallstep.com/docs/step-ca/provisioners/#acme) that enables automation with the [ACME
    protocol](https://smallstep.com/docs/step-ca/acme-basics/#acme-challenges).

        Attributes:
            challenges (List[ACMEProvisionerChallengesItem]): Which ACME challenge types are allowed.
            require_eab (bool): Only ACME clients that have been preconfigured with valid EAB credentials will be able to
                create an account with this provisioner. Must be `true` for all new provisioners.
            force_cn (Union[Unset, bool]): Force one of the SANs to become the Common Name, if a Common Name is not
                provided.
    """

    challenges: List[ACMEProvisionerChallengesItem]
    require_eab: bool
    force_cn: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        challenges = []
        for challenges_item_data in self.challenges:
            challenges_item = challenges_item_data.value

            challenges.append(challenges_item)

        require_eab = self.require_eab
        force_cn = self.force_cn

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "challenges": challenges,
                "requireEAB": require_eab,
            }
        )
        if force_cn is not UNSET:
            field_dict["forceCN"] = force_cn

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        challenges = []
        _challenges = d.pop("challenges")
        for challenges_item_data in _challenges:
            challenges_item = ACMEProvisionerChallengesItem(challenges_item_data)

            challenges.append(challenges_item)

        require_eab = d.pop("requireEAB")

        force_cn = d.pop("forceCN", UNSET)

        acme_provisioner = cls(
            challenges=challenges,
            require_eab=require_eab,
            force_cn=force_cn,
        )

        acme_provisioner.additional_properties = d
        return acme_provisioner

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
