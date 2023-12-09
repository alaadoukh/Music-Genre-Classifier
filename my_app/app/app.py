from flask import Flask, render_template, request
import requests
import base64

app = Flask(__name__)

svm_service_url = 'http://svm_service:8000'

@app.route('/')
def hello_world():
    return render_template('upload.html')

@app.route('/classify', methods=['POST'])
def classify():

    if 'musicFile' not in request.files:
        return "No file provided"

    # Get the uploaded file
    music_file = request.files['musicFile']

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

    return render_template('result.html', received_message=received_message, svm_response=svm_response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True, use_reloader=True)
