import solution
import unittest

class TestSolution(unittest.TestCase):
    def test_number(self):
        s = solution.Solution()
        self.assertEqual(s.myAtoi('123'), 123)
        pass

    def test_overflow(self):
        s = solution.Solution()
        self.assertEqual(s.myAtoi('99999999999999999999999999999'), 2 ** 31 - 1)
        self.assertEqual(s.myAtoi('-99999999999999999999999999999'), -2 ** 31)
        pass

    def test_negative(self):
        s = solution.Solution()
        self.assertEqual(s.myAtoi('-123'), -123)
        pass

    def test_toomany_minus(self):
        s = solution.Solution()
        self.assertEqual(s.myAtoi('-1-23'), -1)
        pass

    def test_toomany_plus(self):
        s = solution.Solution()
        self.assertEqual(s.myAtoi('+1+23'), 1)
        pass

    def test_nonnumeric(self):
        s = solution.Solution()
        self.assertEqual(s.myAtoi('a123'), 0)
        pass

    def test_empty_str(self):
        s = solution.Solution()
        self.assertEqual(s.myAtoi(''), 0)
        pass

    def test_space(self):
        s = solution.Solution()
        self.assertEqual(s.myAtoi('  123    '), 123)
        pass

    def test_space(self):
        s = solution.Solution()
        self.assertEqual(s.myAtoi("  -0012a42"), -12)
        pass

if __name__ == '__main__':
    unittest.main()
