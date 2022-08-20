# @Time : 2022-08-20 11:26
# @Author : Phalange
# @File : 684. 冗余连接.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        arr = [0] *(n+1)
        ans = []
        for i in range(n):
            if arr[edges[i][0]] + arr[edges[i][1]] == 2:
                ans = edges[i]
                break
            else:
                arr[edges[i][0]] = 1
                arr[edges[i][1]] = 1
        return ans