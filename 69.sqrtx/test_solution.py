from solution import Solution
import math


def test_1():
    s = Solution()
    for i in range(0, 20):
        ans = s.mySqrt(i)
        assert ans == int(math.sqrt(i))
