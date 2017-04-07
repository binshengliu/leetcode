

# Imagin the first and last bar as two walls. Search through the lower
# wall towards the higher wall. See
# https://discuss.leetcode.com/topic/5125/sharing-my-simple-c-code-o-n-time-o-1-space
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height) - 1
        max_left = 0
        max_right = 0
        water = 0
        while left <= right:
            if max_left < max_right:
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    water += max_left - height[left]
                left += 1
            else:
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    water += max_right - height[right]
                right -= 1

        return water
