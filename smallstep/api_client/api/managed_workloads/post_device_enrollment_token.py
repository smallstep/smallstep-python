from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.device_enrollment_token import DeviceEnrollmentToken
from ...models.new_device_enrollment_token import NewDeviceEnrollmentToken
from ...types import UNSET, Response, Unset


def _get_kwargs(
    collection_slug: str,
    instance_id: str,
    *,
    json_body: NewDeviceEnrollmentToken,
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
        "url": "/device-collections/{collectionSlug}/{instanceID}/enrollment-token".format(
            collectionSlug=collection_slug,
            instanceID=instance_id,
        ),
        "json": json_json_body,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DeviceEnrollmentToken]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = DeviceEnrollmentToken.from_dict(response.json())

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
) -> Response[Union[Any, DeviceEnrollmentToken]]:
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
    json_body: NewDeviceEnrollmentToken,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Response[Union[Any, DeviceEnrollmentToken]]:
    """Generate Device Enrollment Token

     Create a new device enrollment.

    Args:
        collection_slug (str):
        instance_id (str):
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):
        json_body (NewDeviceEnrollmentToken): The body of a request to generate a new device
            enrollment token.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeviceEnrollmentToken]]
    """

    kwargs = _get_kwargs(
        collection_slug=collection_slug,
        instance_id=instance_id,
        json_body=json_body,
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
    json_body: NewDeviceEnrollmentToken,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, DeviceEnrollmentToken]]:
    """Generate Device Enrollment Token

     Create a new device enrollment.

    Args:
        collection_slug (str):
        instance_id (str):
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):
        json_body (NewDeviceEnrollmentToken): The body of a request to generate a new device
            enrollment token.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeviceEnrollmentToken]
    """

    return sync_detailed(
        collection_slug=collection_slug,
        instance_id=instance_id,
        client=client,
        json_body=json_body,
        x_request_id=x_request_id,
        accept=accept,
    ).parsed


async def asyncio_detailed(
    collection_slug: str,
    instance_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: NewDeviceEnrollmentToken,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Response[Union[Any, DeviceEnrollmentToken]]:
    """Generate Device Enrollment Token

     Create a new device enrollment.

    Args:
        collection_slug (str):
        instance_id (str):
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):
        json_body (NewDeviceEnrollmentToken): The body of a request to generate a new device
            enrollment token.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeviceEnrollmentToken]]
    """

    kwargs = _get_kwargs(
        collection_slug=collection_slug,
        instance_id=instance_id,
        json_body=json_body,
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
    json_body: NewDeviceEnrollmentToken,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, DeviceEnrollmentToken]]:
    """Generate Device Enrollment Token

     Create a new device enrollment.

    Args:
        collection_slug (str):
        instance_id (str):
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):
        json_body (NewDeviceEnrollmentToken): The body of a request to generate a new device
            enrollment token.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeviceEnrollmentToken]
    """

    return (
        await asyncio_detailed(
            collection_slug=collection_slug,
            instance_id=instance_id,
            client=client,
            json_body=json_body,
            x_request_id=x_request_id,
            accept=accept,
        )
    ).parsed
