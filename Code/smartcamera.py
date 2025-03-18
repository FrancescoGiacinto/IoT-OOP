from smartdevice import SmartDevice
from typing import Dict

class SmartCamera(SmartDevice):
    def __init__(self, device_id, view_angle=120, recording_capacity=120, motion_detection=False, **kwargs):
        super().__init__(device_id, **kwargs)
        self.view_angle = view_angle
        self.original_capacity = recording_capacity  
        self.remaining_capacity = recording_capacity  
        self.is_recording = False  

    def start_recording(self)-> None:
        """Start recording."""
        if self.is_recording:
            print("Camera is already recording!")
        elif self.remaining_capacity <= 0:
            print("No recording capacity left!")
        else:
            self.is_recording = True
            print("Camera started recording.")

    def stop_recording(self)-> None:
        """Stop recording."""
        if not self.is_recording:
            print("Camera isn't recording!")
        else:
            self.is_recording = False
            self.remaining_capacity -= 1  
            print("Camera stopped recording.")
    
    def get_details(self) -> Dict:
        return {
            'View Angle': f"{self.view_angle}°",
            'Remaining Capacity': self.remaining_capacity
        }