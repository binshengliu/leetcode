# With one iteration through 'nums', the rest of the problem is a 2sum
# problem. The key to handling duplication is to sort the list and
# ignore the elements when appropriate.

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        l = []
        d = {}
        for i, v in enumerate(nums):
            if v in d:
                d[v].append(i)
            else:
                d[v] = [i]

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            for j, b in enumerate(nums[i + 1:], i + 1):
                if j > i + 1 and b == nums[j - 1]:
                    continue

                v = a + b
                if -v in d:
                    if j < max(d[-v]):
                        # print("d[-v]: {}".format(d[-v]))
                        # print("l: {}, i: {}, a: {}, j:{}, b:{}".format(l, i, a, j, b))
                        l.append([a, b, -v])
        return l

