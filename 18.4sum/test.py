import unittest
import code

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = code.Solution()
        # print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
        # print(s.threeSum([1, 0, -1, 0, 2], 2))
        # self.assertEqual(s.fourSum([1, 0, -1, 0, -2, 2], 0), 0)
        print(s.fourSum([-1,-5,-5,-3,2,5,0,4], -7))

if __name__ == '__main__':
    unittest.main()
