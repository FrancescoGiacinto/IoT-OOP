from smarthome import SmartHome, SmartCamera, SmartLight, SmartThermostat, VoiceAssistant

def main():
    # Create an instance of SmartHome
    home = SmartHome()

    # Add devices to the home
    home.add_device(device_type="smartcamera", device_id="cam1")
    home.add_device(device_type="smartlight", device_id="light1")
    home.add_device(device_type="smartthermostat", device_id="thermo1")
    home.add_device(device_type="voiceassistant", device_id="va1")

    # List devices
    print("\n--- All Devices in SmartHome ---")
    devices = home.list_all_devices()
    for device in devices:
        print(f"Device ID: {device._device_id}, Type: {type(device).__name__}")

    # Attempt to add a duplicate device
    print("\n--- Adding Duplicate Device ---")
    home.add_device(device_type="smartlight", device_id="light1")

    # Change device properties
    # (Assuming each device class has methods to set their properties)
    light1 = next(device for device in devices if device._device_id == "light1")
    if isinstance(light1, SmartLight):
        light1.brightness = 70
        light1.color = "red"
        print(f"\nUpdated Light Details: Brightness = {light1.brightness}, Color = {light1.color}")

    # This is just a basic script to demonstrate the use of instances. I can expand on it or modify 
    # based on the methods and functionalities available in your classes.

if __name__ == "__main__":
    main()
