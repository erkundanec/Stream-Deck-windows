import unittest
from flask import Flask, url_for

class StreamDeckAppTestCase(unittest.TestCase):

    def setUp(self):
        # Create a test Flask app
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_index_route(self):
        response = self.client.get('/')
        self.assertIn(b'Stream Deck', response.data)

    def test_static_file(self):
    # Set up a test request context
        with self.app.test_request_context():
            response = self.client.get(url_for('static', filename='styles.css'))
            # Check for specific styles in the response data
            self.assertIn(b'body {', response.data)
            self.assertIn(b'font-family: Arial, sans-serif;', response.data)
            self.assertIn(b'.stream-deck {', response.data)
            self.assertIn(b'display: flex;', response.data)
            self.assertIn(b'.stream-button {', response.data)
            self.assertIn(b'width: 100px;', response.data)
            # ... add more assertions as needed


if __name__ == '__main__':
    unittest.main()

