import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# This solution works. But since LinkNode shouldn't be modified and heapq does not
# support custom sorting very well, the solution breaks when there are same
# priorities in the list and heapq tries to compare further elements. Refer to
# http://stackoverflow.com/questions/3954530/how-to-make-heapq-evaluate-the-heap-off-of-a-specific-attribute/3954575#3954575

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = [(i.val, i) for i in lists if i != None]

        heapq.heapify(heap)

        ans = None
        c = None
        while heap:
            smallest = heapq.heappop(heap)
            if c == None:
                c = smallest[1]
                ans = c
            else:
                c.next = smallest[1]
                c = c.next

            next_node = smallest[1].next
            c.next = None

            if next_node == None:
                continue

            heapq.heappush(heap, (next_node.val, next_node))

        return ans
