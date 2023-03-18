from tensorflow.keras.models import load_model
from flask import Flask, request, render_template
import numpy as np
from PIL import Image

flask_app = Flask(__name__)

class_names = ['Tomato_Early_blight', 'Tomato_Late_blight', 'Tomato_healthy']
model = load_model('model')

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/predict", methods = ["POST"])
def predict():
    image = Image.open(request.files['image'])
    image = image.resize((256, 256))
    image = image.convert('RGB')
    img_array = np.array(image)
    img_array = np.expand_dims(img_array, axis=0)
    print(model.predict(img_array))
    prediction = model.predict(img_array)

    predicted_class = class_names[np.argmax(prediction)]
    confidence = round(100 * (np.max(prediction)), 2)
    message = f"The tomato is predicted to be {predicted_class} with {confidence}% confidence"

    return render_template("index.html", message=message)


if __name__ == "__main__":
    flask_app.run(debug=True)
