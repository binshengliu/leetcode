import numpy as np

class Solution:
    def candy(self, ratings: List[int]) -> int:
        values = sorted(set(ratings))
        ratings = np.array(ratings)
        candies = np.ones_like(ratings)
        for value in values:
            indexes = (ratings == value).nonzero()[0]
            for i in indexes:
                left = ratings[i-1] if i > 0 else ratings[i]
                right = ratings[i+1] if i < len(ratings) - 1 else ratings[i]
                left_candies = candies[i-1] if i > 0 else 1
                right_candies = candies[i+1] if i < len(candies) - 1 else 1
                if ratings[i] > left and ratings[i] <= right:
                    candies[i] = left_candies + 1
                elif ratings[i] > right and ratings[i] <= left:
                    candies[i] = right_candies + 1
                elif ratings[i] > right and ratings[i] > left:
                    candies[i] = max(left_candies, right_candies) + 1
        return candies.sum()
