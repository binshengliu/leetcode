class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return True

            if nums[mid] < nums[right]:
                if target < nums[mid]:
                    right = mid - 1
                else:
                    if target <= nums[right]:
                        left = mid + 1
                    elif nums[left] <= target:
                        right = mid - 1
                    else:
                        return False
            elif nums[left] < nums[mid]:
                if nums[mid] < target:
                    left = mid + 1
                else:
                    if nums[left] <= target:
                        right = mid - 1
                    elif target <= nums[right]:
                        left = mid + 1
                    else:
                        return False
            elif nums[mid] == nums[right]:
                right -= 1
            elif nums[mid] == nums[left]:
                left += 1

        return False
