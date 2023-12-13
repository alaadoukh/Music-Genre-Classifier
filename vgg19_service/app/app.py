# svm_service/app.py
from flask import Flask, request, jsonify
import time
import base64
import os
import librosa
import numpy as np
import base64
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Get the absolute path to the directory of this script
base_path = os.path.abspath(os.path.dirname(__file__))

# Load the pre-trained model using joblib
model_path = os.path.join(base_path, "vgg-classification-model.h5")
model = load_model(model_path)

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read())
        return encoded_image.decode("utf-8")
    

@app.route('/classify', methods=['POST'])
def classify_image():
    data = request.get_json()

    if data and "image_data" in data:
        # Decode base64 data
        encoded_image_data = data["image_data"]
        decoded_image_data = base64.b64decode(encoded_image_data)

        # Save decoded data to a temporary image file
        temp_image_file = '/Nouvarch/shared_volume/temp_image.jpg'
        with open(temp_image_file, 'wb') as temp_file:
            temp_file.write(decoded_image_data)

        # Load and preprocess the image
        img = image.load_img(temp_image_file, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0  # Rescale the pixel values to the range [0, 1]

        # Make predictions
        predictions = model.predict(img_array)

        # Decode the predictions
        genres = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']
        predicted_genre = genres[np.argmax(predictions)]

        response_data = {"received_message": "Image file received and processed successfully",
                         "response": f"Predicted Genre: {predicted_genre}"}
    else:
        response_data = {"received_message": "No image file received", "response": "Error"}

    return jsonify(response_data)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
