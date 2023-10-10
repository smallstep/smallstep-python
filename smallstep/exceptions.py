# SPDX-License-Identifier: Apache-2.0
#
# Copyright (c) 2023 Smallstep Labs, Inc <techadmin@smallstep.com> All Rights Reserved.
# Apache-2.0 (see LICENSE or https://opensource.org/license/apache-2-0/)


class StepException(Exception):
    def __init__(self, status_code: int, message: dict, headers: dict):
        self.status_code = status_code
        self.message = message
        self.headers = headers
