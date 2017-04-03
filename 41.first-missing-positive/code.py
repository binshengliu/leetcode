# If the length of nums is n, then the answer <= n + 1. If an element
# in nums satisfies (1 <= element <= n - 1), then put it in the
# correct index. Do the same check on the swaped element.


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for (i, _) in enumerate(nums):
            while 0 < nums[i] and nums[i] < len(nums) \
                  and nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                (nums[nums[i] - 1], nums[i]) = (nums[i], nums[nums[i] - 1])

        missing_number = len(nums) + 1
        for (i, _) in enumerate(nums):
            if nums[i] != i + 1:
                missing_number = i + 1
                break
        return missing_number
