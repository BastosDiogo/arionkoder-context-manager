import unittest
from context_manager import ContextManager


class TestResourceContextManager(unittest.TestCase):
    def test_basic_connection(self):
        connected = []
        disconnected = []

        def mock_connect():
            connected.append(True)
            return "resource"

        def mock_disconnect(res):
            disconnected.append(True)

        with ContextManager("TestBasic", mock_connect, mock_disconnect) as r:
            self.assertEqual(r, "resource")

        self.assertTrue(connected)
        self.assertTrue(disconnected)

    def test_exception_handling(self):
        events = []

        def mock_connect():
            events.append("connect")
            return "res"

        def mock_disconnect(res):
            events.append("disconnect")

        with self.assertRaises(ValueError):
            with ContextManager("TestError", mock_connect, mock_disconnect):
                raise ValueError("erro simulado")

        self.assertEqual(events, ["connect", "disconnect"])

if __name__ == "__main__":
    unittest.main()
