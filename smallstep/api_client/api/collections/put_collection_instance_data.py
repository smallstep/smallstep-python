from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_slug: str,
    instance_id: str,
    *,
    body: Any,
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
        "url": f"/collections/{collection_slug}/instances/{instance_id}/data",
    }

    _body = body

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if response.status_code == HTTPStatus.BAD_REQUEST:
        return None
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.CONFLICT:
        return None
    if response.status_code == HTTPStatus.PRECONDITION_FAILED:
        return None
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
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
    body: Any,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Save Collection Instance Data

     Add an instance to a collection or replace an existing instance.
    This is equivalent to the put-collection-instance operation except the instance data is at the top
    level of the request and response body.

    Args:
        collection_slug (str):
        instance_id (str):
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):
        body (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
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


async def asyncio_detailed(
    collection_slug: str,
    instance_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Any,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Save Collection Instance Data

     Add an instance to a collection or replace an existing instance.
    This is equivalent to the put-collection-instance operation except the instance data is at the top
    level of the request and response body.

    Args:
        collection_slug (str):
        instance_id (str):
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):
        body (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
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
