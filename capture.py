import time
import picamera

def capture_image(file_path):
    with picamera.PiCamera() as camera:
        time.sleep(2)
        camera.capture(file_path)

if __name__ == "__main__":
    image_path = "/raspberry_pi/images/image.jpg" 
    capture_image(image_path)
    print(f"Image captured and saved at {image_path}")
