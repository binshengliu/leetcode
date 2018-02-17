class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        # Whether string i through j (inclusive) is a pal.
        pal = [[False for col in range(n)] for row in range(n)]

        # How many cuts at *index* i (inclusive).
        cuts = [i for i in range(n)]

        for col in range(0, n):
            for row in range(col+1):
                if row == col:
                    # A single character is certainly a pal.
                    pal[row][col] = True
                elif row + 1 == col and s[row] == s[col]:
                    # Two consecutive chars are a pal if they are the same.
                    pal[row][col] = True
                elif s[row] == s[col] and pal[row+1][col-1]:
                    # s[a through b] is a pal if s[a] == s[b] and
                    # s[a+1 through b-1] is a pal.
                    pal[row][col] = True

                # When a pal is found, the whole min cuts is itself
                # plus the prefix string's min cuts.
                if pal[row][col]:
                    if row == 0:
                        cuts[col] = 0
                    else:
                        cuts[col] = min(cuts[col], cuts[row-1]+1)

        return cuts[n-1]
