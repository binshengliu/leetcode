import code
import unittest

class TestSolution(unittest.TestCase):
    def test_compare(self):
        self.assertEqual(code.compare('1', '1'), 0)
        self.assertEqual(code.compare('2', '1'), 1)
        self.assertEqual(code.compare('2', '3'), -1)

    def test_1(self):
        s = code.Solution()
        self.assertEqual(s.reverse(123), 321)
        self.assertEqual(s.reverse(-123), -321)
        self.assertEqual(s.reverse(0), 0)
        self.assertEqual(s.reverse(10), 1)
        self.assertEqual(s.reverse(1534236469), 0)
        self.assertEqual(s.reverse(1563847412), 0)

if __name__ == '__main__':
    unittest.main()
