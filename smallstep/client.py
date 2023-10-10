# SPDX-License-Identifier: Apache-2.0
#
# Copyright (c) 2023 Smallstep Labs, Inc <techadmin@smallstep.com> All Rights Reserved.
# Apache-2.0 (see LICENSE or https://opensource.org/license/apache-2-0/)

from . import config
from .api_client import AuthenticatedClient


class StepClient(AuthenticatedClient):
    def __init__(self, smallstep_api_host: str = None, smallstep_api_token: str = None, **kwargs):
        settings = config.get_settings(smallstep_api_host, smallstep_api_token)
        self.base_url = settings.smallstep_api_host
        self.token = settings.smallstep_api_token
        self.raise_on_unexpected_status = True
        super().__init__(
            self.base_url,
            self.token,
            raise_on_unexpected_status=self.raise_on_unexpected_status,
            headers={"User-Agent": settings.smallstep_user_agent},
            **kwargs,
        )
