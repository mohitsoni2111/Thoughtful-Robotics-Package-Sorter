import unittest
from sorter import sort

class TestPackageSorter(unittest.TestCase):
    def test_standard(self):
        self.assertEqual(sort(10, 100, 100, 10), "STANDARD")

    def test_bulky(self):
        self.assertEqual(sort(200, 50, 40, 10), "SPECIAL")

    def test_heavy(self):
        self.assertEqual(sort(50, 50, 50, 25), "SPECIAL")

    def test_rejected(self):
        self.assertEqual(sort(200, 200, 200, 25), "REJECTED")

if __name__ == "__main__":
    unittest.main()
