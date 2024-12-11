from AI.frc2023_ai import FRC2023AI
from robot import Robot
from detect import detect

model_path = 'models/best.pt'

def main():
    model = FRC2023AI("FRC2023", model_path, (640, 480), ["CONE", "CUBE"], logging=True)
    robot = Robot()

    detect(model, robot)



if __name__ == "__main__":
    main()
