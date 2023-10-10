# SPDX-License-Identifier: Apache-2.0
#
# Copyright (c) 2023 Smallstep Labs, Inc <techadmin@smallstep.com> All Rights Reserved.
# Apache-2.0 (see LICENSE or https://opensource.org/license/apache-2-0/)

import datetime
import json
from typing import Any, Callable, List, TypeVar

from .api_client.api.authorities import get_authorities
from .api_client.api.collections import (
    delete_collection,
    delete_collection_instance,
    get_collection,
    get_collection_instance,
    get_collection_instance_data,
    list_collection_instances,
    list_collections,
    post_collections,
    put_collection,
    put_collection_instance,
    put_collection_instance_data,
)
from .api_client.api.managed_workloads import (
    delete_device_collection,
    delete_workload,
    get_device_collection,
    get_workload,
    post_device_enrollment_token,
    put_device_collection,
    put_workload,
)
from .api_client.errors import UnexpectedStatus
from .api_client.models import (
    Authority,
    AWSVMDeviceType,
    AzureVMDeviceType,
    Collection,
    CollectionInstance,
    DeviceCollection,
    DeviceCollectionDeviceType,
    GCPVMDeviceType,
    ManagedEndpointCertificateInfo,
    ManagedEndpointCertificateInfoType,
    ManagedEndpointHook,
    ManagedEndpointHooks,
    ManagedEndpointKeyInfo,
    ManagedEndpointKeyInfoFormat,
    ManagedEndpointKeyInfoType,
    ManagedEndpointReloadInfo,
    ManagedEndpointReloadInfoMethod,
    NewCollection,
    NewDeviceEnrollmentToken,
    PutCollectionInstanceJsonBody,
    TPMDeviceType,
    Workload,
)
from .api_client.types import Response
from .client import StepClient
from .exceptions import StepException

T = TypeVar("T")


class BaseClass:
    def __init__(self, smallstep_api_host: str = None, smallstep_api_token: str = None):
        self.client = StepClient(smallstep_api_host, smallstep_api_token)

    def _make_request(self, func: Callable, *args, **kwargs) -> Response[T]:
        with self.client as self.client:
            try:
                res = func.sync_detailed(client=self.client, *args, **kwargs)
            except UnexpectedStatus as e:
                raise StepException(
                    status_code=e.status_code,
                    message=e.content,
                    headers=None,
                )
            except:
                raise

            if res.status_code >= 400:
                if res.headers["content-type"] == "application/json; charset=utf-8":
                    raise StepException(
                        status_code=res.status_code,
                        message=json.loads(res.content.decode("utf-8")),
                        headers=res.headers,
                    )
                else:
                    raise StepException(
                        status_code=res.status_code,
                        message=res.content.decode("utf-8").strip(),
                        headers=res.headers,
                    )

            return res.parsed


class StepAuthority(BaseClass):
    def __init__(self, smallstep_api_host: str = None, smallstep_api_token: str = None):
        super().__init__(
            smallstep_api_host=smallstep_api_host,
            smallstep_api_token=smallstep_api_token,
        )

    def get_all(self) -> List[Authority]:
        return self._make_request(func=get_authorities)

    def create(self):
        """Not implemented."""
        pass

    def destroy(self):
        """Not implemented."""
        pass


class StepCollection(BaseClass):
    def __init__(self, smallstep_api_host: str = None, smallstep_api_token: str = None):
        super().__init__(
            smallstep_api_host=smallstep_api_host,
            smallstep_api_token=smallstep_api_token,
        )

    def get_all(self) -> List[Collection]:
        return self._make_request(func=list_collections)

    def get(self, collection_slug: str) -> Collection:
        return self._make_request(func=get_collection, collection_slug=collection_slug)

    def update(self, collection_slug: str, collection_name: str, collection_data: dict) -> Collection:
        data = {
            "created_at": datetime.datetime.fromisoformat(collection_data["createdAt"]),
            "display_name": collection_name,
            "instance_count": 5,
            "slug": collection_slug,
            "updated_at": datetime.datetime.now(tz=datetime.timezone.utc),
        }
        json_body = Collection(**data)

        return self._make_request(func=put_collection, collection_slug=collection_slug, json_body=json_body)

    def create(self, collection_slug: str, collection_name: str) -> Collection:
        json_body = NewCollection(
            slug=collection_slug,
            display_name=collection_name,
        )
        return self._make_request(func=post_collections, json_body=json_body)

    def destroy(self, collection_slug: str) -> Response[Any]:
        return self._make_request(func=delete_collection, collection_slug=collection_slug)

    def create_instance(
        self,
        collection_slug: str,
        instance_id: str,
        instance_metadata: PutCollectionInstanceJsonBody,
    ) -> CollectionInstance:
        json_body = PutCollectionInstanceJsonBody(data=instance_metadata)
        return self._make_request(
            func=put_collection_instance,
            collection_slug=collection_slug,
            instance_id=instance_id,
            json_body=json_body,
        )

    def get_instance(self, collection_slug: str, instance_id: str) -> Collection:
        return self._make_request(
            func=get_collection_instance,
            collection_slug=collection_slug,
            instance_id=instance_id,
        )

    def get_instance_data(self, collection_slug: str, instance_id: str) -> Collection:
        return self._make_request(
            func=get_collection_instance_data,
            collection_slug=collection_slug,
            instance_id=instance_id,
        )

    def update_instance(self, collection_slug: str, instance_id: str, instance_metadata: dict) -> CollectionInstance:
        return self._make_request(
            func=put_collection_instance_data,
            collection_slug=collection_slug,
            instance_id=instance_id,
            json_body=instance_metadata,
        )

    def list_instances(self, collection_slug: str) -> List[CollectionInstance]:
        return self._make_request(func=list_collection_instances, collection_slug=collection_slug)

    def destroy_instance(self, collection_slug: str, instance_id: str) -> Response[Any]:
        return self._make_request(
            func=delete_collection_instance,
            collection_slug=collection_slug,
            instance_id=instance_id,
        )


