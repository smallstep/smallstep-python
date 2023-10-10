# smallstep-python

smallstep-python is a Python library at allows you to interface with the Smallstep API.

We use [openapi-python-client](https://github.com/openapi-generators/openapi-python-client) to generate a low level Python client that is located in `smallstep/api_client/`. See the `smallstep/README.md` for more information on using this generated library. We built a wrapper library on top of `smallstep/api_client` that is located in `api.py`. This adds a handful of helper features. At this time `smallstep/api.py` only supports a few API endpoints. See `smallstep/api.py` for details.

## Requirements

* Python 3.9
* [Smallstep Account](https://smallstep.com/signup)
* A very strong desire to allow a cute snake to manage your Smallstep account

## Development

### Configuration

Create a `.env` file in the project root and add the following lines:

```bash
# Not needed unless you are using our run anywhere offering
# SMALLSTEP_API_HOST="https://gateway.smallstep.com/api"
SMALLSTEP_API_TOKEN="your_smallstep_api_token"
```

Adjust them to your needs. See `config.py` for configuration details. We use [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) for easy settings management. Below is the order of precedence for configuration settings:

1. Arguments passed to the Settings class initialiser.
1. Environment variables, e.g. SMALLSTEP_MY_CONFIG_SETTING as described above.
1. Variables loaded from a dotenv (.env) file.
1. Variables loaded from the secrets directory.
1. The default field values for the Settings model.

See the Pydantic Settings [field value priority](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#field-value-priority) section for more information.

## With Poetry

Install Poetry on your system with [this](https://python-poetry.org/docs/#installation).

Run this from the repo directory:

```bash
poetry install
```

Enter the Poetry shell with this:

```bash
poetry shell
pre-commit install
```

### With venv

```bash
export VIRTUAL_ENV=${PWD}/.venv
python3 -m venv $VIRTUAL_ENV
export PATH="$VIRTUAL_ENV/bin:$PATH"
pip install wheel
pip install -r requirements.txt
. .venv/bin/activate
pre-commit install
```

### Adding packages

Add packages to Poetry and then run pre-commit which will generate a requirements.txt file for you.

Development:

```bash
poetry add --group=dev rich
pre-commit
```

Production:

```bash
poetry add rich
pre-commit
```

## License

[Apache License Version 2.0](http://www.apache.org/licenses/LICENSE-2.0)

Copyright 2023 Smallstep Labs Inc.
