from AI.frc2023_ai import FRC2023AI
from robot import Robot
import asyncio
from detect import detect

model_path = 'models/best.pt'

async def main():
    model = FRC2023AI("FRC2023", model_path, (640, 480), ["CUBE", "CONE"], logging=True)
    robot = Robot()

    try:
        detect(model, robot)
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    asyncio.run(main())
