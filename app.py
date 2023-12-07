from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

class_names = ['Tomato_Early_blight', 'Tomato_Late_blight', 'Tomato_healthy']
model = load_model('model')

def predict(image):
    image = image.resize((256, 256))
    image = image.convert('RGB')
    img_array = np.array(image)
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)

    predicted_class = class_names[np.argmax(prediction)]
    confidence = round(100 * (np.max(prediction)), 2)
    message = f"The tomato is predicted to be {predicted_class} with {confidence}% confidence"

    return message.replace('_', ' ')

# Replace this path with the actual image path on your Raspberry Pi
image_path = "raspberry_pi/images/image.jpeg"

try:
    image = Image.open(image_path)
except Exception as e:
    print(f"Error opening the image: {e}")
    exit()

prediction_message = predict(image)
print(prediction_message)
