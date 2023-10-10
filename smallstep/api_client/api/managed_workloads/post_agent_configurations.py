from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_configuration import AgentConfiguration
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    json_body: AgentConfiguration,
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
        "url": "/agent-configurations",
        "json": json_json_body,
        "headers": headers,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AgentConfiguration, Any]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = AgentConfiguration.from_dict(response.json())

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
) -> Response[Union[AgentConfiguration, Any]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: AgentConfiguration,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Response[Union[AgentConfiguration, Any]]:
    """Create Agent Configuration

     Create a new agent configuration.

    Args:
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):
        json_body (AgentConfiguration): The agent configuration describes the attestation
            authority used by the agent to grant workload certificates. This object is experimental
            and subject to change. Example: {'attestationSlug': 'teamfooattestationca', 'authorityID':
            '60bba807-d3dc-414f-90c9-968a0e3b28c3', 'id': '59b4489d-f731-4ae2-8339-16cf829d143d',
            'name': 'Agent 1', 'provisioner': 'agentsattestor'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AgentConfiguration, Any]]
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
    json_body: AgentConfiguration,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Optional[Union[AgentConfiguration, Any]]:
    """Create Agent Configuration

     Create a new agent configuration.

    Args:
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):
        json_body (AgentConfiguration): The agent configuration describes the attestation
            authority used by the agent to grant workload certificates. This object is experimental
            and subject to change. Example: {'attestationSlug': 'teamfooattestationca', 'authorityID':
            '60bba807-d3dc-414f-90c9-968a0e3b28c3', 'id': '59b4489d-f731-4ae2-8339-16cf829d143d',
            'name': 'Agent 1', 'provisioner': 'agentsattestor'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AgentConfiguration, Any]
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
    json_body: AgentConfiguration,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Response[Union[AgentConfiguration, Any]]:
    """Create Agent Configuration

     Create a new agent configuration.

    Args:
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):
        json_body (AgentConfiguration): The agent configuration describes the attestation
            authority used by the agent to grant workload certificates. This object is experimental
            and subject to change. Example: {'attestationSlug': 'teamfooattestationca', 'authorityID':
            '60bba807-d3dc-414f-90c9-968a0e3b28c3', 'id': '59b4489d-f731-4ae2-8339-16cf829d143d',
            'name': 'Agent 1', 'provisioner': 'agentsattestor'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AgentConfiguration, Any]]
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
    json_body: AgentConfiguration,
    x_request_id: Union[Unset, str] = UNSET,
    accept: Union[Unset, str] = UNSET,
) -> Optional[Union[AgentConfiguration, Any]]:
    """Create Agent Configuration

     Create a new agent configuration.

    Args:
        x_request_id (Union[Unset, str]):
        accept (Union[Unset, str]):
        json_body (AgentConfiguration): The agent configuration describes the attestation
            authority used by the agent to grant workload certificates. This object is experimental
            and subject to change. Example: {'attestationSlug': 'teamfooattestationca', 'authorityID':
            '60bba807-d3dc-414f-90c9-968a0e3b28c3', 'id': '59b4489d-f731-4ae2-8339-16cf829d143d',
            'name': 'Agent 1', 'provisioner': 'agentsattestor'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AgentConfiguration, Any]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            x_request_id=x_request_id,
            accept=accept,
        )
    ).parsed
