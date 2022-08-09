# @Time : 2022-08-09 18:06
# @Author : Phalange
# @File : 2078. 两栋颜色不同且距离最远的房子.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        l = 0
        r = n-1
        maxDist = -1000
        while l!=r:
            if colors[l] != colors[r]:
                maxDist = r - l
                break
            r -=1

        r = n - 1
        while l !=r:
            if colors[l] !=colors[r]:
                maxDist = max(maxDist,r - l)
                break
            l +=1
        return maxDist
