import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = solution.Solution()
        self.assertEqual(s.maxArea([1, 1]), 1)
        self.assertEqual(s.maxArea([1, 9, 9, 1]), 9)

if __name__ == '__main__':
    unittest.main()
