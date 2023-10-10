from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.endpoint_configuration import EndpointConfiguration
from ...types import UNSET, Response, Unset


def _get_kwargs(
    endpoint_configuration_id: str,
    *,
    json_body: EndpointConfiguration,
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
        "method": "put",
        "url": "/endpoint-configurations/{endpointConfigurationID}".format(
            endpointConfigurationID=endpoint_configuration_id,
        ),
        "json": json_json_body,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, EndpointConfiguration]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = EndpointConfiguration.from_dict(response.json())

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
) -> Response[Union[Any, EndpointConfiguration]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    endpoint_configuration_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: EndpointConfiguration,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Response[Union[Any, EndpointConfiguration]]:
    """Update Endpoint Configuration

     Update an endpoint configuration.

    Args:
        endpoint_configuration_id (str):
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):
        json_body (EndpointConfiguration): Configuration for a managed endpoint. This object is
            experimental and subject to change. Example: {'authorityID':
            '8e3ff498-2059-4859-9053-c334ceab5f83', 'certificateInfo': {'crtFile': '/etc/db.crt',
            'duration': '24h0m0s', 'gid': 999, 'keyFile': '/etc/db.key', 'mode': 256, 'rootFile':
            '/etc/ca.crt', 'type': 'X509', 'uid': 1001}, 'hooks': {'renew': {'after': ['echo
            renewed'], 'before': ['echo renewing'], 'onError': ['echo failed to renew'], 'shell':
            '/bin/bash'}, 'sign': {'after': ['echo signed'], 'before': ['echo signing'], 'onError':
            ['echo failed to sign'], 'shell': '/bin/bash'}}, 'id':
            'd9dd9ca8-8624-4eca-84e9-ee3dd74c1786', 'keyInfo': {'format': 'DER', 'pubFile':
            '/etc/db.csr', 'type': 'ECDSA_P256'}, 'kind': 'WORKLOAD', 'name': 'My Database Server',
            'provisioner': 'Endpoints Provisioner', 'reloadInfo': {'method': 'SIGNAL', 'pidFile':
            '/var/run/db.pid', 'signal': 1}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EndpointConfiguration]]
    """

    kwargs = _get_kwargs(
        endpoint_configuration_id=endpoint_configuration_id,
        json_body=json_body,
        x_request_id=x_request_id,
        accept=accept,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    endpoint_configuration_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: EndpointConfiguration,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, EndpointConfiguration]]:
    """Update Endpoint Configuration

     Update an endpoint configuration.

    Args:
        endpoint_configuration_id (str):
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):
        json_body (EndpointConfiguration): Configuration for a managed endpoint. This object is
            experimental and subject to change. Example: {'authorityID':
            '8e3ff498-2059-4859-9053-c334ceab5f83', 'certificateInfo': {'crtFile': '/etc/db.crt',
            'duration': '24h0m0s', 'gid': 999, 'keyFile': '/etc/db.key', 'mode': 256, 'rootFile':
            '/etc/ca.crt', 'type': 'X509', 'uid': 1001}, 'hooks': {'renew': {'after': ['echo
            renewed'], 'before': ['echo renewing'], 'onError': ['echo failed to renew'], 'shell':
            '/bin/bash'}, 'sign': {'after': ['echo signed'], 'before': ['echo signing'], 'onError':
            ['echo failed to sign'], 'shell': '/bin/bash'}}, 'id':
            'd9dd9ca8-8624-4eca-84e9-ee3dd74c1786', 'keyInfo': {'format': 'DER', 'pubFile':
            '/etc/db.csr', 'type': 'ECDSA_P256'}, 'kind': 'WORKLOAD', 'name': 'My Database Server',
            'provisioner': 'Endpoints Provisioner', 'reloadInfo': {'method': 'SIGNAL', 'pidFile':
            '/var/run/db.pid', 'signal': 1}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EndpointConfiguration]
    """

    return sync_detailed(
        endpoint_configuration_id=endpoint_configuration_id,
        client=client,
        json_body=json_body,
        x_request_id=x_request_id,
        accept=accept,
    ).parsed


async def asyncio_detailed(
    endpoint_configuration_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: EndpointConfiguration,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Response[Union[Any, EndpointConfiguration]]:
    """Update Endpoint Configuration

     Update an endpoint configuration.

    Args:
        endpoint_configuration_id (str):
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):
        json_body (EndpointConfiguration): Configuration for a managed endpoint. This object is
            experimental and subject to change. Example: {'authorityID':
            '8e3ff498-2059-4859-9053-c334ceab5f83', 'certificateInfo': {'crtFile': '/etc/db.crt',
            'duration': '24h0m0s', 'gid': 999, 'keyFile': '/etc/db.key', 'mode': 256, 'rootFile':
            '/etc/ca.crt', 'type': 'X509', 'uid': 1001}, 'hooks': {'renew': {'after': ['echo
            renewed'], 'before': ['echo renewing'], 'onError': ['echo failed to renew'], 'shell':
            '/bin/bash'}, 'sign': {'after': ['echo signed'], 'before': ['echo signing'], 'onError':
            ['echo failed to sign'], 'shell': '/bin/bash'}}, 'id':
            'd9dd9ca8-8624-4eca-84e9-ee3dd74c1786', 'keyInfo': {'format': 'DER', 'pubFile':
            '/etc/db.csr', 'type': 'ECDSA_P256'}, 'kind': 'WORKLOAD', 'name': 'My Database Server',
            'provisioner': 'Endpoints Provisioner', 'reloadInfo': {'method': 'SIGNAL', 'pidFile':
            '/var/run/db.pid', 'signal': 1}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EndpointConfiguration]]
    """

    kwargs = _get_kwargs(
        endpoint_configuration_id=endpoint_configuration_id,
        json_body=json_body,
        x_request_id=x_request_id,
        accept=accept,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    endpoint_configuration_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: EndpointConfiguration,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, EndpointConfiguration]]:
    """Update Endpoint Configuration

     Update an endpoint configuration.

    Args:
        endpoint_configuration_id (str):
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):
        json_body (EndpointConfiguration): Configuration for a managed endpoint. This object is
            experimental and subject to change. Example: {'authorityID':
            '8e3ff498-2059-4859-9053-c334ceab5f83', 'certificateInfo': {'crtFile': '/etc/db.crt',
            'duration': '24h0m0s', 'gid': 999, 'keyFile': '/etc/db.key', 'mode': 256, 'rootFile':
            '/etc/ca.crt', 'type': 'X509', 'uid': 1001}, 'hooks': {'renew': {'after': ['echo
            renewed'], 'before': ['echo renewing'], 'onError': ['echo failed to renew'], 'shell':
            '/bin/bash'}, 'sign': {'after': ['echo signed'], 'before': ['echo signing'], 'onError':
            ['echo failed to sign'], 'shell': '/bin/bash'}}, 'id':
            'd9dd9ca8-8624-4eca-84e9-ee3dd74c1786', 'keyInfo': {'format': 'DER', 'pubFile':
            '/etc/db.csr', 'type': 'ECDSA_P256'}, 'kind': 'WORKLOAD', 'name': 'My Database Server',
            'provisioner': 'Endpoints Provisioner', 'reloadInfo': {'method': 'SIGNAL', 'pidFile':
            '/var/run/db.pid', 'signal': 1}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EndpointConfiguration]
    """

    return (
        await asyncio_detailed(
            endpoint_configuration_id=endpoint_configuration_id,
            client=client,
            json_body=json_body,
            x_request_id=x_request_id,
            accept=accept,
        )
    ).parsed
