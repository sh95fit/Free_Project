import asyncio
from bleak import BleakScanner, BleakClient


async def scan_for_devices():
    print("Scanning for devices...")
    devices = await BleakScanner.discover()
    for device in devices:
        print(f"Device: {device.name}, Address: {device.address}")
        print(f"RSSI (신호감도) : {device.rssi}")
        if device.metadata:
            print("Metadata:")
            for key, value in device.metadata.items():
                print(f"  {key}: {value}")
        if device.details:
            print(f"Device Detail:")
            adv_data = decode_adv_data(device)
            for key, value in adv_data.items():
                print(f"  {key}: {value}")


def decode_adv_data(raw_data):
    # 여기에 raw_data를 해석하는 코드를 추가하세요.
    adv_data = {}
    adv_data['local_name'] = raw_data.local_name if hasattr(
        raw_data, 'local_name') else None
    adv_data['manufacturer_data'] = raw_data.manufacturer_data if hasattr(
        raw_data, 'manufacturer_data') else None
    adv_data['service_data'] = raw_data.service_data if hasattr(
        raw_data, 'service_data') else None
    adv_data['service_uuids'] = raw_data.service_uuids if hasattr(
        raw_data, 'service_uuids') else None
    return adv_data


async def get_device_services(address):
    async with BleakClient(address) as client:
        print(f"Connected: {client.is_connected}")
        services = await client.get_services()
        for service in services:
            print(f"Service UUID: {service.uuid}")
            for characteristic in service.characteristics:
                print(f"  Characteristic UUID: {characteristic.uuid}")


if __name__ == "__main__":
    asyncio.run(scan_for_devices())
    # asyncio.run(get_device_services("[MAC Address]"))
