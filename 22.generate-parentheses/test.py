import unittest
import code

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = code.Solution()
        # self.assertEqual(1, 1)
        ans = s.generateParenthesis(4)
        print(ans)

if __name__ == '__main__':
    unittest.main()
