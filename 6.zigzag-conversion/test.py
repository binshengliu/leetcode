import code
import unittest

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = code.Solution()
        self.assertEqual(s.convert('PAYPALISHIRING', 3), 'PAHNAPLSIIGYIR')
        self.assertEqual(s.convert('PAYPALISHIRING', 4), 'PINALSIGYAHRPI')
        self.assertEqual(s.convert('ABC', 1), 'ABC')

if __name__ == '__main__':
    unittest.main()
