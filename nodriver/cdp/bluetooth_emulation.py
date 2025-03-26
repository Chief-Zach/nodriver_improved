# DO NOT EDIT THIS FILE!
#
# This file is generated from the CDP specification. If you need to make
# changes, edit the generator and regenerate all of the modules.
#
# CDP domain: BluetoothEmulation (experimental)

from __future__ import annotations
import enum
import typing
from dataclasses import dataclass
from .util import event_class, T_JSON_DICT


class CentralState(enum.Enum):
    '''
    Indicates the various states of Central.
    '''
    ABSENT = "absent"
    POWERED_OFF = "powered-off"
    POWERED_ON = "powered-on"

    def to_json(self) -> str:
        return self.value

    @classmethod
    def from_json(cls, json: str) -> CentralState:
        return cls(json)


@dataclass
class ManufacturerData:
    '''
    Stores the manufacturer data
    '''
    #: Company identifier
    #: https://bitbucket.org/bluetooth-SIG/public/src/main/assigned_numbers/company_identifiers/company_identifiers.yaml
    #: https://usb.org/developers
    key: int

    #: Manufacturer-specific data (Encoded as a base64 string when passed over JSON)
    data: str

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['key'] = self.key
        json['data'] = self.data
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> ManufacturerData:
        return cls(
            key=int(json['key']),
            data=str(json['data']),
        )


@dataclass
class ScanRecord:
    '''
    Stores the byte data of the advertisement packet sent by a Bluetooth device.
    '''
    name: typing.Optional[str] = None

    uuids: typing.Optional[typing.List[str]] = None

    #: Stores the external appearance description of the device.
    appearance: typing.Optional[int] = None

    #: Stores the transmission power of a broadcasting device.
    tx_power: typing.Optional[int] = None

    #: Key is the company identifier and the value is an array of bytes of
    #: manufacturer specific data.
    manufacturer_data: typing.Optional[typing.List[ManufacturerData]] = None

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        if self.name is not None:
            json['name'] = self.name
        if self.uuids is not None:
            json['uuids'] = [i for i in self.uuids]
        if self.appearance is not None:
            json['appearance'] = self.appearance
        if self.tx_power is not None:
            json['txPower'] = self.tx_power
        if self.manufacturer_data is not None:
            json['manufacturerData'] = [i.to_json() for i in self.manufacturer_data]
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> ScanRecord:
        return cls(
            name=str(json['name']) if json.get('name', None) is not None else None,
            uuids=[str(i) for i in json['uuids']] if json.get('uuids', None) is not None else None,
            appearance=int(json['appearance']) if json.get('appearance', None) is not None else None,
            tx_power=int(json['txPower']) if json.get('txPower', None) is not None else None,
            manufacturer_data=[ManufacturerData.from_json(i) for i in json['manufacturerData']] if json.get('manufacturerData', None) is not None else None,
        )


@dataclass
class ScanEntry:
    '''
    Stores the advertisement packet information that is sent by a Bluetooth device.
    '''
    device_address: str

    rssi: int

    scan_record: ScanRecord

    def to_json(self) -> T_JSON_DICT:
        json: T_JSON_DICT = dict()
        json['deviceAddress'] = self.device_address
        json['rssi'] = self.rssi
        json['scanRecord'] = self.scan_record.to_json()
        return json

    @classmethod
    def from_json(cls, json: T_JSON_DICT) -> ScanEntry:
        return cls(
            device_address=str(json['deviceAddress']),
            rssi=int(json['rssi']),
            scan_record=ScanRecord.from_json(json['scanRecord']),
        )


def enable(
        state: CentralState,
        le_supported: bool
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Enable the BluetoothEmulation domain.

    :param state: State of the simulated central.
    :param le_supported: If the simulated central supports low-energy.
    '''
    params: T_JSON_DICT = dict()
    params['state'] = state.to_json()
    params['leSupported'] = le_supported
    cmd_dict: T_JSON_DICT = {
        'method': 'BluetoothEmulation.enable',
        'params': params,
    }
    json = yield cmd_dict


def set_simulated_central_state(
        state: CentralState
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Set the state of the simulated central.

    :param state: State of the simulated central.
    '''
    params: T_JSON_DICT = dict()
    params['state'] = state.to_json()
    cmd_dict: T_JSON_DICT = {
        'method': 'BluetoothEmulation.setSimulatedCentralState',
        'params': params,
    }
    json = yield cmd_dict


def disable() -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Disable the BluetoothEmulation domain.
    '''
    cmd_dict: T_JSON_DICT = {
        'method': 'BluetoothEmulation.disable',
    }
    json = yield cmd_dict


def simulate_preconnected_peripheral(
        address: str,
        name: str,
        manufacturer_data: typing.List[ManufacturerData],
        known_service_uuids: typing.List[str]
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Simulates a peripheral with ``address``, ``name`` and ``knownServiceUuids``
    that has already been connected to the system.

    :param address:
    :param name:
    :param manufacturer_data:
    :param known_service_uuids:
    '''
    params: T_JSON_DICT = dict()
    params['address'] = address
    params['name'] = name
    params['manufacturerData'] = [i.to_json() for i in manufacturer_data]
    params['knownServiceUuids'] = [i for i in known_service_uuids]
    cmd_dict: T_JSON_DICT = {
        'method': 'BluetoothEmulation.simulatePreconnectedPeripheral',
        'params': params,
    }
    json = yield cmd_dict


def simulate_advertisement(
        entry: ScanEntry
    ) -> typing.Generator[T_JSON_DICT,T_JSON_DICT,None]:
    '''
    Simulates an advertisement packet described in ``entry`` being received by
    the central.

    :param entry:
    '''
    params: T_JSON_DICT = dict()
    params['entry'] = entry.to_json()
    cmd_dict: T_JSON_DICT = {
        'method': 'BluetoothEmulation.simulateAdvertisement',
        'params': params,
    }
    json = yield cmd_dict
