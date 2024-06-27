#!/usr/bin/env bash
# SPDX-License-Identifier: Apache-2.0
#
# Copyright (c) 2023 Smallstep Labs, Inc <techadmin@smallstep.com> All Rights Reserved.

set -x

TEMPDIR=$(mktemp -d)
: ${SMALLSTEP_API_URL:="https://gateway.smallstep.com/openapi.json"}

# Update the smallstep-python client libs from smallstep/openapi.json
openapi-python-client generate --config scripts/openapi-python-client.yml --url ${SMALLSTEP_API_URL} --output-path=${TEMPDIR} --overwrite
rm -rf smallstep/api_client

# Do us a find and replace to fix CamelCase issues
rg disable_custom_sa_ns --files-with-matches ${TEMPDIR} | xargs sed -i 's/disable_custom_sa_ns/disable_custom_sans/g'
rg project_i_ds --files-with-matches ${TEMPDIR} | xargs sed -i 's/project_i_ds/project_ids/g'
mv ${TEMPDIR}/api_client smallstep/
