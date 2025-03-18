from typing import List
from smartdevice import SmartDevice

class Environment:
    def __init__(self, name)-> None:
        self.name = name  
        self._devices: List[SmartDevice] = []

    def add_device(self, device) -> None:
        """Add a device to the environment."""
        if device not in self._devices:
            self._devices.append(device)
            device.location = self.name  
            print(f"{device.__class__.__name__} added to {self.name}.")
        else:
            print(f"{device.__class__.__name__} is already in {self.name}.")

    def remove_device(self, device) -> None:
        """Remove a device from the environment."""
        if device in self._devices:
            self._devices.remove(device)
            device.location = "unknown" 
            print(f"{device.__class__.__name__} removed from {self.name}.")
        else:
            print(f"{device.__class__.__name__} was not found in {self.name}.")

    def list_devices(self)-> List:
        """List all devices in the environment and return their IDs."""
        if not self._devices:
            print(f"No devices in {self.name}.")
            return []
        print(f"Devices in {self.name}:")
        device_ids = []
        for device in self._devices:
            print(f"  - {device.__class__.__name__} (ID: {device._device_id})")
            device_ids.append(device._device_id)
        return device_ids


