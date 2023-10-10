# SPDX-License-Identifier: Apache-2.0
#
# Copyright (c) 2023 Smallstep Labs, Inc <techadmin@smallstep.com> All Rights Reserved.
# Apache-2.0 (see LICENSE or https://opensource.org/license/apache-2-0/)

import sys
from functools import lru_cache

from pydantic import ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict

VERSION: str = "0.0.1"


@lru_cache()
def get_settings(smallstep_api_host=None, smallstep_api_token=None):
    incoming_params = {
        "smallstep_api_host": smallstep_api_host,
        "smallstep_api_token": smallstep_api_token,
    }
    set_params = {k: v for k, v in incoming_params.items() if v is not None}
    try:
        Settings(**set_params)
    except ValidationError as exc:
        for errors in list(exc.errors()):
            print(f"{errors['msg']}: {errors['loc'][0]}")
        sys.exit("Exiting...")
    return Settings(**set_params)


class Settings(BaseSettings):
    smallstep_api_host: str = "https://gateway.smallstep.com/api"
    smallstep_api_token: str
    smallstep_user_agent: str = f"smallstep-python/{VERSION}"

    model_config = SettingsConfigDict(env_file=".env", extra="forbid")
