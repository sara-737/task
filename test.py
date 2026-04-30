import unittest 

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)


def add(x, y):
    return x + y