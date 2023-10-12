from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import streamlit as st


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


st.title("Tomato Disease Classification")
upload_file = st.file_uploader("Upload tomato leaves images", type = ['jpg', 'png', 'jpeg'])
generate_pred = st.button("Predict")

if generate_pred:
    image = Image.open(upload_file)
    with st.expander('image', expanded=True):
        st.image(image, use_column_width=True)
    st.markdown(f"<h2>{predict(image)}</h2>", unsafe_allow_html=True)
