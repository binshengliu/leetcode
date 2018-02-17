class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)

        # How many cuts at *index* i (inclusive).
        cuts = [i for i in range(length)]

        # Or it may mean how many cuts at *length* i. Then the edge
        # case can be avoided. But I think keeping the if middle -
        # span == 0 makes the code more clear.
        #
        # cuts = [i-1 for i in range(length+1)]

        for index in range(length):
            # Odd pal
            middle = index
            for span in range(0, min(middle, length - middle - 1) + 1):
                if s[middle-span] != s[middle+span]:
                    break

                if middle - span == 0:
                    cuts[middle+span] = 0
                else:
                    cuts[middle+span] = min(cuts[middle-span-1]+1, cuts[middle+span])

            # Even pal
            left = index
            right = index+1
            for span in range(0, min(left, length - right - 1) + 1):
                if s[left-span] != s[right+span]:
                    break

                if left - span == 0:
                    cuts[right+span] = 0
                else:
                    cuts[right+span] = min(cuts[left-span-1]+1, cuts[right+span])

        return cuts[length - 1]
