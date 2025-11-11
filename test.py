import unittest

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([1, 2]), 3)

if _name_ == '_main_':
    unittest.main()
