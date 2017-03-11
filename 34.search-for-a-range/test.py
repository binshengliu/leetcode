import unittest
import code

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = code.Solution()
        self.assertEqual(s.searchRange([5, 7, 7, 8, 8, 10], 8), [3, 4])
        self.assertEqual(s.searchRange([5, 7, 7, 8, 8, 10], 7), [1, 2])
        self.assertEqual(s.searchRange([], 7), [-1, -1])
        self.assertEqual(s.searchRange([5, 8, 9], 7), [-1, -1])
        self.assertEqual(s.searchRange([1, 3], 1), [0, 0])
        self.assertEqual(s.searchRange([2, 2], 3), [-1, -1])

if __name__ == '__main__':
    unittest.main()
