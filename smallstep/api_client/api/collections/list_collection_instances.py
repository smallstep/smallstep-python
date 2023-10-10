from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.collection_instance import CollectionInstance
from ...models.list_collection_instances_pagination import ListCollectionInstancesPagination
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_slug: str,
    *,
    pagination: Union[Unset, None, "ListCollectionInstancesPagination"] = UNSET,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-Id"] = x_request_id

    if not isinstance(accept, Unset):
        headers["Accept"] = accept

    params: Dict[str, Any] = {}
    json_pagination: Union[Unset, None, Dict[str, Any]] = UNSET
    if not isinstance(pagination, Unset):
        json_pagination = pagination.to_dict() if pagination else None

    if not isinstance(json_pagination, Unset) and json_pagination is not None:
        params.update(json_pagination)

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/collections/{collectionSlug}/items".format(
            collectionSlug=collection_slug,
        ),
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["CollectionInstance"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CollectionInstance.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, List["CollectionInstance"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collection_slug: str,
    *,
    client: Union[AuthenticatedClient, Client],
    pagination: Union[Unset, None, "ListCollectionInstancesPagination"] = UNSET,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List["CollectionInstance"]]]:
    """List Collection Instances

     Paginate over all instances in a collection.

    Args:
        collection_slug (str):
        pagination (Union[Unset, None, ListCollectionInstancesPagination]):
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['CollectionInstance']]]
    """

    kwargs = _get_kwargs(
        collection_slug=collection_slug,
        pagination=pagination,
        x_request_id=x_request_id,
        accept=accept,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_slug: str,
    *,
    client: Union[AuthenticatedClient, Client],
    pagination: Union[Unset, None, "ListCollectionInstancesPagination"] = UNSET,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List["CollectionInstance"]]]:
    """List Collection Instances

     Paginate over all instances in a collection.

    Args:
        collection_slug (str):
        pagination (Union[Unset, None, ListCollectionInstancesPagination]):
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['CollectionInstance']]
    """

    return sync_detailed(
        collection_slug=collection_slug,
        client=client,
        pagination=pagination,
        x_request_id=x_request_id,
        accept=accept,
    ).parsed


async def asyncio_detailed(
    collection_slug: str,
    *,
    client: Union[AuthenticatedClient, Client],
    pagination: Union[Unset, None, "ListCollectionInstancesPagination"] = UNSET,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List["CollectionInstance"]]]:
    """List Collection Instances

     Paginate over all instances in a collection.

    Args:
        collection_slug (str):
        pagination (Union[Unset, None, ListCollectionInstancesPagination]):
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['CollectionInstance']]]
    """

    kwargs = _get_kwargs(
        collection_slug=collection_slug,
        pagination=pagination,
        x_request_id=x_request_id,
        accept=accept,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_slug: str,
    *,
    client: Union[AuthenticatedClient, Client],
    pagination: Union[Unset, None, "ListCollectionInstancesPagination"] = UNSET,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List["CollectionInstance"]]]:
    """List Collection Instances

     Paginate over all instances in a collection.

    Args:
        collection_slug (str):
        pagination (Union[Unset, None, ListCollectionInstancesPagination]):
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['CollectionInstance']]
    """

    return (
        await asyncio_detailed(
            collection_slug=collection_slug,
            client=client,
            pagination=pagination,
            x_request_id=x_request_id,
            accept=accept,
        )
    ).parsed
