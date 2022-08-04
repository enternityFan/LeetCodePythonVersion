# @Time : 2022-08-04 18:58
# @Author : Phalange
# @File : 1431. 拥有最多糖果的孩子.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        maxV = max(candies)
        for each in candies:
            if each + extraCandies >= maxV:
                ans.append(True)
            else:
                ans.append(False)
        return ans
