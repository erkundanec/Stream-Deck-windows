import unittest
from flask import Flask, url_for

class StreamDeckAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_index_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Stream Deck', response.data)

    def test_static_file(self):
        response = self.client.get(url_for('static', filename='styles.css'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'body', response.data)

if __name__ == '__main__':
    unittest.main()
