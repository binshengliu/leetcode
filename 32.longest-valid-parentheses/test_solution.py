import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = solution.Solution()
        self.assertEqual(s.longestValidParentheses('(()'), 2)
        self.assertEqual(s.longestValidParentheses(')()())'), 4)
        self.assertEqual(s.longestValidParentheses('()()()()'), 8)
        self.assertEqual(s.longestValidParentheses('()(())'), 6)

if __name__ == '__main__':
    unittest.main()
