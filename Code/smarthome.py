from typing import Dict, List, Optional, Union
from environment import Environment
from smartcamera import SmartCamera
from smartlight import SmartLight
from smartthermostat import SmartThermostat
from voiceassistant import VoiceAssistant
from smartdevice import SmartDevice

class SmartHome:
    """
    A class to represent a smart home which can hold various smart devices and environments.
    """

    def __init__(self):
        self._devices: List[SmartDevice] = []
        self.environments: Dict[str, Environment] = {} 

    def add_device(self, device_type: str, device_id: str) -> Optional[Union[SmartCamera, SmartLight, SmartThermostat, VoiceAssistant]]:
        """
        Create and return a device instance based on its type.

        Parameters:
        - device_type (str): The type of device to create.
        - device_id (str): The unique identifier for the device.

        Returns:
        - device (Union[SmartCamera, SmartLight, SmartThermostat, VoiceAssistant]): The created device instance.
        """
        if device_id in self._devices:
            print(f"Error: Device with ID {device_id} already exists!")
            return
        
        if any(device._device_id == device_id for device in self._devices):
            print(f"Error: Device with ID {device_id} already exists!")
            return
        
        device = None

        if device_type == 'smartcamera':
            view_angle = int(input("Enter view angle for SmartCamera: "))
            device = SmartCamera(device_id=device_id, view_angle=view_angle)

        elif device_type == 'smartlight':
            brightness = int(input("Enter intensity for SmartLight: "))
            color = input("Enter color (if RGB) for SmartLight: ")
            device = SmartLight(device_id=device_id, brightness=brightness, color=color)

        elif device_type == 'smartthermostat':
            desired_temperature = int(input("Enter desired temperature for SmartThermostat: "))
            mode = input("Enter mode (cooling/heating) for SmartThermostat: ")
            device = SmartThermostat(device_id=device_id, desired_temp=desired_temperature, mode=mode)

        elif device_type == 'voiceassistant':
            volume = int(input("Enter volume for VoiceAssistant: "))
            language = input("Enter language for VoiceAssistant: ")
            device = VoiceAssistant(device_id=device_id, volume=volume, language=language)

        else:
            print(f"Unknown device type: {device_type}")
            return

        self._devices.append(device)
        print(f"{device_type} with ID {device_id} added.")
        return device

    def remove_device(self, device_id: str) -> None:
        """
        Remove a device from the smart home based on device_id.

        Parameters:
        - device_id (str): The unique identifier for the device to be removed.
        """
        self.list_all_devices()
        device = self._devices.get(device_id)

        if not device:
            print("Device with given ID not found!")
            return

        self._devices.pop(device_id)

        device = next((d for d in self._devices if d._device_id == device_id), None)

        if not device:
            print("Device with given ID not found!")            
            return

        self._devices.remove(device)

        for env in self.environments.values():
            if device in env._devices:
                env.remove_device(device)

        print(f"Device with ID {device_id} removed from smart home and all environments it was present in.")

    def modify_device(self, device_id: str) -> None:
        """
        Modifies the attributes of a device based on its type (SmartLight, SmartThermostat, SmartCamera, VoiceAssistant).

        Args:
            device_id (int): The ID of the device to be modified.

        Returns:
            None: The function modifies the device attributes in place and does not return a value.
        """
        device = next((d for d in self._devices if d._device_id == device_id), None)
        if not device:
            print("Device not found!")
            return

        if isinstance(device, SmartLight):
            new_brightness = input("Enter new brightness (0-100): ")
            if new_brightness.isdigit():
                device.brightness = int(new_brightness)
            new_color = input("Enter new color: ")
            device.color = new_color

        elif isinstance(device, SmartThermostat):
            new_current_temp = input("Enter current temperature: ")
            if new_current_temp.isdigit():
                device.current_temp = int(new_current_temp)
            new_desired_temp = input("Enter new desired temperature: ")
            if new_desired_temp.isdigit():
                device.desired_temp = int(new_desired_temp)
            new_mode = input("Enter new mode (cooling/heating): ")
            device.mode = new_mode

        elif isinstance(device, SmartCamera):
            new_view_angle = input("Enter new view angle: ")
            if new_view_angle.isdigit():
                device.view_angle = int(new_view_angle)
            new_capacity = input("Enter new recording capacity: ")
            if new_capacity.isdigit():
                device.original_capacity = int(new_capacity)
                device.remaining_capacity = int(new_capacity)
            motion_detection = input("Enable motion detection? (yes/no): ")
            device.motion_detection = motion_detection.lower() == "yes"

        elif isinstance(device, VoiceAssistant):
            new_volume = input("Enter new volume (0-100): ")
            if new_volume.isdigit():
                device.volume = int(new_volume)
            new_language = input("Enter new language: ")
            device.language = new_language

        print("Device attributes updated!")

    def add_or_update_environment(self, environment_name: str, environment: Environment = None) -> None:
        """Adds or updates an environment instance to the smart home."""
        
        if environment_name in self.environments:
            if environment:
                # Update the existing environment with the new one
                self.environments[environment_name] = environment
                print(f"Environment '{environment_name}' updated in the smart home.")
            else:
                print(f"{environment_name} already exists in the smart home.")
            return

        if environment:
            self.environments[environment_name] = environment
        else:
            # Create a new Environment instance if none is provided
            self.environments[environment_name] = Environment(environment_name) 

        print(f"Environment '{environment_name}' added to the smart home.")

    def remove_environment(self, environment_name)-> None:
        """Remove an environment from the smart home."""
        if environment_name in self.environments:
            del self.environments[environment_name]
            print(f"Environment '{environment_name}' removed from the smart home.")
        else:
            print(f"{environment_name} doesn't exist in the smart home.")

    def add_device_to_environment(self, device_id: str, environment_name: str) -> None:
        """Add a device to a specific environment."""
        if environment_name not in self.environments:
            print(f"The environment '{environment_name}' doesn't exist.")
            return
        
        device = next((d for d in self._devices if d._device_id == device_id), None)
        if not device:
            print(f"No device with ID '{device_id}' found.")
            return

        env = self.environments[environment_name]
        if device in env._devices:
            print(f"Device with ID '{device_id}' is already in the '{environment_name}' environment.")
            return

        env.add_device(device)
        device.location = environment_name
        print(f"Device with ID '{device_id}' added to '{environment_name}' environment.")


    def remove_device_from_environment(self, device_id: str, environment_name: str) -> None:
        """
        Remove a device from a specific environment.

        Parameters:
        - device_id (str): The unique identifier for the device.
        - environment_name (str): The name of the environment from which to remove the device.
        """
        # Ensure the environment exists
        if environment_name not in self.environments:
            print(f"The environment '{environment_name}' doesn't exist.")
            return

        env = self.environments[environment_name]
        
        # Find the device based on device_id
        device = next((d for d in self._devices if d._device_id == device_id), None)
        if not device:
            print(f"No device with ID '{device_id}' found.")
            return

        # Check if the device is in the specified environment
        if device not in env._devices:
            print(f"Device with ID '{device_id}' is not in the '{environment_name}' environment.")
            return
        
        # Remove the device from the environment
        env.remove_device(device)
        device.location = "unknown"
        print(f"Device with ID '{device_id}' removed from '{environment_name}' environment.")

    def control_devices(self, group_by: str, action: str)-> None:
        """
        Control the devices based on their grouping and desired action.

        Parameters:
        - group_by (str): The criterion to group devices ('type', 'environment', or 'individual').
        - action (str): The action to perform on devices ('on' or 'off').
        """
        if group_by == "type":
            # Group devices by type
            device_types = {}
            for device in self._devices:
                device_type = device.__class__.__name__
                if device_type not in device_types:
                    device_types[device_type] = [device]
                else:
                    device_types[device_type].append(device)

            for dtype, devices in device_types.items():
                print(f"\nTurning {action} all {dtype}s...")
                for device in devices:
                    if action == "on":
                        device.turn_on()
                    elif action == "off":
                        device.turn_off()

        elif group_by == "environment":
            # Group devices by environment
            for env_name, env in self.environments.items():
                print(f"\nTurning {action} all devices in {env_name}...")
                for device in env._devices:
                    if action == "on":
                        device.turn_on()
                    elif action == "off":
                        device.turn_off()

        elif group_by == "individual":
            # List individual devices and choose which to control
            for index, device in enumerate(self._devices, 1):
                device_name = device.__class__.__name__ + " - " + device._device_id
                print(f"{index}. {device_name}")

            choice = int(input(f"\nSelect a device (1-{len(self._devices)}) to turn {action}: "))
            if 0 < choice <= len(self._devices):
                selected_device = self._devices[choice - 1]
                if action == "on":
                    selected_device.turn_on()
                elif action == "off":
                    selected_device.turn_off()
                print(f"\n{selected_device.__class__.__name__} with ID {selected_device._device_id} turned {action}.")
            else:
                print("Invalid selection.")
        else:
            print("Invalid grouping criteria.")



    def list_devices_in_environment(self, environment_name)-> List:
        """List all devices in a specified environment and return the list."""
        if environment_name not in self.environments:
            print(f"{environment_name} doesn't exist in the smart home.")
            return []
        env = self.environments[environment_name]
        return env.list_devices()


    def list_all_devices(self)-> List:
        return self._devices

    

    def list_environments(self) -> List[str]:
        """
        List all environments in the smart home and display the count of each device type within them.

        This method prints the names of all environments along with a breakdown of device types within each environment.
        It returns a list of environment names.

        Returns:
            List[str]: A list of names of all environments in the smart home.
        """
        if not self.environments:
            print("No environments in the smart home.")
            return []

        print("Environments in the smart home:")
        for env_name, env in self.environments.items():
            device_count: Dict[str, int] = {}

            for device in env._devices:
                device_type = device.__class__.__name__
                device_count[device_type] = device_count.get(device_type, 0) + 1

            device_count_str = ", ".join([f"{key}: {value}" for key, value in device_count.items()])
            print(f"  - {env_name} ({device_count_str})")

        return list(self.environments.keys())

    
        
"""    def get_environment(self, environment_name):
        #Retrieve an environment instance by name.
        return self.environments.get(environment_name)"""
