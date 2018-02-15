import unittest
import solution
import sys
from linked_list import *

class TestSolution(unittest.TestCase):


    def test_1(self):
        s = solution.Solution()
        ans = s.reverseKGroup(list_to_linked_list([1, 2, 3]), 2)
        # print_linked_list('1. : ', ans)
        self.assertEqual(linked_list_to_list(ans), [2, 1, 3])

    def test_2(self):
        s = solution.Solution()
        ans = s.reverseKGroup(list_to_linked_list([1, 2, 3, 4, 5]), 3)
        # print_linked_list('2. :', ans)
        self.assertEqual(linked_list_to_list(ans), [3, 2, 1, 4, 5])

    def test_3(self):
        s = solution.Solution()
        ans = s.reverseKGroup(list_to_linked_list([1]), 2)
        # print_linked_list('third answer:', ans)
        self.assertEqual(linked_list_to_list(ans), [1])

    def test_4(self):
        s = solution.Solution()
        ans = s.reverseKGroup(list_to_linked_list([1, 2, 3, 4, 5]), 4)
        # print_linked_list('second answer:', ans)
        self.assertEqual(linked_list_to_list(ans), [4, 3, 2, 1, 5])

if __name__ == '__main__':
    unittest.main()
