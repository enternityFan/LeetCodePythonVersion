# @Time : 2022-08-09 18:31
# @Author : Phalange
# @File : 2144. 打折购买糖果的最小开销.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        idx = 0
        ans = 0
        n = len(cost)-1
        for i in range(n,-1,-1):
            if idx == 2:
                idx = 0
                continue
            else:
                ans +=cost[i]
                idx +=1
        return ans