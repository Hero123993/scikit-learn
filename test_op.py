import unittest
from op import send_line_notify
from Untitled1 import coin

class TestLineNotify(unittest.TestCase):
    def test_send_line_notify(self):
        # This test assumes a valid token and network connectivity
        total_value, coin_10, coin_5, coin_1 = coin()
        token = "HBhODgY43Y9rYIYv1yirI0xkVypNFJMcjVgocuaRGTD"
        response = send_line_notify(total_value, coin_10, coin_5, coin_1, token)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()