from AI.base_ai import BaseAI
from libs.utils.log import log
from ultralytics import YOLO
from AI.classes import Result, Prediction
from libs.vision.classes import BBox


class FRC2023AI(BaseAI):
    """ 
        A class to represent the FRC2023 AI
    """

    def __init__(self, name, model_path, input_size, classes, logging=False):
        super().__init__(name, model_path, input_size, classes, logging)
        self.model = YOLO(self.model_path)

    def predict(self, image, conf: float = 0.5, verbose: bool = False, device: str = "cpu", max_det: int = 10):
        """
        Placeholder method for making predictions
        """
        results = self.model.predict(
            image, conf=conf, verbose=verbose, device=device, max_det=max_det, imgsz=self.input_size)[0]
        if (self.logging):
            if (len(results) > 0):
                log(f"""
            Number of objects detected: {len(results)}
            Classes detected: {[self.classes[int(obj.boxes.cls.item())] for obj in results]}
                """, "success")
            else:
                log("No objects detected", "danger")
            

    
        result = Result(
            objects_count=len(results),
            predictions=[
                Prediction(
                    cls=(self.classes[int(obj.boxes.cls.item())], int(
                        obj.boxes.cls.item())),
                    bbox=BBox(
                        xmax=obj.boxes.xyxy[0][2].item(),
                        xmin=obj.boxes.xyxy[0][0].item(),
                        ymax=obj.boxes.xyxy[0][3].item(),
                        ymin=obj.boxes.xyxy[0][1].item()
                    )
                ) for obj in results
            ]

        )

        return result
