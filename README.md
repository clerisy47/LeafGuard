# LeafGuard

## Overview

This Python application is designed to run on a Raspberry Pi and utilizes a pre-trained TensorFlow Keras model to classify tomato images into three categories: Early Blight, Late Blight, and Healthy. The model has been trained to make predictions based on input images provided to it.

## Prerequisites

- Raspberry Pi with camera module
- Python 3.x installed
- Required Python packages: tensorflow, numpy, Pillow (PIL), picamera

## Installation

1. Clone this repository to your Raspberry Pi:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. Install the required Python packages:

    ```bash
    pip install tensorflow numpy Pillow picamera[array]
    ```

3. Ensure that you have a pre-trained model file named `model` in the root directory of the project. You can replace it with your own trained model.

## Usage

1. Ensure your Raspberry Pi camera module is connected.

2. Run the application:

    ```bash
    python your_app_name.py
    ```

3. The application will capture an image using the Raspberry Pi camera and classify the tomato in the image using the pre-trained model.

4. The result, including the predicted class and confidence, will be printed to the console.

## Configuration

- The `class_names` variable contains the classes that the model can predict.
- The `image_path` variable specifies the path to the captured image. Update it to match your project's file structure.

## Notes

- This application assumes that the Raspberry Pi camera module is properly connected and configured.
- Ensure that the model file is present in the root directory and matches the expected file name ('model').
- Modify the `class_names` list according to your model's output classes.
- The `capture_image` function uses the `picamera` module to capture an image. Adjust the `time.sleep` duration based on your camera's initialization time.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute it as needed.

## Acknowledgments

- TensorFlow and Keras for providing powerful tools for machine learning on embedded devices.
- The Raspberry Pi community for their continuous support and contributions to the field of DIY electronics.

Please feel free to reach out for any questions or improvements!
