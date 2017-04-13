class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [nums]

        ans = []
        for (i, num) in enumerate(nums):
            sub_ans = self.permute(nums[:i] + nums[i+1:])
            for a_list_in_sub_ans in sub_ans:
                a_list_in_sub_ans.insert(0, num)
            ans.extend(sub_ans)

        return ans
