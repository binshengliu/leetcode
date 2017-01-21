class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # In python, we can get the count. If count is odd, just find the
        # (count/2)th element. If count is even, find average of ((count/2 -
        # 1)th + (count/2)th)
        count = len(nums1) + len(nums2)
        if count % 2 == 0:
            pos1 = int(count / 2 - 1)
            pos2 = int(count / 2)
        else:
            pos1 = int(count / 2)
            pos2 = int(count / 2)

        nums3 = []
        i = 0
        j = 0
        while True:
            if i >= len(nums1):
                while j < len(nums2):
                    nums3.append(nums2[j])
                    j = j + 1
                    # can be optimized when len(nums3) reach pos2
                break

            if j >= len(nums2):
                while i < len(nums1):
                    nums3.append(nums1[i])
                    i = i + 1
                    # can be optimized when len(nums3) reach pos2
                break

            if nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i = i + 1
            elif nums2[j] < nums1[i]:
                nums3.append(nums2[j])
                j = j + 1
            else:
                nums3.append(nums1[i])
                nums3.append(nums2[j])
                i = i + 1
                j = j + 1
            # can be optimized when len(nums3) reach pos2
        return (float(nums3[pos1]) + float(nums3[pos2])) / 2

if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    result = s.findMedianSortedArrays(nums1, nums2)
    print("Find in {} and {}, result: {}.".format(nums1, nums2, result))

    nums1 = [1, 2]
    nums2 = [3, 4]
    result = s.findMedianSortedArrays(nums1, nums2)
    print("Find in {} and {}, result: {}.".format(nums1, nums2, result))
