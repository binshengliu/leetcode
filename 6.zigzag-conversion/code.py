class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        array = [[] for i in range(numRows)]
        curr = 0
        increase = True
        for i, c in enumerate(s):
            array[curr].append(c)

            if curr == numRows - 1:
                increase = False
            elif curr == 0:
                increase = True

            if increase:
                curr = curr + 1
            else:
                curr = curr - 1

        return ''.join(''.join(line) for line in array)

import unittest

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = Solution()
        self.assertEqual(s.convert('PAYPALISHIRING', 3), 'PAHNAPLSIIGYIR')
        self.assertEqual(s.convert('PAYPALISHIRING', 4), 'PINALSIGYAHRPI')
        self.assertEqual(s.convert('ABC', 1), 'ABC')

if __name__ == '__main__':
    unittest.main()
