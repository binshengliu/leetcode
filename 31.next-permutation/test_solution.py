import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = solution.Solution()
        l = [1, 2, 3]
        s.nextPermutation(l)
        self.assertEqual(l, [1, 3, 2])

        l = [3, 2, 1]
        s.nextPermutation(l)
        self.assertEqual(l, [1, 2, 3])

        l = [1, 1, 5]
        s.nextPermutation(l)
        self.assertEqual(l, [1, 5, 1])

        l = [3, 5, 4, 1]
        s.nextPermutation(l)
        self.assertEqual(l, [4, 1, 3, 5])

        l = [1]
        s.nextPermutation(l)
        self.assertEqual(l, [1])

        l = []
        s.nextPermutation(l)
        self.assertEqual(l, [])

if __name__ == '__main__':
    unittest.main()
