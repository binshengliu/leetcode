class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        for (i, num) in enumerate(candidates):
            if num == target:
                ans.append([target])
                continue
            elif num > target:
                continue

            tmp_result = [num]
            result = self.combinationSum(candidates[i:], target - num)
            if not result:
                continue
            for r in result:
                r.extend(tmp_result)
            ans.extend(result)

        return ans
