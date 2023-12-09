# svm_service/app.py
from flask import Flask, request, jsonify
import time
import base64
import os
import librosa
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Get the absolute path to the directory of this script
base_path = os.path.abspath(os.path.dirname(__file__))

# Load the pre-trained model using joblib
model_path = os.path.join(base_path, "svm-classification-model.h5")
model = load_model(model_path)

genre_dict = {0: 'blues', 1: 'classical', 2: 'country', 3: 'disco',
              4: 'hiphop', 5: 'jazz', 6: 'metal', 7: 'pop', 8: 'reggae', 9: 'rock'}

# Function to retrieve the latest audio file from a directory


# def get_latest_audio_file(directory):
#     files = [os.path.join(directory, f) for f in os.listdir(
#         directory) if f.endswith('.wav')]  # Change extension if different
#     if files:
#         # Get the latest file based on creation time
#         return max(files, key=os.path.getctime)
#     else:
#         return None


def extract_features(file_path):
    # Load audio file with librosa
    audio, sample_rate = librosa.load(file_path, res_type='kaiser_fast')
    # Extract MFCCs and other features...
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=20)
    mfccs_processed = np.mean(mfccs.T, axis=0)

    return mfccs_processed


def predict_genre(file_path):
    # Extract features
    features = extract_features(file_path)

    # Reshape features to fit the model input format
    features = np.reshape(features, (1, -1))  # Reshape for model

    # Predict genre
    prediction = model.predict(features)
    print("Raw Prediction:", prediction)
    # Convert prediction to genre
    predicted_genre = np.argmax(prediction)
    predicted_genre_name = genre_dict.get(predicted_genre, "Unknown Genre")
    return predicted_genre_name


@app.route('/classify', methods=['POST'])
def classify():
    data = request.get_json()
    if data and "music_data" in data:
        # Decode base64 data
        encoded_music_data = data["music_data"]
        decoded_music_data = base64.b64decode(encoded_music_data)

        # Save decoded data to a temporary WAV file
        temp_wav_file = '/Nouvarch/shared_volume/temp_audio.wav'
        with open(temp_wav_file, 'wb') as temp_file:
            temp_file.write(decoded_music_data)

        # Process the temporary WAV file
        genre = predict_genre(temp_wav_file)

        response_data = {"received_message": "Music file received and processed successfully",
                         "response": f"Predicted Genre: {genre}"}
    else:
        response_data = {"received_message": "No music file received", "response": "Error"}

    return jsonify(response_data)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
