#!/usr/bin/env bash
# SPDX-License-Identifier: Apache-2.0
#
# Copyright (c) 2023 Smallstep Labs, Inc <techadmin@smallstep.com> All Rights Reserved.

set -e

: ${SMALLSTEP_API_URL:="https://gateway.smallstep.com/openapi.json"}

# Update smallstep/openapi.json from URL and update the version to 3.0.2
curl -sL ${SMALLSTEP_API_URL} |jq '.openapi = "3.0.2"'|sponge smallstep/openapi.json

# Update the smallstep-python client libs from smallstep/openapi.json
openapi-python-client update --config scripts/openapi-python-client.yml --path smallstep/openapi.json

# Do us a find and replace to fix CamelCase issues
rg disable_custom_sa_ns --files-with-matches smallstep/ | xargs sed -i 's/disable_custom_sa_ns/disable_custom_sans/g'
rg project_i_ds --files-with-matches smallstep/ | xargs sed -i 's/project_i_ds/project_ids/g'
rg static_sa_ns --files-with-matches smallstep/ | xargs sed -i 's/static_sa_ns/static_sans/g'
rg device_metadata_key_sa_ns --files-with-matches smallstep/ | xargs sed -i 's/device_metadata_key_sa_ns/device_metadata_key_sans/g'
