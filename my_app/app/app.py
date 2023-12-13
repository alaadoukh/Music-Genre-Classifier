import json
from flask import Flask, render_template, request
import requests
import base64

app = Flask(__name__)

svm_service_url = 'http://svm_service:8000'
vgg19_service_url = 'http://vgg19_service:9000'


@app.route('/')
def hello_world():
    return render_template('upload.html')

@app.route('/classify_audio', methods=['POST'])
def classify():

    if 'fileInput' not in request.files:
        return "No file provided"

    # Get the uploaded file
    music_file = request.files['fileInput']

    # Save the file to the shared volume
    # file_path = '/Nouvarch/shared_volume/' + music_file.filename
    # music_file.save(file_path)

    # Read and encode the file to base64
    encoded_music_data = base64.b64encode(music_file.read()).decode('utf-8')

    # Send the base64-encoded data to svm_service
    response = requests.post(f'{svm_service_url}/classify', json={"music_data": encoded_music_data})

    # Assuming svm_service returns a JSON response
    response_data = response.json()

    # Process the response as needed
    received_message = response_data.get("received_message", "No message received")
    svm_response = response_data.get("response", "No response received")

    return render_template('result.html', received_message=received_message, response=svm_response)

@app.route('/classify_image', methods=['POST'])
def classify_image():

    if 'fileInput' not in request.files:
        return "No file provided"

    # Get the uploaded image file
    image_file = request.files['fileInput']

    # Read and encode the image file to base64
    encoded_image_data = base64.b64encode(image_file.read()).decode('utf-8')

    # Send the base64-encoded data to vgg19_service
    response = requests.post(f'{vgg19_service_url}/classify', json={"image_data": encoded_image_data})

    # Assuming 'response' is the variable containing the response from the server
    try:
        response_data = response.json()
    except json.decoder.JSONDecodeError:
        # Handle the case where the response is not valid JSON
        print("Error: Invalid JSON response")
        response_data = {}

    # Process the response as needed
    received_message = response_data.get("received_message", "No message received")
    vgg19_response = response_data.get("response", "No response received")

    return render_template('result.html', received_message=received_message, response=vgg19_response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True, use_reloader=True)
