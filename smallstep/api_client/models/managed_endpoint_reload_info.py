from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.managed_endpoint_reload_info_method import ManagedEndpointReloadInfoMethod
from ..types import UNSET, Unset

T = TypeVar("T", bound="ManagedEndpointReloadInfo")


@_attrs_define
class ManagedEndpointReloadInfo:
    """The properties used to reload a service.

    Example:
        {'method': 'SIGNAL', 'pidFile': '/var/run/db.pid', 'signal': 1}

    Attributes:
        method (ManagedEndpointReloadInfoMethod): Ways an endpoint can reload a certificate. `AUTOMATIC` means the
            process is able to detect and reload new certificates automatically. `CUSTOM` means a custom command must be run
            to trigger the workload to reload the certificates. `SIGNAL` will configure the agent to send a signal to the
            process in `pidFile`. `DBUS` will use the systemd system bus to issue a `try-reload-or-restart` job for unit
            specified by `unitName`.
        pid_file (Union[Unset, str]): File that holds the pid of the process to signal. Required when method is SIGNAL.
        signal (Union[Unset, int]): The signal to send to a process when a certificate should be reloaded. Required when
            method is SIGNAL.
        unit_name (Union[Unset, str]): The systemd unit name to reload when a certificate should be reloaded. Required
            when method is DBUS.
    """

    method: ManagedEndpointReloadInfoMethod
    pid_file: Union[Unset, str] = UNSET
    signal: Union[Unset, int] = UNSET
    unit_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        method = self.method.value

        pid_file = self.pid_file
        signal = self.signal
        unit_name = self.unit_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
            }
        )
        if pid_file is not UNSET:
            field_dict["pidFile"] = pid_file
        if signal is not UNSET:
            field_dict["signal"] = signal
        if unit_name is not UNSET:
            field_dict["unitName"] = unit_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        method = ManagedEndpointReloadInfoMethod(d.pop("method"))

        pid_file = d.pop("pidFile", UNSET)

        signal = d.pop("signal", UNSET)

        unit_name = d.pop("unitName", UNSET)

        managed_endpoint_reload_info = cls(
            method=method,
            pid_file=pid_file,
            signal=signal,
            unit_name=unit_name,
        )

        managed_endpoint_reload_info.additional_properties = d
        return managed_endpoint_reload_info

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
