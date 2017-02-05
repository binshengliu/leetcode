
# I use a window to test the area between two lines. The window is initialized
# as the first and last index of height. After compared the area of the window
# with current max area, the index with smaller number is changed by 1 so the
# window is smaller. This is because changing the index with larger number
# can't get any larger area than current one. If the numbers of both indices
# are same, the two indices should be simultaneously changed.

# For example, if length of height 10 with height[0] = 8 and height[9] =
# 3. Now, i is initialized to 0 and j is initialized to 9, so we get an area of
# 27. Next we should decrease j, because increasing i can't help up get a
# result greater than 27.

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        i = 0
        j = len(height) - 1

        while j > i:
            area = (j - i) * min(height[i], height[j])
            if area > maxArea:
                maxArea = area
            if height[i] > height[j]:
                j -= 1
            elif height[i] < height[j]:
                i += 1
            else:
                j -= 1
                i += 1

        return maxArea
