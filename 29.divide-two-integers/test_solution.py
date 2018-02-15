import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = solution.Solution()
        self.assertEqual(s.divide(1, 1), 1)
        self.assertEqual(s.divide(20, 2), 10)
        self.assertEqual(s.divide(-20, 3), -6)
        self.assertEqual(s.divide(20, 1), 20)
        self.assertEqual(s.divide(-2147483648, -1), 2147483647) # overflow
        self.assertEqual(s.divide(-2147483648, 1), -2147483648)
        self.assertEqual(s.divide(-2147483647, -1), 2147483647)

if __name__ == '__main__':
    unittest.main()
