from abc import ABC, abstractmethod

class SmartDevice(ABC):
    def __init__(self, device_id, status="off", location="unknown"):
        self._device_id = device_id 
        self._status = status 
        self.location = location

    @property
    def status(self):
        """Get the device's status."""
        return self._status

    @property
    def device_id(self) -> str:
        """Get the device ID."""
        return self._device_id

    @abstractmethod
    def get_details(self) -> dict:
        """Retrieve details of the device. Must be implemented by subclasses."""
        pass

    def turn_on(self):
        """Turn the device on."""
        self._status = "on"

    def turn_off(self):
        """Turn the device off."""
        self._status = "off"

