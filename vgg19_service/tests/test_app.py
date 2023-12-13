import unittest
from flask import json
import base64
from svm_service.app import app

class SVMServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_classify_endpoint(self):
        with open('tests/disco00056.png', 'rb') as image_file:
            image_data = image_file.read()

        # Convert image to base64
        encoded_image_data = base64.b64encode(image_data).decode('utf-8')

        # Prepare JSON data
        data = {"image_data": encoded_image_data}

        response = self.app.post('/classify', json=data)

        # Validate the response
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.data)
        self.assertIn('received_message', response_data)
        self.assertIn('response', response_data)
        self.assertEqual(response_data['received_message'], 'Image file received and processed successfully')

if __name__ == '__main__':
    unittest.main()
