import unittest
from flask import Flask, url_for

class StreamDeckAppTestCase(unittest.TestCase):

    def setUp(self):
        # Create a test Flask app
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client: FlaskTestClient = self.app.test_client()

    def test_index_route(self):
        response = self.client.get('/')
        self.assertIn(b'Stream Deck', response.data)

    def test_static_file(self):
        # Set up a test request context
        with self.app.test_request_context():
             response = self.client.get(url_for('static', filename='styles.css'))
             self.assertIn(b'body', response.data)

if __name__ == '__main__':
    unittest.main()

