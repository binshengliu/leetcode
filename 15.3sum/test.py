import unittest
import code

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = code.Solution()
        self.assertEqual(s.threeSum([-1, 0, 1, 2, -1, -1, -4]), [[-1, 0, 1], [-1, -1, 2]])

if __name__ == '__main__':
    unittest.main()
