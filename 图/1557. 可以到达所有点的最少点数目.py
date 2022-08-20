# @Time : 2022-08-20 11:19
# @Author : Phalange
# @File : 1557. 可以到达所有点的最少点数目.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # 返回入度为0 的点
        arr = [0]*n
        for each in edges:
            arr[each[1]] =1
        ans = []
        for i in range(n):
            if arr[i] == 0:
                ans.append(i)
        return ans