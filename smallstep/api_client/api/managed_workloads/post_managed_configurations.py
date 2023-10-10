from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.managed_configuration import ManagedConfiguration
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    json_body: ManagedConfiguration,
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
        "url": "/managed-configurations",
        "json": json_json_body,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ManagedConfiguration]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = ManagedConfiguration.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
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
) -> Response[Union[Any, ManagedConfiguration]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: ManagedConfiguration,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ManagedConfiguration]]:
    """Create Managed Configuration

     Create a new managed configuration.

    Args:
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):
        json_body (ManagedConfiguration): The agent and managed endpoints used in one host. This
            object is experimental and subject to change. Example: {'agentConfigurationID':
            '12d6f7a3-2096-4ed6-b4e7-53e7f925facd', 'hostID': '8d996786-29c8-4fcd-999a-4a625be60616',
            'id': 'aad6ad55-866b-4988-a51e-58a7225db66c', 'managedEndpoints':
            [{'endpointConfigurationID': '3b872b88-bb2f-4575-b3fe-69cf92ae57f6', 'id':
            '5bad10b3-32fe-44da-b516-aef568790e66', 'x509CertificateData': {'commonName': 'db',
            'sans': ['db', 'db.internal']}}, {'endpointConfigurationID': '1f42f5fe-
            eda0-4300-bb7f-462afe483ae1', 'id': '99e45a28-36b9-4dd0-ac57-2d43aac9f36e',
            'sshCertificateData': {'keyID': 'abc123', 'principals': ['ops', 'eng']}}], 'name': 'My
            Server'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ManagedConfiguration]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
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
    json_body: ManagedConfiguration,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ManagedConfiguration]]:
    """Create Managed Configuration

     Create a new managed configuration.

    Args:
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):
        json_body (ManagedConfiguration): The agent and managed endpoints used in one host. This
            object is experimental and subject to change. Example: {'agentConfigurationID':
            '12d6f7a3-2096-4ed6-b4e7-53e7f925facd', 'hostID': '8d996786-29c8-4fcd-999a-4a625be60616',
            'id': 'aad6ad55-866b-4988-a51e-58a7225db66c', 'managedEndpoints':
            [{'endpointConfigurationID': '3b872b88-bb2f-4575-b3fe-69cf92ae57f6', 'id':
            '5bad10b3-32fe-44da-b516-aef568790e66', 'x509CertificateData': {'commonName': 'db',
            'sans': ['db', 'db.internal']}}, {'endpointConfigurationID': '1f42f5fe-
            eda0-4300-bb7f-462afe483ae1', 'id': '99e45a28-36b9-4dd0-ac57-2d43aac9f36e',
            'sshCertificateData': {'keyID': 'abc123', 'principals': ['ops', 'eng']}}], 'name': 'My
            Server'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ManagedConfiguration]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        x_request_id=x_request_id,
        accept=accept,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: ManagedConfiguration,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ManagedConfiguration]]:
    """Create Managed Configuration

     Create a new managed configuration.

    Args:
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):
        json_body (ManagedConfiguration): The agent and managed endpoints used in one host. This
            object is experimental and subject to change. Example: {'agentConfigurationID':
            '12d6f7a3-2096-4ed6-b4e7-53e7f925facd', 'hostID': '8d996786-29c8-4fcd-999a-4a625be60616',
            'id': 'aad6ad55-866b-4988-a51e-58a7225db66c', 'managedEndpoints':
            [{'endpointConfigurationID': '3b872b88-bb2f-4575-b3fe-69cf92ae57f6', 'id':
            '5bad10b3-32fe-44da-b516-aef568790e66', 'x509CertificateData': {'commonName': 'db',
            'sans': ['db', 'db.internal']}}, {'endpointConfigurationID': '1f42f5fe-
            eda0-4300-bb7f-462afe483ae1', 'id': '99e45a28-36b9-4dd0-ac57-2d43aac9f36e',
            'sshCertificateData': {'keyID': 'abc123', 'principals': ['ops', 'eng']}}], 'name': 'My
            Server'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ManagedConfiguration]]
    """

    kwargs = _get_kwargs(
        json_body=json_body,
        x_request_id=x_request_id,
        accept=accept,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: ManagedConfiguration,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ManagedConfiguration]]:
    """Create Managed Configuration

     Create a new managed configuration.

    Args:
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):
        json_body (ManagedConfiguration): The agent and managed endpoints used in one host. This
            object is experimental and subject to change. Example: {'agentConfigurationID':
            '12d6f7a3-2096-4ed6-b4e7-53e7f925facd', 'hostID': '8d996786-29c8-4fcd-999a-4a625be60616',
            'id': 'aad6ad55-866b-4988-a51e-58a7225db66c', 'managedEndpoints':
            [{'endpointConfigurationID': '3b872b88-bb2f-4575-b3fe-69cf92ae57f6', 'id':
            '5bad10b3-32fe-44da-b516-aef568790e66', 'x509CertificateData': {'commonName': 'db',
            'sans': ['db', 'db.internal']}}, {'endpointConfigurationID': '1f42f5fe-
            eda0-4300-bb7f-462afe483ae1', 'id': '99e45a28-36b9-4dd0-ac57-2d43aac9f36e',
            'sshCertificateData': {'keyID': 'abc123', 'principals': ['ops', 'eng']}}], 'name': 'My
            Server'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ManagedConfiguration]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            x_request_id=x_request_id,
            accept=accept,
        )
    ).parsed
