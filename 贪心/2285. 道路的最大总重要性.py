# @Time : 2022-09-18 12:02
# @Author : Phalange
# @File : 2285. 道路的最大总重要性.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        mycnt = [0] * n
        for road in roads:
            mycnt[road[0]] +=1
            mycnt[road[1]] +=1
        site = list(range(1,n+1))
        mycnt,site = zip(*sorted(zip(mycnt,site),key=lambda x:x[0]))
        cityVal = [0]*n
        val = 1
        for each in site:
            cityVal[each-1] = val
            val +=1
        ans = 0
        for road in roads:
            ans +=cityVal[road[0]] + cityVal[road[1]]

        return ans
n = 5
roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
print(Solution().maximumImportance(n,roads))