import unittest
import code

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class TestSolution(unittest.TestCase):
    def test_1(self):
        s = code.Solution()

        head = ListNode(1)
        c = head
        for i in range(2, 6):
            c.next = ListNode(i)
            c = c.next

        ans = s.removeNthFromEnd(head, 2)
        t = ans
        self.assertEqual(t.val, 1)

        t = t.next
        self.assertEqual(t.val, 2)

        t = t.next
        self.assertEqual(t.val, 3)

        t = t.next
        self.assertEqual(t.val, 5)

    def test_2(self):
        s = code.Solution()

        head = ListNode(1)
        c = head
        for i in range(2, 3):
            c.next = ListNode(i)
            c = c.next

        ans = s.removeNthFromEnd(head, 1)
        t = ans
        self.assertEqual(t.val, 1)

if __name__ == '__main__':
    unittest.main()
