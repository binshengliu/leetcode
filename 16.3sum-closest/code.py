# Similar to 3sum problem, except that the condition is "close" instead of
# "equal".

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            raise ValueError('\"nums\" has fewer than 3 elements.')

        nums.sort()
        closest = sum(nums[:3])
        for (i, c) in enumerate(nums):
            j, k = i + 1, len(nums) - 1
            while j < k:
                # print("j: {}, k: {}, nums[j]: {}, nums[k]: {}, c: {}".format(j, k, nums[j], nums[k], c))
                total = c + nums[j] + nums[k]
                if abs(total - target) < abs(closest - target):
                    # print("old: {}, new: {}".format(closest, c + total))
                    closest = total

                if total == target:
                    return closest
                elif total > target:
                    k -= 1
                else:                     #total < target
                    j += 1
        return closest
