# Object Detection Project

This project aims to perform object detection using the YOLOv3 model on the Jetson Nano device.

## Requirements

- Jetson Nano device
- JetPack SDK
- Python 3.x
- CUDA and cuDNN
- OpenCV
- YOLOv8 model

## Installation

1. Ensure that JetPack SDK is installed.
2. Download and install Python 3.x from [here](https://www.python.org/downloads/).
3. Install CUDA and cuDNN on the Jetson Nano following the instructions [here](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html).
4. Install OpenCV using the following command in the terminal:
   ```bash
   pip install opencv-python
    ```

## Usage

1. Run the `main.py` script to initiate object detection:
   ```bash
   python main.py
    ```
2. Observe object detection results on the camera feed.

## License

This project is licensed under the MIT License.

## Contribution

If you wish to contribute, please open an issue first, and then submit a pull request.