import unittest
import code

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = code.Solution()
        self.assertEqual(s.search([4, 5, 6, 7, 0, 1, 2], 5), 1)

if __name__ == '__main__':
    unittest.main()
