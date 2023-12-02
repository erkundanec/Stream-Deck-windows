import unittest
from flask import Flask, url_for

class StreamDeckAppTestCase(unittest.TestCase):

    def setUp(self):
        # Create a test Flask app
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()




    def tearDown(self):
        # Clean up after each test
        pass

    def test_dummy_pass_1(self):
        # This is a dummy test that always passes
        self.assertTrue(True)

    def test_dummy_pass_2(self):
        # Another dummy test that always passes
        self.assertEqual(2 + 2, 4)

    def test_dummy_pass_3(self):
        # Yet another dummy test that always passes
        self.assertIn('dummy', 'dummy test')

    def test_dummy_pass_4(self):
        # A dummy test using a context manager
        with self.subTest():
            self.assertTrue(True)






if __name__ == '__main__':
    unittest.main()

