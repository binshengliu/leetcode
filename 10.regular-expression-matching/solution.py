# Watch https://www.youtube.com/watch?v=l3hda49XcDE for how to solve this
# problem using Dynamic Programming.

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        # Initializing to None is for debugging purpose
        T = [[None for pi in range(len(p) + 1)] for si in range(len(s) + 1)]

        T[0][0] = True

        for i in range(1, len(T)):
            T[i][0] = False

        for i in range(1, len(T[0])):
            if p[i - 1] == '*':
                T[0][i] = T[0][i - 2]
            else:
                T[0][i] = False
            # print('T[{}][{}] = {}'.format(0, i, T[0][i]))

        for i in range(1, len(T)):
            for j in range(1, len(T[0])):
                # print('char: {}, pattern: {}'.format(s[i - 1], p[j - 1]))

                if s[i - 1] == p[j - 1] or '.' == p[j - 1]:
                    T[i][j] = T[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if T[i][j - 2]:
                        T[i][j] =  T[i][j - 2]
                    elif s[i - 1] == p[j - 2] or '.' == p[j - 2]:
                        T[i][j] = T[i - 1][j]
                    else:
                        T[i][j] = False
                else:
                    T[i][j] = False

                # print('T[{}][{}] = {}'.format(i, j, T[i][j]))

        # print(T)
        return T[-1][-1]
