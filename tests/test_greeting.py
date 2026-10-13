import unittest

from src.greeting import greet


class GreetingTests(unittest.TestCase):
    def test_greet_includes_name(self):
        self.assertEqual(greet("Git"), "Hello, Git!")


if __name__ == "__main__":
    unittest.main()
