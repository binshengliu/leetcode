import unittest
import code

class TestSolution(unittest.TestCase):
    cases = (('barfoothefoobarman', ['foo', 'bar'], [0, 9]),
                 ('barfoothefoobarman', ['foo', 'bar', 'the'], [0, 6]),
                 ('barfoothekfoobarman', ['foo', 'bar', 'the'], [0]),
                 ('barfoothekfoobarman', ['fook', 'bar', 'the'], []))

    def test_1(self):
        s = code.Solution()
        for case in self.cases:
            self.assertEqual(s.findSubstring(case[0], case[1]), case[2])

if __name__ == '__main__':
    unittest.main()
