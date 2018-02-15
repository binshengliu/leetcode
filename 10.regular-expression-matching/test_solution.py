import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = solution.Solution()
        self.assertEqual(s.isMatch("aa","a"), False)
        self.assertEqual(s.isMatch("aa","aa"), True)
        self.assertEqual(s.isMatch("aaa","aa"), False)
        self.assertEqual(s.isMatch("aa", "a*"), True)
        self.assertEqual(s.isMatch("aa", ".*"), True)
        self.assertEqual(s.isMatch("ab", ".*"), True)
        self.assertEqual(s.isMatch("aab", "c*a*b"), True)
        self.assertEqual(s.isMatch("", "c*a*b*"), True)
        self.assertEqual(s.isMatch("", ""), True)
        self.assertEqual(s.isMatch('abcd', 'd*'), False)
        self.assertEqual(s.isMatch('aaa', 'aaaa'), False)

if __name__ == '__main__':
    unittest.main()
