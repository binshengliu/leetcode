import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = solution.Solution()
        result = s.threeSum([-1, 0, 1, 2, -1, -1, -4])
        self.assertEqual(result, [[-1, -1, 2], [-1, 0, 1]])

if __name__ == '__main__':
    unittest.main()
