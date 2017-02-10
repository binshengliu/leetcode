import unittest
import code

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = code.Solution()
        self.assertEqual(s.longestCommonPrefix(['abcd', 'ab']), 'ab')
        self.assertEqual(s.longestCommonPrefix(['ab', 'abcd']), 'ab')
        self.assertEqual(s.longestCommonPrefix(['ab', 'abcd', 'abcde']), 'ab')
        self.assertEqual(s.longestCommonPrefix(['b', 'abcd', 'abcde']), '')

if __name__ == '__main__':
    unittest.main()
