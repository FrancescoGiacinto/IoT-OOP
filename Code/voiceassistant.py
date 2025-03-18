from smartdevice import SmartDevice

class VoiceAssistant(SmartDevice):
    def __init__(self, device_id, volume=50, language="English", **kwargs):
        super().__init__(device_id, **kwargs)
        self.volume:int = volume
        self.language: str = language
        self.commands_received: list = []

    def listen(self) -> None:
        """Listen for voice commands and save them."""
        while True:
            command = input("Listening... (say 'stop' to quit): ").strip()

            if command.lower() == "stop":
                print("Stopping the voice assistant...")
                break
            else:
                self.commands_received.append(command)
                print(f"Command '{command}' saved.")

    def get_details(self):
        return {
            'Volume': f"{self.volume}%",
            'Language': self.language
        }

    def display_saved_commands(self)-> None:
        """Display the list of saved voice commands."""
        if not self.commands_received:
            print("No voice commands received yet.")
            return

        print("Received voice commands:")
        for idx, command in enumerate(self.commands_received, 1):
            print(f"{idx}. {command}")