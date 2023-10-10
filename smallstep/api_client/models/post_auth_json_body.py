from io import BytesIO
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_auth_json_body_audience import PostAuthJsonBodyAudience
from ..types import UNSET, File, FileJsonType, Unset

T = TypeVar("T", bound="PostAuthJsonBody")


@_attrs_define
class PostAuthJsonBody:
    """
    Attributes:
        audience (Union[Unset, PostAuthJsonBodyAudience]):
        bundle (Union[Unset, List[File]]):
        team_id (Union[Unset, str]):
        team_slug (Union[Unset, str]):
    """

    audience: Union[Unset, PostAuthJsonBodyAudience] = UNSET
    bundle: Union[Unset, List[File]] = UNSET
    team_id: Union[Unset, str] = UNSET
    team_slug: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        audience: Union[Unset, str] = UNSET
        if not isinstance(self.audience, Unset):
            audience = self.audience.value

        bundle: Union[Unset, List[FileJsonType]] = UNSET
        if not isinstance(self.bundle, Unset):
            bundle = []
            for bundle_item_data in self.bundle:
                bundle_item = bundle_item_data.to_tuple()

                bundle.append(bundle_item)

        team_id = self.team_id
        team_slug = self.team_slug

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if audience is not UNSET:
            field_dict["audience"] = audience
        if bundle is not UNSET:
            field_dict["bundle"] = bundle
        if team_id is not UNSET:
            field_dict["teamID"] = team_id
        if team_slug is not UNSET:
            field_dict["teamSlug"] = team_slug

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _audience = d.pop("audience", UNSET)
        audience: Union[Unset, PostAuthJsonBodyAudience]
        if isinstance(_audience, Unset):
            audience = UNSET
        else:
            audience = PostAuthJsonBodyAudience(_audience)

        bundle = []
        _bundle = d.pop("bundle", UNSET)
        for bundle_item_data in _bundle or []:
            bundle_item = File(payload=BytesIO(bundle_item_data))

            bundle.append(bundle_item)

        team_id = d.pop("teamID", UNSET)

        team_slug = d.pop("teamSlug", UNSET)

        post_auth_json_body = cls(
            audience=audience,
            bundle=bundle,
            team_id=team_id,
            team_slug=team_slug,
        )

        post_auth_json_body.additional_properties = d
        return post_auth_json_body

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
