import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = solution.Solution()
        self.assertEqual(s.letterCombinations('22'), ["aa","ab","ac","ba","bb","bc","ca","cb","cc"])
        self.assertEqual(s.letterCombinations('0'), [' '])
        self.assertEqual(s.letterCombinations('1'), ['*'])
        self.assertEqual(s.letterCombinations('12'), ["*a","*b","*c"])

if __name__ == '__main__':
    unittest.main()
