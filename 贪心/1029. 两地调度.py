# @Time : 2022-09-29 16:18
# @Author : Phalange
# @File : 1029. 两地调度.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        costs = sorted(costs,key=lambda x:x[1]-x[0])

        ans = 0
        n = len(costs) // 2
        for i,each in enumerate(costs):

            if i < n:
                ans +=each[1]
            else:
                ans +=each[0]

        return ans
print(Solution().twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))