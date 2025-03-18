from smartdevice import SmartDevice

class SmartThermostat(SmartDevice):
    def __init__(self, device_id, current_temp=20, desired_temp=22, mode="cooling", **kwargs):
        super().__init__(device_id, **kwargs)
        self.current_temp = current_temp
        self.desired_temp = desired_temp
        self.mode = mode

    def set_temperature(self, temp):
        """Set the thermostat's temperature."""
        self.desired_temp = temp


    def display_attributes(self):
        """Display attributes specific to SmartThermostat."""
        return f"Desired Temperature: {self.desired_temp},Current temperature: {self.current_temp}, Mode: {self.mode}"

    def get_details(self):
        return {
            'Desired Temperature': f"{self.desired_temp}°C",
            'Mode': self.mode
        }