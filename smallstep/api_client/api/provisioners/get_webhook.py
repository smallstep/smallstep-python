from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.provisioner_webhook import ProvisionerWebhook
from ...types import UNSET, Response, Unset


def _get_kwargs(
    authority_id: str,
    provisioner_name_or_id: str,
    webhook_name_or_id: str,
    *,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers = {}
    if not isinstance(x_request_id, Unset):
        headers["X-Request-Id"] = x_request_id

    if not isinstance(accept, Unset):
        headers["Accept"] = accept

    return {
        "method": "get",
        "url": "/authorities/{authorityID}/provisioners/{provisionerNameOrID}/webhooks/{webhookNameOrID}".format(
            authorityID=authority_id,
            provisionerNameOrID=provisioner_name_or_id,
            webhookNameOrID=webhook_name_or_id,
        ),
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ProvisionerWebhook]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ProvisionerWebhook.from_dict(response.json())

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
) -> Response[Union[Any, ProvisionerWebhook]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    authority_id: str,
    provisioner_name_or_id: str,
    webhook_name_or_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ProvisionerWebhook]]:
    """Get Provisioner Webhook

     Get a single provisioner webhook by name or ID.

    Args:
        authority_id (str):
        provisioner_name_or_id (str):
        webhook_name_or_id (str):
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProvisionerWebhook]]
    """

    kwargs = _get_kwargs(
        authority_id=authority_id,
        provisioner_name_or_id=provisioner_name_or_id,
        webhook_name_or_id=webhook_name_or_id,
        x_request_id=x_request_id,
        accept=accept,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    authority_id: str,
    provisioner_name_or_id: str,
    webhook_name_or_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ProvisionerWebhook]]:
    """Get Provisioner Webhook

     Get a single provisioner webhook by name or ID.

    Args:
        authority_id (str):
        provisioner_name_or_id (str):
        webhook_name_or_id (str):
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProvisionerWebhook]
    """

    return sync_detailed(
        authority_id=authority_id,
        provisioner_name_or_id=provisioner_name_or_id,
        webhook_name_or_id=webhook_name_or_id,
        client=client,
        x_request_id=x_request_id,
        accept=accept,
    ).parsed


async def asyncio_detailed(
    authority_id: str,
    provisioner_name_or_id: str,
    webhook_name_or_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ProvisionerWebhook]]:
    """Get Provisioner Webhook

     Get a single provisioner webhook by name or ID.

    Args:
        authority_id (str):
        provisioner_name_or_id (str):
        webhook_name_or_id (str):
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProvisionerWebhook]]
    """

    kwargs = _get_kwargs(
        authority_id=authority_id,
        provisioner_name_or_id=provisioner_name_or_id,
        webhook_name_or_id=webhook_name_or_id,
        x_request_id=x_request_id,
        accept=accept,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    authority_id: str,
    provisioner_name_or_id: str,
    webhook_name_or_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ProvisionerWebhook]]:
    """Get Provisioner Webhook

     Get a single provisioner webhook by name or ID.

    Args:
        authority_id (str):
        provisioner_name_or_id (str):
        webhook_name_or_id (str):
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProvisionerWebhook]
    """

    return (
        await asyncio_detailed(
            authority_id=authority_id,
            provisioner_name_or_id=provisioner_name_or_id,
            webhook_name_or_id=webhook_name_or_id,
            client=client,
            x_request_id=x_request_id,
            accept=accept,
        )
    ).parsed
