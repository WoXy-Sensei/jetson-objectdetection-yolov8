from AI.base_ai import BaseAI
from libs.utils.log import log
from ultralytics import YOLO


class FRC2023AI(BaseAI):
    """ 
        A class to represent the FRC2023 AI
    """

    def __init__(self, name, model_path, input_size, classes, logging=False):
        super().__init__(name, model_path, input_size, classes,logging)
        self.model = YOLO(self.model_path)

    def predict(self, image, conf: float = 0.5, verbose: bool = False, device: str = "cpu", max_det: int = 10):
        """
        Placeholder method for making predictions
        """
        results = self.model.predict(
            image, conf=conf, verbose=verbose, device=device, max_det=max_det, imgsz=self.input_size)[0]
        if (self.logging):
            if(len(results) > 0):
                log(f"""
            Number of objects detected: {len(results)}
            Classes detected: {[self.classes[int(obj.boxes.cls.item())] for obj in results]}
                """, "success")
            else:
                log("No objects detected", "danger")

        return results
