import unittest
import code

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = code.Solution()
        self.assertEqual(s.intToRoman(1), 'I')
        self.assertEqual(s.intToRoman(47), 'XLVII')
        self.assertEqual(s.intToRoman(123), 'CXXIII')
        self.assertEqual(s.intToRoman(999), 'CMXCIX')
        self.assertEqual(s.intToRoman(1998), 'MCMXCVIII')
        self.assertEqual(s.intToRoman(2345), 'MMCCCXLV')
        self.assertEqual(s.intToRoman(3999), 'MMMCMXCIX')
        pass

if __name__ == '__main__':
    unittest.main()
