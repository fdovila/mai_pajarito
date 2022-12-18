import unittest
from src.main import app

class TestMain(unittest.TestCase):
    def test_app(self):
        app()

if __name__ == "__main__":
    unittest.main()
