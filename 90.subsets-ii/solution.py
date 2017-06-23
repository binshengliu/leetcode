class Solution(object):
    def subset_of_specific_number(self, nums, count):
        """
        :type nums: List[int]
        :type count: int
        :rtype: List[List[int]]
        """
        if count == 0:
            return [[]]

        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            sub_ans = self.subset_of_specific_number(nums[i+1:], count - 1)
            for one in sub_ans:
                one.insert(0, nums[i])
            ans.extend(sub_ans)
        return ans

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        count = len(nums)
        nums.sort()
        for i in range(count+1):
            sub_ans = self.subset_of_specific_number(nums, i)
            ans.extend(sub_ans)
        return ans
