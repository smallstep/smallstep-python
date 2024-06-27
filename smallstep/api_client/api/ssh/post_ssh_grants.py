from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.new_ssh_grant import NewSSHGrant
from ...models.ssh_host_grant import SSHHostGrant
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: NewSSHGrant,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-Id"] = x_request_id

    if not isinstance(accept, Unset):
        headers["Accept"] = accept

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/grants",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, SSHHostGrant]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = SSHHostGrant.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, SSHHostGrant]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: NewSSHGrant,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Response[Union[Any, SSHHostGrant]]:
    """Create SSH Grant

     Add an SSH grant to a group.

    Args:
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):
        body (NewSSHGrant): The body of a request to add a grant to a group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SSHHostGrant]]
    """

    kwargs = _get_kwargs(
        body=body,
        x_request_id=x_request_id,
        accept=accept,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: NewSSHGrant,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, SSHHostGrant]]:
    """Create SSH Grant

     Add an SSH grant to a group.

    Args:
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):
        body (NewSSHGrant): The body of a request to add a grant to a group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SSHHostGrant]
    """

    return sync_detailed(
        client=client,
        body=body,
        x_request_id=x_request_id,
        accept=accept,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: NewSSHGrant,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Response[Union[Any, SSHHostGrant]]:
    """Create SSH Grant

     Add an SSH grant to a group.

    Args:
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):
        body (NewSSHGrant): The body of a request to add a grant to a group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SSHHostGrant]]
    """

    kwargs = _get_kwargs(
        body=body,
        x_request_id=x_request_id,
        accept=accept,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: NewSSHGrant,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, SSHHostGrant]]:
    """Create SSH Grant

     Add an SSH grant to a group.

    Args:
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):
        body (NewSSHGrant): The body of a request to add a grant to a group.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SSHHostGrant]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_request_id=x_request_id,
            accept=accept,
        )
    ).parsed
