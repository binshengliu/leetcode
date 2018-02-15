import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = solution.Solution()
        self.assertEqual(s.searchInsert([1], 0), 0)
        self.assertEqual(s.searchInsert([1, 3, 5, 6], 5), 2)
        self.assertEqual(s.searchInsert([1, 3, 5, 6], 2), 1)
        self.assertEqual(s.searchInsert([1, 3, 5, 6], 7), 4)
        self.assertEqual(s.searchInsert([1, 3, 5, 6], 0), 0)
        self.assertEqual(s.searchInsert([1, 3], 4), 2)
        self.assertEqual(s.searchInsert([1], 2), 1)

if __name__ == '__main__':
    unittest.main()
