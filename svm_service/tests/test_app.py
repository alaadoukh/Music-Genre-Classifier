import unittest
from flask import json
import base64
from svm_service.app import app

class SVMServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_classify_endpoint(self):
        # Assuming you have a test audio file in your tests directory
        with open('tests/metal.00011.wav', 'rb') as audio_file:
            audio_data = audio_file.read()

        # Convert audio to base64
        encoded_audio_data = base64.b64encode(audio_data).decode('utf-8')

        # Prepare JSON data
        data = {"audio_data": encoded_audio_data}

        # Make a request to the /classify endpoint
        response = self.app.post('/classify', json=data)

        # Validate the response
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertIn('received_message', response_data)
        self.assertIn('response', response_data)
        self.assertEqual(response_data['received_message'], 'audio file received and processed successfully')

if __name__ == '__main__':
    unittest.main()
