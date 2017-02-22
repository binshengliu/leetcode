import unittest
import code

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = code.Solution()
        self.assertEqual(s.isValid("()]"), False)
        self.assertEqual(s.isValid("[]()"), True)
        self.assertEqual(s.isValid("[][()"), False)

if __name__ == '__main__':
    unittest.main()
