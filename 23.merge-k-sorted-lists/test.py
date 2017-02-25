import unittest
import code

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def convert(l):
    def to_linked_list(val):
        if not val:
            return None

        ret = ListNode(0)
        current = ret
        for c in val:
            current.next = ListNode(c)
            current = current.next
        return ret.next
    return [to_linked_list(val) for val in l]

def print_linked_list(l):
    while l != None:
        print(l.val, end=' ', flush=True)
        l = l.next
    print('')

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = code.Solution()
        ans = s.mergeKLists(convert([[1,5,7], [2,4,6]]))
        print_linked_list(ans)

    def test_2(self):
        s = code.Solution()
        ans = s.mergeKLists(convert([[-1,1],[-3,1,4],[-2,-1,0,2]]))
        print_linked_list(ans)

if __name__ == '__main__':
    unittest.main()
