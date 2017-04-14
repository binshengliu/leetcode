class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]

        nums.sort()

        ans = []
        for (i, num) in enumerate(nums):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            sub_ans = self.permuteUnique(nums[:i] + nums[i+1:])
            for a_list in sub_ans:
                a_list.insert(0, num)
            ans.extend(sub_ans)

        return ans
