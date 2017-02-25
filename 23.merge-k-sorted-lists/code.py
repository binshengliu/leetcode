from operator import itemgetter, attrgetter

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# def print_linked_list(l):
#     while l != None:
#         print(l.val, end=' ', flush=True)
#         l = l.next
#     print('')

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        tmp = [val for val in lists if val != None]

        ans = None
        c = None
        tmp.sort(key=attrgetter('val'))
        while tmp:
            if c == None:
                c = tmp[0]
                ans = c
            else:
                c.next = tmp[0]
                c = c.next
            tmp[0] = tmp[0].next
            c.next = None

            if tmp[0] == None:
                del tmp[0]
                continue

            # for l in tmp:
            #     print_linked_list(l)

            # print('')

            i = 0
            while i < len(tmp) - 1 and tmp[i].val > tmp[i+1].val:
                tmp[i], tmp[i+1] = tmp[i+1], tmp[i]
                i += 1

            # for l in tmp:
            #     print_linked_list(l)

            # print('-----------------------')
        return ans
