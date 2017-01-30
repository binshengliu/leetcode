import unittest
import code

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = code.Solution()
        self.assertEqual(s.isPalindrome(1), True)
        self.assertEqual(s.isPalindrome(0), True)
        self.assertEqual(s.isPalindrome(121), True)
        self.assertEqual(s.isPalindrome(122), False)
        self.assertEqual(s.isPalindrome(1221), True)
        self.assertEqual(s.isPalindrome(-1221), False)
        self.assertEqual(s.isPalindrome(-2147447412), False)

if __name__ == '__main__':
    unittest.main()
