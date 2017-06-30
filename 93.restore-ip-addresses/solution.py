class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []

        start1 = 0
        for end1 in range(start1 + 1, min(start1 + 4, len(s))):
            # Lead zero is not allowed
            if end1 - start1 > 1 and s[start1] == '0':
                break

            part1 = int(s[start1:end1])
            if part1 > 255:
                continue

            start2 = end1
            for end2 in range(start2 + 1, min(start2 + 4, len(s))):
                # Lead zero is not allowed
                if end2 - start2 > 1 and s[start2] == '0':
                    break

                part2 = int(s[start2:end2])
                if part2 > 255:
                    continue

                start3 = end2
                for end3 in range(start3 + 1, min(start3 + 4, len(s))):
                    # Lead zero is not allowed
                    if end3 - start3 > 1 and s[start3] == '0':
                        break

                    part3 = int(s[start3:end3])
                    if part3 > 255:
                        continue

                    start4 = end3
                    # Lead zero is not allowed
                    if len(s) - start4 > 1 and s[start4] == '0':
                        continue

                    part4 = int(s[start4:])
                    if part4 > 255:
                        continue

                    ans.append("{}.{}.{}.{}".format(part1, part2,
                                                    part3, part4))
        return ans
