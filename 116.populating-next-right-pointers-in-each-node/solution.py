# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return

        q = [root]
        while q:
            count = len(q)
            for i in range(count - 1):
                q[i].next = q[i+1]
            for i in range(count):
                if q[i] and q[i].left:
                    q.append(q[i].left)
                if q[i] and q[i].right:
                    q.append(q[i].right)
            del q[:count]
