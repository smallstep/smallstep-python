# smallstep-api-client

A client library for accessing the [Smallstep API](https://gateway.smallstep.com/).

## Usage

First, create a client:

```python
from smallstep_python.api_client import Client

client = Client(base_url="https://gateway.smallstep.com/api")
```

If the endpoints you're going to hit require authentication, use `AuthenticatedClient` instead:

```python
from smallstep_python.api_client import AuthenticatedClient

client = AuthenticatedClient(base_url="https://gateway.smallstep.com/api", token="SuperSecretToken")
```

Now call your endpoint and use your models:

```python
from smallstep_python.api_client.models import Authority
from smallstep_python.api_client.api.authorities import get_authorities
from smallstep_python.api_client.types import Response

with client as client:
    my_authorities: Authority = get_authorities.sync(client=client)
    # or if you need more info (e.g. status_code)
    response: Response[Authority] = get_authorities.sync_detailed(client=client)
```

Or do the same thing with an async version:

```python
from smallstep_python.api_client.models import Authority
from smallstep_python.api_client.api.authorities import authorities
from smallstep_python.api_client.types import Response

async with client as client:
    my_authorities: Authority = await get_authorities.asyncio(client=client)
    response: Response[Authority] = await get_authorities.asyncio_detailed(client=client)
```

Things to know:

1. Every path/method combo becomes a Python module with four functions:
    1. `sync`: Blocking request that returns parsed data (if successful) or `None`
    1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
    1. `asyncio`: Like `sync` but async instead of blocking
    1. `asyncio_detailed`: Like `sync_detailed` but async instead of blocking

1. All path/query params, and bodies become method arguments.
1. If your endpoint had any tags on it, the first tag will be used as a module name for the function (authorities above)
1. Any endpoint which did not have a tag will be in `smallstep_python.api_client.api.default`

## Advanced customizations

There are more settings on the generated `Client` class which let you control more runtime behavior, check out the docstring on that class for more info. You can also customize the underlying `httpx.Client` or `httpx.AsyncClient` (depending on your use-case):

```python
from smallstep_python.api_client import Client

def log_request(request):
    print(f"Request event hook: {request.method} {request.url} - Waiting for response")

def log_response(response):
    request = response.request
    print(f"Response event hook: {request.method} {request.url} - Status {response.status_code}")

client = Client(
    base_url="https://gateway.smallstep.com/api",
    httpx_args={"event_hooks": {"request": [log_request], "response": [log_response]}},
)

# Or get the underlying httpx client to modify directly with client.get_httpx_client() or client.get_async_httpx_client()
```

You can even set the httpx client directly, but beware that this will override any existing settings (e.g., base_url):

```python
import httpx
from smallstep_python.api_client import Client

client = Client(
    base_url="https://gateway.smallstep.com/api",
)
# Note that base_url needs to be re-set, as would any shared cookies, headers, etc.
client.set_httpx_client(httpx.Client(base_url="https://gateway.smallstep.com/api", proxies="http://localhost:8030"))
```

## Building / publishing this package

This project uses [Poetry](https://python-poetry.org/) to manage dependencies  and packaging.  Here are the basics:

1. Update the metadata in pyproject.toml (e.g. authors, version)
1. If you're using a private repository, configure it with Poetry
    1. `poetry config repositories.<your-repository-name> <url-to-your-repository>`
    1. `poetry config http-basic.<your-repository-name> <username> <password>`
1. Publish the client with `poetry publish --build -r <your-repository-name>` or, if for public PyPI, just `poetry publish --build`

If you want to install this client into another project without publishing it (e.g. for development) then:

1. If that project **is using Poetry**, you can simply do `poetry add <path-to-this-client>` from that project
1. If that project is not using Poetry:
    1. Build a wheel with `poetry build -f wheel`
    1. Install that wheel from the other project `pip install <path-to-wheel>`
