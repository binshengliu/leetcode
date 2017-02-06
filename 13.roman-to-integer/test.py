import unittest
import code

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = code.Solution()
        self.assertEqual(s.romanToInt('I'), 1)
        self.assertEqual(s.romanToInt('XLVII'), 47)
        self.assertEqual(s.romanToInt('CXXIII'), 123)
        self.assertEqual(s.romanToInt('CMXCIX'), 999)
        self.assertEqual(s.romanToInt('MCMXCVIII'), 1998)
        self.assertEqual(s.romanToInt('MMCCCXLV'), 2345)
        self.assertEqual(s.romanToInt('MMMCMXCIX'), 3999)

if __name__ == '__main__':
    unittest.main()
