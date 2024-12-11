from abc import ABC, abstractmethod
from AI.classes import Result

class BaseAI(ABC):
    def __init__(self, name:str, model_path:str, input_size:tuple, classes:list[str],logging=False):
        self.name:str = name
        self.model_path:str = model_path
        self.input_size:tuple = input_size
        self.classes:list[str] = classes
        self.logging = logging

    @abstractmethod
    def predict(self, image) -> Result:
        """
        Abstract method for making predictions.
        To be implemented by subclasses.
        """
        pass
    
    def get_info(self):
        """
        Returns basic information about the AI instance.
        """
        return {
            "name": self.name,
            "model_path": self.model_path,
            "input_size": self.input_size,
            "classes": self.classes,
        }
