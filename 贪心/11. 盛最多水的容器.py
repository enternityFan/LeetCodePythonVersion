# @Time : 2022-08-20 9:22
# @Author : Phalange
# @File : 11. 盛最多水的容器.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        r = n - 1
        l = 0
        maxVal =0
        while l < r:
            maxVal = max(maxVal,(r-l)*min(height[l],height[r]))
            if height[l] < height[r]:
                l +=1
            else:
                r-=1
        return maxVal