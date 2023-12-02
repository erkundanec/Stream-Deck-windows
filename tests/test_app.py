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



if __name__ == '__main__':
    unittest.main()

