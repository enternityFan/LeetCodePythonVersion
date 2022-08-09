# @Time : 2022-08-09 17:31
# @Author : Phalange
# @File : 1833. 雪糕的最大数量.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans = 0
        for i in range(len(costs)):
            if costs[i] <=coins:
                ans +=1
                coins -=costs[i]
            else:
                break#买不起了
        return ans
