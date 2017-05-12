class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        unique = []
        for elem in path.split('/'):
            if elem == '':
                continue
            elif elem == '/':
                continue
            elif elem == '.':
                continue
            elif elem == '..':
                if unique:
                    del unique[-1]
            else:
                unique.append(elem)

        ans = '/' + '/'.join(unique)
        return ans
