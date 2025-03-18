from smarthome import SmartHome

class SmartHomeInterface:
    def __init__(self, home: SmartHome)-> None:
        self.home = home

    def run(self)-> None:
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_or_remove_device()
            elif choice == '2':
                self.modify_device()
            elif choice == '3':
                self.add_or_remove_environment()
            elif choice == '4':
                self.add_or_remove_device_from_environment()
            elif choice == '5':
                self.list_devices()
            elif choice == '6':
                self.list_environments()
            elif choice == '7':
                self.toggle_device()
            elif choice == '8':
                self.search_and_display_device_attributes()
            elif choice == '0':
                print("Exiting...")
                break
            else:
                print("Invalid choice, try again.")

    def display_menu(self)-> None:
        print("\n--- Smart Home Menu ---")
        print("1. Add Device or Remove Device")
        print("2. Modify Device")
        print("3. Add Environment or Remove Environment")
        print("4. Add Device to Environment or Remove Device from Environment")
        print("5. List Devices")
        print("6. List Environments")
        print("7. Turn On/Off Device")
        print("8. Search and Display Device Attributes")
        print("0. Exit")

    def add_or_remove_device(self)-> None:
        print("\n--- Add or Remove Device ---")
        print("1. Add Device")
        print("2. Remove Device")
        choice = input("Choose an option: ")

        if choice == '1':
            # Add Device
            device_type = input("Enter device type (smartcamera, smartlight, smartthermostat, voiceassistant): ")
            device_id = input("Enter device ID: ")
            
            device = self.home.add_device(device_type, device_id)

            if device:
                print(f"{device_type} with ID {device_id} added successfully!")
            else:
                print("Failed to add device!")

        elif choice == '2':
            # Remove Device
            device_id = input("Enter device ID to remove: ")
            self.home.remove_device(device_id)
        else:
            print("Invalid choice!")


    def modify_device(self)-> None:
        print("\n--- Modify Device ---")
        
        # List existing devices first for user's reference
        self.list_devices()
        
        device_id = input("Enter the device ID of the device you want to modify: ")

        if not device_id.isdigit():
            print("Invalid device ID!")
            return

        # Call modify_device from the SmartHome class
        self.home.modify_device(device_id)

        print(f"Device with ID {device_id} modified successfully!")


    def add_or_remove_environment(self)-> None:
        print("\n--- Add or Remove Environment ---")
        
        # List existing environments for the user's reference
        self.list_environments()
        
        action = input("Would you like to (add) or (remove) an environment? ")

        if action == "add":
            environment_name = input("Enter the name of the new environment: ")
            self.home.add_or_update_environment(environment_name)

        elif action == "remove":
            environment_name = input("Enter the name of the environment to remove: ")
            self.home.remove_environment(environment_name)

        else:
            print("Invalid choice!")


    def add_or_remove_device_from_environment(self)-> None:
        print("\n--- Add or Remove Device from Environment ---")
        
        # List existing devices and environments for the user's reference
        print("\nAvailable Devices:")
        self.list_devices()
        print("\nAvailable Environments:")
        self.list_environments()
        
        action = input("Would you like to (add) or (remove) a device from an environment? ")

        if action == "add":
            device_id = input("Enter the ID of the device you want to add: ")
            environment_name = input("Enter the name of the environment where you want to add the device: ")
            self.home.add_device_to_environment(device_id, environment_name)

        elif action == "remove":
            device_id = input("Enter the ID of the device you want to remove: ")
            environment_name = input("Enter the name of the environment from which you want to remove the device: ")
            self.home.remove_device_from_environment(device_id, environment_name)

        else:
            print("Invalid choice!")

    def list_devices(self)-> None:
        print("\n--- List of All Devices ---")
        
        devices = self.home.list_all_devices()
        
        if not devices:
            print("No devices available in the smart home.")
            return

        for device in devices:
            device_type = device.__class__.__name__
            device_id = device._device_id
            device_status = device.status
            device_location = device.location
            details = device.get_details()
            
            # Formatting the details
            details_str = ", ".join([f"{key}: {value}" for key, value in details.items()])
            print(f"{device_type} (ID: {device_id}) - {details_str} Status : {device_status}, Is in : {device_location} ")

        print("\n")

    def list_environments(self)-> None:
        print("\n--- List of All Environments ---")
        
        environments = self.home.environments
        
        if not environments:
            print("No environments available in the smart home.")
            return

        for env_name, env in environments.items():
            if env._devices:
                device_count = {}
                for device in env._devices:
                    device_type = device.__class__.__name__
                    device_count[device_type] = device_count.get(device_type, 0) + 1

                devices_in_env = ", ".join([f"{k}: {v}" for k, v in device_count.items()])
                print(f"- {env_name} (Devices: {devices_in_env})")
            else:
                print(f"- {env_name} (No devices)")

        print("\n")


    def toggle_device(self)-> None:
        """
        Interface for the user to toggle the status of devices in the smart home.
        """
        # Display the grouping options to the user
        print("Choose how you want to group devices:")
        print("1. By Type")
        print("2. By Environment")
        print("3. Individually")
        
        group_choice = int(input("Enter your choice (1/2/3): "))

        # Determine the grouping criterion based on the user's choice
        if group_choice == 1:
            group_by = "type"
        elif group_choice == 2:
            group_by = "environment"
        elif group_choice == 3:
            group_by = "individual"
        else:
            print("Invalid choice. Please try again.")
            return

        # Ask the user for the desired action
        print("\nChoose an action:")
        print("1. Turn On")
        print("2. Turn Off")

        action_choice = int(input("Enter your choice (1/2): "))

        # Determine the action based on the user's choice
        if action_choice == 1:
            action = "on"
        elif action_choice == 2:
            action = "off"
        else:
            print("Invalid choice. Please try again.")
            return

        # Call the control_devices function to handle the action
        self.home.control_devices(group_by, action)


    def search_and_display_device_attributes(self)-> None:
        """
        Interface for the user to search and view the attributes of a device in the smart home.
        """
        # 1. Prompt the user to enter a search criterion
        search_criterion = input("Enter the device ID or other criteria to search: ")

        # 2. Search for the device in the smart home
        device = self.find_device_by_criterion(search_criterion)

        # 3. If found, display the device's attributes
        if device:
            print("\nDevice Attributes:")
            for attr, value in vars(device).items():
                if not attr.startswith("_"):  # Skip private/protected attributes
                    print(f"{attr}: {value}")
        # 4. If not found, inform the user
        else:
            print("Device not found!")
        
    def find_device_by_criterion(self, criterion: str):
        """
        Searches for a device in the smart home based on a given criterion (e.g., device ID).

        Args:
            criterion (str): The search criterion (usually device ID).

        Returns:
            SmartDevice or None: The device if found, otherwise None.
        """
        for device in self.home._devices:
            if device._device_id == criterion:
                return device
            for attr, value in vars(device).items():
                if str(value) == criterion:
                    return device
        return None

smarthome = SmartHome()
interface = SmartHomeInterface(smarthome)
interface.run()
