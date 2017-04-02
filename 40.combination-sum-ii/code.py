class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # To skip duplicate elements if one element is equal to its
        # precedence.
        candidates.sort()

        ans = []
        for (i, num) in enumerate(candidates):
            # Skip duplicate elements
            if i > 0 and num == candidates[i-1]:
                continue

            if num == target:
                ans.append([num])
                continue
            elif num > target:
                continue

            # Candidates are sorted, so sub_ans won't contain duplicates
            sub_ans = self.combinationSum2(candidates[i+1:], target - num)
            if not sub_ans:
                continue

            for one_solution in sub_ans:
                one_solution.insert(0, num)
            ans.extend(sub_ans)

        return ans
