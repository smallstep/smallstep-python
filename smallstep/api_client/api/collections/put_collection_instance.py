from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.collection_instance import CollectionInstance
from ...models.put_collection_instance_body import PutCollectionInstanceBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_slug: str,
    instance_id: str,
    *,
    body: PutCollectionInstanceBody,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-Id"] = x_request_id

    if not isinstance(accept, Unset):
        headers["Accept"] = accept

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/collections/{collection_slug}/instances/{instance_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, CollectionInstance]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CollectionInstance.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = cast(Any, None)
        return response_409
    if response.status_code == HTTPStatus.PRECONDITION_FAILED:
        response_412 = cast(Any, None)
        return response_412
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, CollectionInstance]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collection_slug: str,
    instance_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PutCollectionInstanceBody,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CollectionInstance]]:
    """Save Collection Instance

     Add an instance to a collection or replace an existing instance.

    Args:
        collection_slug (str):
        instance_id (str):
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):
        body (PutCollectionInstanceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CollectionInstance]]
    """

    kwargs = _get_kwargs(
        collection_slug=collection_slug,
        instance_id=instance_id,
        body=body,
        x_request_id=x_request_id,
        accept=accept,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_slug: str,
    instance_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PutCollectionInstanceBody,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CollectionInstance]]:
    """Save Collection Instance

     Add an instance to a collection or replace an existing instance.

    Args:
        collection_slug (str):
        instance_id (str):
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):
        body (PutCollectionInstanceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CollectionInstance]
    """

    return sync_detailed(
        collection_slug=collection_slug,
        instance_id=instance_id,
        client=client,
        body=body,
        x_request_id=x_request_id,
        accept=accept,
    ).parsed


async def asyncio_detailed(
    collection_slug: str,
    instance_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PutCollectionInstanceBody,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Response[Union[Any, CollectionInstance]]:
    """Save Collection Instance

     Add an instance to a collection or replace an existing instance.

    Args:
        collection_slug (str):
        instance_id (str):
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):
        body (PutCollectionInstanceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, CollectionInstance]]
    """

    kwargs = _get_kwargs(
        collection_slug=collection_slug,
        instance_id=instance_id,
        body=body,
        x_request_id=x_request_id,
        accept=accept,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_slug: str,
    instance_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PutCollectionInstanceBody,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, CollectionInstance]]:
    """Save Collection Instance

     Add an instance to a collection or replace an existing instance.

    Args:
        collection_slug (str):
        instance_id (str):
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):
        body (PutCollectionInstanceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, CollectionInstance]
    """

    return (
        await asyncio_detailed(
            collection_slug=collection_slug,
            instance_id=instance_id,
            client=client,
            body=body,
            x_request_id=x_request_id,
            accept=accept,
        )
    ).parsed
