class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()

        # print("input: {}".format(nums))
        ans = []
        for (i, n) in enumerate(nums[:-3]):
            if i > 0 and nums[i - 1] == nums[i]: # avoid duplicates
                continue
            result = self.threeSum(nums[i+1:], target - n)
            if result:
                # print("Three sum result for {}: {}".format(target - n, result))
                for one in result:
                    one.insert(0, n)
                ans.extend(result)

        return ans

    def threeSum(self, nums, target):
        nums.sort()

        l = []
        d = {}
        for i, v in enumerate(nums):
            if v in d:
                d[v].append(i)
            else:
                d[v] = [i]

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]: # avoid duplicates
                continue

            for j, b in enumerate(nums[i + 1:], i + 1):
                if j > i + 1 and b == nums[j - 1]:
                    continue

                v = a + b
                if target-v in d:
                    if j < max(d[target-v]):
                        # print("d[-v]: {}".format(d[target-v]))
                        # print("l: {}, i: {}, a: {}, j:{}, b:{}".format(l, i, a, j, b))
                        l.append([a, b, target-v])
        return l
