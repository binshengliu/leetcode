import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = solution.Solution()
        # self.assertEqual(1, 1)
        ans = s.generateParenthesis(4)
        print(ans)

if __name__ == '__main__':
    unittest.main()
