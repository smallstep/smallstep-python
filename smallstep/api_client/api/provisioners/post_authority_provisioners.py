from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.provisioner import Provisioner
from ...types import UNSET, Response, Unset


def _get_kwargs(
    authority_id: str,
    *,
    json_body: Provisioner,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-Id"] = x_request_id

    if not isinstance(accept, Unset):
        headers["Accept"] = accept

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/authorities/{authorityID}/provisioners".format(
            authorityID=authority_id,
        ),
        "json": json_json_body,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Provisioner]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = Provisioner.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = cast(Any, None)
        return response_409
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, Provisioner]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    authority_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: Provisioner,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Response[Union[Any, Provisioner]]:
    """Create Authority Provisioner

     Create a new provisioner attached to an authority.

    Args:
        authority_id (str):
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):
        json_body (Provisioner): [Provisioners](https://smallstep.com/docs/step-ca/provisioners/)
            are methods of using the CA to get certificates with different modes of authorization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Provisioner]]
    """

    kwargs = _get_kwargs(
        authority_id=authority_id,
        json_body=json_body,
        x_request_id=x_request_id,
        accept=accept,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    authority_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: Provisioner,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, Provisioner]]:
    """Create Authority Provisioner

     Create a new provisioner attached to an authority.

    Args:
        authority_id (str):
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):
        json_body (Provisioner): [Provisioners](https://smallstep.com/docs/step-ca/provisioners/)
            are methods of using the CA to get certificates with different modes of authorization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Provisioner]
    """

    return sync_detailed(
        authority_id=authority_id,
        client=client,
        json_body=json_body,
        x_request_id=x_request_id,
        accept=accept,
    ).parsed


async def asyncio_detailed(
    authority_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: Provisioner,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Response[Union[Any, Provisioner]]:
    """Create Authority Provisioner

     Create a new provisioner attached to an authority.

    Args:
        authority_id (str):
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):
        json_body (Provisioner): [Provisioners](https://smallstep.com/docs/step-ca/provisioners/)
            are methods of using the CA to get certificates with different modes of authorization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Provisioner]]
    """

    kwargs = _get_kwargs(
        authority_id=authority_id,
        json_body=json_body,
        x_request_id=x_request_id,
        accept=accept,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    authority_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: Provisioner,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, Provisioner]]:
    """Create Authority Provisioner

     Create a new provisioner attached to an authority.

    Args:
        authority_id (str):
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):
        json_body (Provisioner): [Provisioners](https://smallstep.com/docs/step-ca/provisioners/)
            are methods of using the CA to get certificates with different modes of authorization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Provisioner]
    """

    return (
        await asyncio_detailed(
            authority_id=authority_id,
            client=client,
            json_body=json_body,
            x_request_id=x_request_id,
            accept=accept,
        )
    ).parsed
