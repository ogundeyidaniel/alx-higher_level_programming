"""
TestMaxInteger testing max integer class
"""
import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_default_list(self):
        self.assertEqual(max_integer(), None)

    def test_max_list_first(self):
        lst = [55, 5, 3, 44]
        self.assertEqual(max_integer(lst), 55)

    def test_max_list_last(self):
        lst = [0, 1, 3, 55]
        self.assertEqual(max_integer(lst), 55)

    def test_max_mixed_list(self):
        lst = [-1, -4, 0, 4, -6]
        self.assertEqual(max_integer(lst), 4)

    def test_max_list_with_string(self):
        lst = ['issam', 5, 6, 9]
        with self.assertRaises(TypeError):
            max_integer(lst)

if __name__ == "__main__":
    unittest.main()
