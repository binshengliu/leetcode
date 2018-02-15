import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = solution.Solution()
        self.assertEqual(s.longestCommonPrefix(['abcd', 'ab']), 'ab')
        self.assertEqual(s.longestCommonPrefix(['ab', 'abcd']), 'ab')
        self.assertEqual(s.longestCommonPrefix(['ab', 'abcd', 'abcde']), 'ab')
        self.assertEqual(s.longestCommonPrefix(['b', 'abcd', 'abcde']), '')

if __name__ == '__main__':
    unittest.main()
