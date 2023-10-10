from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_ssh_host_tags_pagination import GetSshHostTagsPagination
from ...models.ssh_host_tag import SSHHostTag
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    pagination: Union[Unset, None, "GetSshHostTagsPagination"] = UNSET,
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
        "url": "/tags",
        "params": params,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, List["SSHHostTag"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = SSHHostTag.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
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
) -> Response[Union[Any, List["SSHHostTag"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    pagination: Union[Unset, None, "GetSshHostTagsPagination"] = UNSET,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List["SSHHostTag"]]]:
    """List SSH Host Tags

     Paginate over all of your team's SSH host tags.

    Args:
        pagination (Union[Unset, None, GetSshHostTagsPagination]):
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['SSHHostTag']]]
    """

    kwargs = _get_kwargs(
        pagination=pagination,
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
    pagination: Union[Unset, None, "GetSshHostTagsPagination"] = UNSET,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List["SSHHostTag"]]]:
    """List SSH Host Tags

     Paginate over all of your team's SSH host tags.

    Args:
        pagination (Union[Unset, None, GetSshHostTagsPagination]):
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['SSHHostTag']]
    """

    return sync_detailed(
        client=client,
        pagination=pagination,
        x_request_id=x_request_id,
        accept=accept,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    pagination: Union[Unset, None, "GetSshHostTagsPagination"] = UNSET,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List["SSHHostTag"]]]:
    """List SSH Host Tags

     Paginate over all of your team's SSH host tags.

    Args:
        pagination (Union[Unset, None, GetSshHostTagsPagination]):
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['SSHHostTag']]]
    """

    kwargs = _get_kwargs(
        pagination=pagination,
        x_request_id=x_request_id,
        accept=accept,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    pagination: Union[Unset, None, "GetSshHostTagsPagination"] = UNSET,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List["SSHHostTag"]]]:
    """List SSH Host Tags

     Paginate over all of your team's SSH host tags.

    Args:
        pagination (Union[Unset, None, GetSshHostTagsPagination]):
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['SSHHostTag']]
    """

    return (
        await asyncio_detailed(
            client=client,
            pagination=pagination,
            x_request_id=x_request_id,
            accept=accept,
        )
    ).parsed
