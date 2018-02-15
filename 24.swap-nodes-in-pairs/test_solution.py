import unittest
import solution

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def to_linked_list(val):
    if not val:
        return None

    ret = ListNode(0)
    current = ret
    for c in val:
        current.next = ListNode(c)
        current = current.next
    return ret.next

def print_linked_list(msg, l):
    print(msg)
    while l != None:
        print(l.val, end=' ', flush=True)
        l = l.next
    print('\n')

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = solution.Solution()
        ans = s.swapPairs(to_linked_list([1, 2, 3, 4]))
        print_linked_list('first answer: ', ans)

    def test_2(self):
        s = solution.Solution()
        ans = s.swapPairs(to_linked_list([1, 2, 3]))
        print_linked_list('second answer:', ans)

    def test_3(self):
        s = solution.Solution()
        ans = s.swapPairs(to_linked_list([1]))
        print_linked_list('third answer:', ans)

    def test_4(self):
        s = solution.Solution()
        ans = s.swapPairs(to_linked_list([1, 2, 3, 4, 5]))
        print_linked_list('second answer:', ans)

if __name__ == '__main__':
    unittest.main()
