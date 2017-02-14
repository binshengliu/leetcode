import unittest
import code

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = code.Solution()
        self.assertEqual(s.threeSumClosest([-1, 2, 1, -4], 1), 2)
        self.assertEqual(s.threeSumClosest([-9, -1, 0, 2, 9], 0), 0)
        self.assertEqual(s.threeSumClosest([-9, -1, 0, 2, 9], 1), 1)
        self.assertEqual(s.threeSumClosest([-9, -1, 0, 3, 9], 9), 8)

if __name__ == '__main__':
    unittest.main()
