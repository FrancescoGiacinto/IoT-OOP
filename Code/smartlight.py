from smartdevice import SmartDevice
from typing import Dict

class SmartLight(SmartDevice):
    def __init__(self, device_id, brightness=50, color="white", **kwargs):
        super().__init__(device_id, **kwargs)
        self.brightness: int = brightness
        self.color: str = color

    def adjust_brightness(self, new_brightness)-> None:
        """Adjust the light's brightness."""
        self.brightness = new_brightness

    def change_color(self, new_color)-> None:
        """Change the light's color."""
        self.color = new_color

    def get_details(self)-> Dict:
        return {
            'Color': self.color,
            'Brightness': f"{self.brightness}%"
        }