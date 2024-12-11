import math
import json

class Camera:
    def __init__(self,config_path = "./configs/camera.configs.json"):
        """ 
        Initialize the camera configuration

        Args:
            config_path (str): The path to the camera configuration file (default: "../configs/camera.configs.json")
        """
        self.camera_config_path = config_path;
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)

        self.id = config.get('id', 0)
        self.width = config.get('width', 640)
        self.height = config.get('height', 480)
        self.horizontal_mount_offset = config.get('horizontal_mount_offset', 0)
        self.vertical_mount_offset = config.get('vertical_mount_offset', 0)
        self.focal_length = config.get('focal_length', 1) 
        self.fps = config.get('fps', 6)
        self.horizontal_FOV = config.get('horizontal_FOV', self.calculate_horizontal_fov())
        self.vertical_FOV = config.get('vertical_FOV', self.calculate_vertical_fov())

    
    def __str__(self):
        return f"Camera(id={self.id}, width={self.width}, height={self.height}, horizontal_mount_offset={self.horizontal_mount_offset}, vertical_mount_offset={self.vertical_mount_offset}, focal_length={self.focal_length}, fps={self.fps}, horizontal_FOV={self.horizontal_FOV}, vertical_FOV={self.vertical_FOV})"
    
    def config(self) -> dict:
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "horizontal_mount_offset": self.horizontal_mount_offset,
            "vertical_mount_offset": self.vertical_mount_offset,
            "focal_length": self.focal_length,
            "fps": self.fps,
            "horizontal_FOV": self.horizontal_FOV,
            "vertical_FOV": self.vertical_FOV
        }
        
    def calculate_horizontal_fov(self) -> float:
        """ 
        Calculate the horizontal field of view of the camera 

        return the horizontal field of view in degrees
        """
        rad = 2 * math.atan(self.width / 2 * self.focal_length) # in radians
        return math.degrees(rad) # in degrees
    
    def calculate_vertical_fov(self) -> float:
        """ 
        Calculate the vertical field of view of the camera  

        return the vertical field of view in degrees
        """
        rad = 2 * math.atan(self.height / 2 * self.focal_length) # in radians
        return math.degrees(rad) # in degrees
    
    