class StepDeviceCollection(BaseClass):
    def __init__(self, smallstep_api_host: str = None, smallstep_api_token: str = None):
        super().__init__(
            smallstep_api_host=smallstep_api_host,
            smallstep_api_token=smallstep_api_token,
        )

    def get(self, collection_slug: str) -> DeviceCollection:
        return self._make_request(func=get_device_collection, collection_slug=collection_slug)

    def create(
        self,
        admin_emails: List[str],
        collection_slug: str,
        collection_name: str,
        device_type: str,
        **kwargs,
    ) -> DeviceCollection:
        device_type = DeviceCollectionDeviceType(device_type)

        if device_type == DeviceCollectionDeviceType.AWS_VM:
            device_type_configuration = AWSVMDeviceType(**kwargs)
        elif device_type == DeviceCollectionDeviceType.GCP_VM:
            device_type_configuration = GCPVMDeviceType(**kwargs)
        elif device_type == DeviceCollectionDeviceType.AZURE_VM:
            device_type_configuration = AzureVMDeviceType(**kwargs)
        elif device_type == DeviceCollectionDeviceType.TPM:
            device_type_configuration = TPMDeviceType(**kwargs)

        new_collection = DeviceCollection(
            admin_emails=admin_emails,
            device_type_configuration=device_type_configuration,
            device_type=device_type,
            display_name=collection_name,
            slug=collection_slug,
        )

        return self._make_request(
            func=put_device_collection,
            collection_slug=collection_slug,
            json_body=new_collection,
        )

    update = create

    def destroy(self, collection_slug: str, collection_purge: bool) -> Response[Any]:
        return self._make_request(
            func=delete_device_collection,
            collection_slug=collection_slug,
            purge=collection_purge,
        )

    def generate_instance_enrollment_token(self, collection_slug: str, instance_id: str) -> NewDeviceEnrollmentToken:
        instance_title = f"Enrollment token for {instance_id}"
        json_body = NewDeviceEnrollmentToken(title=instance_title)
        return self._make_request(
            func=post_device_enrollment_token,
            collection_slug=collection_slug,
            instance_id=instance_id,
            json_body=json_body,
        )


class StepWorkload(BaseClass):
    def __init__(self, smallstep_api_host: str = None, smallstep_api_token: str = None):
        super().__init__(
            smallstep_api_host=smallstep_api_host,
            smallstep_api_token=smallstep_api_token,
        )

    def create(
        self, collection_slug: str, display_name: str, workload_slug: str, workload_type: str, **kwargs
    ) -> Workload:
        optparams = {}

        if kwargs.get("admin_emails") is not None:
            optparams["admin_emails"] = kwargs.get("admin_emails")

        if kwargs.get("certificate_info") is not None:
            cert_info = kwargs.get("certificate_info")
            cert_info["type"] = ManagedEndpointCertificateInfoType(cert_info["type"])
            optparams["certificate_info"] = ManagedEndpointCertificateInfo(**kwargs.get("certificate_info"))

        if kwargs.get("device_metadata_key_sans") is not None:
            optparams["device_metadata_key_sans"] = kwargs.get("device_metadata_key_sans")

        if kwargs.get("hooks") is not None:
            hook = {k: ManagedEndpointHook(*list(v.values())) for k, v in kwargs.get("hooks").items() if v is not None}
            optparams["hooks"] = ManagedEndpointHooks(**hook)

        if kwargs.get("key_info") is not None:
            key_info = kwargs.get("key_info")
            if key_info.get("format") is not None:
                key_info["format_"] = key_info.pop("format")
            key_info["type"] = ManagedEndpointKeyInfoType(key_info["type"])
            key_info["format_"] = ManagedEndpointKeyInfoFormat(key_info["format_"])
            optparams["key_info"] = ManagedEndpointKeyInfo(**key_info)

        if kwargs.get("reload_info") is not None:
            reload_info = kwargs.get("reload_info")
            reload_info["method"] = ManagedEndpointReloadInfoMethod(reload_info["method"])
            optparams["reload_info"] = ManagedEndpointReloadInfo(**kwargs.get("reload_info"))
        if kwargs.get("static_sans") is not None:
            optparams["static_sans"] = kwargs.get("static_sans")

        workload = Workload(display_name=display_name, slug=workload_slug, workload_type=workload_type, **optparams)
        return self._make_request(
            func=put_workload,
            collection_slug=collection_slug,
            workload_slug=workload_slug,
            json_body=workload,
        )

    update = create

    def get(self, workload_slug: str, collection_slug: str) -> Workload:
        return self._make_request(func=get_workload, collection_slug=collection_slug, workload_slug=workload_slug)

    def destroy(self, collection_slug: str, workload_slug: str) -> Response[Any]:
        return self._make_request(func=delete_workload, collection_slug=collection_slug, workload_slug=workload_slug)
